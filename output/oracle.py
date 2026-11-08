import ctypes
import os
import struct
import subprocess
import time
from ctypes import wintypes

ORACLE_EMU_DIR = r"C:\Users\Admin\Downloads\[paste-co.de] python offset dumper__\emulator"
ORACLE_EMU_FILE = "emu.h"

V114_DIR = r"C:\Users\Admin\Downloads\emulator\emulator\emulator"
V114_OFFSETS = os.path.join(V114_DIR, "include", "emulator", "offsets.h")
V114_CONFIG = os.path.join(V114_DIR, "include", "config", "config.h")
V114_PAYLOAD = os.path.join(V114_DIR, "payload", "RobloxPlayerBeta.bin")
V114_PACKED = os.path.join(V114_DIR, "res", "RobloxPlayerBeta.7z")
V114_7Z = r"C:\Users\Admin\Downloads\emulator\emulator\deps\7zip\7z.exe"

V114_TEXT_RVA = 0x1000
V114_TEXT_MAP = 0x6435000
V114_TEXT_PAD = 0x1000
V114_TEXT_SIZE = V114_TEXT_MAP + 0xE00

_TH32CS_SNAPMODULE = 0x8
_TH32CS_SNAPMODULE32 = 0x10


class _MODULEENTRY32(ctypes.Structure):
    _fields_ = [
        ("dwSize", wintypes.DWORD),
        ("th32ModuleID", wintypes.DWORD),
        ("th32ProcessID", wintypes.DWORD),
        ("GlblcntUsage", wintypes.DWORD),
        ("ProccntUsage", wintypes.DWORD),
        ("modBaseAddr", ctypes.POINTER(ctypes.c_byte)),
        ("modBaseSize", wintypes.DWORD),
        ("hModule", wintypes.HMODULE),
        ("szModule", ctypes.c_char * 256),
        ("szExePath", ctypes.c_char * 260),
    ]


def _u16(b, o):
    return struct.unpack_from("<H", b, o)[0]


def _u32(b, o):
    return struct.unpack_from("<I", b, o)[0]


def _u64(b, o):
    return struct.unpack_from("<Q", b, o)[0]


def _modules(pid):
    k32 = ctypes.WinDLL("kernel32", use_last_error=True)
    snap = k32.CreateToolhelp32Snapshot(_TH32CS_SNAPMODULE | _TH32CS_SNAPMODULE32, pid)
    if snap == -1:
        return []
    me = _MODULEENTRY32()
    me.dwSize = ctypes.sizeof(_MODULEENTRY32)
    out = []
    try:
        if k32.Module32First(snap, ctypes.byref(me)):
            while True:
                base = ctypes.cast(me.modBaseAddr, ctypes.c_void_p).value
                out.append((base, me.modBaseSize, me.szModule.decode(errors="replace")))
                if not k32.Module32Next(snap, ctypes.byref(me)):
                    break
    finally:
        k32.CloseHandle(snap)
    return out


def _read(reader, addr, size):
    try:
        return reader.try_read(addr, size)
    except Exception:
        return None


def _export_map(reader, mod_base):
    hdr = _read(reader, mod_base, 0x400)
    if not hdr or hdr[:2] != b"MZ":
        return {}
    e = _u32(hdr, 0x3C)
    if e < 0x40 or e > 0x1000:
        return {}
    nt = _read(reader, mod_base + e, 0x18 + 0xF0)
    if not nt or nt[:4] != b"PE\x00\x00":
        return {}
    dd = 0x18 + 0x70
    exp_rva = _u32(nt, dd)
    exp_size = _u32(nt, dd + 4)
    if not exp_rva or exp_size < 0x28 or exp_rva > 0x1000000:
        return {}
    ed = _read(reader, mod_base + exp_rva, 0x28)
    if not ed:
        return {}
    n_funcs = _u32(ed, 0x14)
    n_names = _u32(ed, 0x18)
    fun_rva = _u32(ed, 0x1C)
    nam_rva = _u32(ed, 0x20)
    ord_rva = _u32(ed, 0x24)
    if not n_names or n_names > 0x20000 or not fun_rva or not nam_rva or not ord_rva:
        return {}
    fns = _read(reader, mod_base + fun_rva, 4 * n_funcs)
    names = _read(reader, mod_base + nam_rva, 4 * n_names)
    ords = _read(reader, mod_base + ord_rva, 2 * n_names)
    if not fns or not names or not ords:
        return {}
    out = {}
    for i in range(n_names):
        ordi = _u16(ords, i * 2)
        if ordi >= n_funcs:
            continue
        nrva = _u32(names, i * 4)
        if not nrva:
            continue
        nm = _read(reader, mod_base + nrva, 0x40)
        if not nm:
            continue
        nul = nm.find(b"\x00")
        if nul <= 0:
            continue
        fn_off = _u32(fns, ordi * 4)
        if fn_off == 0:
            continue
        if exp_rva <= fn_off < exp_rva + exp_size:
            continue
        out.setdefault(fn_off, nm[:nul].decode(errors="replace"))
    return out


def _scan_iat(image, base, size_image, mods):
    ext = [(mb, mb + ms, nm) for mb, ms, nm in mods if not (mb <= base < mb + ms)]
    zone_lo = 0x6436000
    zone_hi = min(len(image) - 8, 0x643A000)
    slots = []
    p = zone_lo
    while p < zone_hi:
        v = _u64(image, p)
        if v:
            for a, b, nm in ext:
                if a <= v < b:
                    slots.append((p, v, nm))
                    break
        p += 8
    runs = []
    cur = []
    prev = None
    for slot_rva, target, owner in slots:
        if prev is not None and slot_rva - prev[0] == 8 and owner == prev[2]:
            cur.append((slot_rva, target, owner))
        else:
            if len(cur) >= 2:
                runs.append(cur)
            cur = [(slot_rva, target, owner)]
        prev = (slot_rva, target, owner)
    if len(cur) >= 2:
        runs.append(cur)
    flat = []
    for run in runs:
        flat.extend(run)
    return flat


def _find_pdata(image, size_image):
    nsec = _u16(image, _u32(image, 0x3C) + 0x6)
    sec0 = _u32(image, 0x3C) + 0x18 + _u16(image, _u32(image, 0x3C) + 0x14)
    best = None
    for i in range(nsec):
        off = sec0 + i * 40
        vsz = _u32(image, off + 8)
        va = _u32(image, off + 12)
        if vsz < 0x10000 or va + vsz > len(image):
            continue
        count = 0
        prev = 0
        ok = True
        end = va + vsz
        p = va
        while p + 12 <= end:
            b_, e_, un = struct.unpack_from("<III", image, p)
            if b_ < prev or b_ < 0x1000 or b_ >= e_ or e_ > size_image or un >= size_image:
                break
            prev = b_
            count += 1
            p += 12
        if ok and count > 0x10000:
            if best is None or count > best[1]:
                best = (va, count)
    return best


def _find_tls_array(image, base, size_image):
    def in_exe(v):
        return base <= v < base + size_image

    lo, hi = 0x6436000, min(len(image) - 64, 0x80F1000)
    candidates = {}
    p = lo
    while p < hi:
        w = struct.unpack_from("<4Q", image, p)
        if in_exe(w[0]) and in_exe(w[3]) and (w[3] - w[0]) == 0x10 and \
           in_exe(w[1]) and in_exe(w[2]) and 0x100 <= (w[2] - w[1]) <= 0x1000:
            crt = 0
            for v in w:
                if image[v - base:v - base + 3] == b"\x48\x8B\x89" or \
                   image[v - base:v - base + 3] == b"\x48\x8D\x0D":
                    crt += 1
            if crt:
                key = tuple(v - base for v in w)
                candidates[key] = candidates.get(key, 0) + 1
        p += 8
    if not candidates:
        return None
    best = max(candidates.items(), key=lambda kv: (kv[1], sum(1 for v in kv[0] if image[v:v + 3] == b"\x48\x8B\x89")))
    return list(best[0])


def _find_yara(image):
    ye = bytes([0x40, 0x53, 0x48, 0x83, 0xEC, 0x30, 0x33, 0xC0, 0x48, 0x8B, 0xDA, 0x8B, 0x51, 0x08, 0x48, 0x8B])
    end = min(len(image), 0x643358C)
    p = 0x1000
    while True:
        p = image.find(ye, p, end)
        if p == -1:
            return None
        return p


def _find_pkt(image, yara):
    end = min(len(image), 0x643358C)
    lo = yara + 0x800
    hi = min(end - 24, yara + 0x30000)
    cands = []
    p = lo
    while p < hi:
        if image[p] == 0x48 and image[p + 1] == 0x83 and image[p + 2] == 0xEC and \
           image[p + 4] == 0x48 and image[p + 5] == 0x8B and image[p + 6] == 0x05 and \
           image[p + 14] == 0x48 and image[p + 15] == 0x89 and \
           image[p + 16] in (0x84, 0x44) and image[p + 17] == 0x24:
            cands.append(p)
        p += 1
    if not cands:
        return None
    target = 0x2D60
    return min(cands, key=lambda c: abs((c - yara) - target))


def _hx(v):
    return f"0x{v:08X}u"


def _find_stub_target(image, base, entry, size_image):
    stub = image[entry:entry + 12]
    if stub[:2] == b"\x48\xB8" and stub[10:12] == b"\xFF\xE0":
        t = _u64(image, entry + 2)
        if base <= t < base + size_image:
            return t - base
    return None


def _find_kpng(image):
    end = min(len(image), 0x643358C)
    for pat in (b"\x44\x8B\x65\xD0\x45\x0B\xE2", b"\x44\x8B\x7D\xB8\x45\x0B\xFA"):
        p = image.find(pat, 0x1000, end)
        if p != -1:
            return p
    return None


def _klua_candidates(image):
    end = min(len(image), 0x643358C)
    pat = b"\x40\x53\x48\x83\xEC\x30\x48\x8B\xDA\x48"
    out = []
    p = 0x1000
    while True:
        p = image.find(pat, p, end)
        if p == -1:
            return out
        out.append(p)
        p += 1


def _find_klua(image):
    for cand in _klua_candidates(image):
        if b"\xC7\x02" in image[cand + 10:cand + 0x20]:
            return cand
    return None


def _find_kproxy(image):
    end = min(len(image), 0x643358C)
    p = 0x1000
    while True:
        p = image.find(b"\x80\x3D", p, end)
        if p == -1:
            return None
        d = struct.unpack_from("<i", image, p + 2)[0]
        g = p + 6 + d
        if 0x80F1000 <= g <= 0x8F987D0 and image[p + 6] == 0x01:
            lim = min(p + 0x30, end - 7)
            q = p + 7
            while q < lim:
                if image[q] == 0xC6 and image[q + 1] == 0x05:
                    d2 = struct.unpack_from("<i", image, q + 2)[0]
                    if q + 6 + d2 == g and image[q + 6] == 0x00:
                        return g
                q += 1
        p += 1


def _render_off_v114(version, image, base, pdata, tls, kpng, klua, kproxy, klua_cands, entries, missing):
    e = _u32(image, 0x3C)
    entry = _u32(image, e + 0x18 + 0x10)
    size_image = _u32(image, e + 0x18 + 0x38)
    ent = _find_stub_target(image, base, entry, size_image)

    lines = []
    lines.append("// made and updated by oracle")
    lines.append(f"// regenerated by minh dumper (by minhlo123df) for {version}")
    lines.append(f"// generated {time.strftime('%d/%m/%Y %H:%M')} from the live client")
    lines.append("// STALE (kept from build cec3ad5889b447cf, could not be re-derived): kMux, kProxy, kIdJson")
    if klua is None:
        lines.append("// STALE: kLua could not be identified (many prologue matches); candidates for manual pick below")
    if missing:
        lines.append(f"// note: {missing} import slots had no resolvable export name and were skipped")
    lines.append("#pragma once")
    lines.append("")
    lines.append("#include <cstddef>")
    lines.append("#include <cstdint>")
    lines.append("")
    lines.append("namespace off {")
    lines.append("")
    lines.append("struct Import {")
    lines.append("    const char *Mod;")
    lines.append("    const char *Fn;")
    lines.append("    std::uint32_t Rva;")
    lines.append("};")
    lines.append("")
    lines.append(f"inline constexpr std::uint32_t kEpOrig = {_hx(entry)};")
    lines.append(f"inline constexpr std::uint32_t kEpNew = {_hx(ent if ent is not None else 0x05B58F10)};" + ("" if ent is not None else " // STALE"))
    lines.append(f"inline constexpr std::uint32_t kRuntime = {_hx(pdata[0] if pdata else 0x08C0F000)};")
    lines.append(f"inline constexpr std::uint32_t kRtCount = {_hx(pdata[1] if pdata else 0x00045B9B)};")
    lines.append(f"inline constexpr std::uint32_t kMux = {_hx(0x08A76550)}; // STALE")
    lines.append(f"inline constexpr std::uint32_t kProxy = {_hx(kproxy if kproxy is not None else 0x07E69320)};" + ("" if kproxy is not None else " // STALE"))
    lines.append(f"inline constexpr std::uint32_t kPng = {_hx(kpng if kpng is not None else 0x0481586D)};" + ("" if kpng is not None else " // STALE"))
    lines.append(f"inline constexpr std::uint32_t kLua = {_hx(klua if klua is not None else 0x041922A0)};" + ("" if klua is not None else " // STALE"))
    lines.append(f"inline constexpr std::uint32_t kTraySpawn = {_hx(0x0078B692)}; // STALE")
    lines.append(f"inline constexpr std::uint32_t kTrayClose = {_hx(0x007514D4)}; // STALE")
    lines.append(f"inline constexpr std::uint32_t kIdJson = {_hx(0x02E014F0)}; // STALE")
    if tls:
        lines.append("inline constexpr std::uint32_t kTls[] = {")
        for v in tls:
            lines.append(f"    {_hx(v)},")
        lines.append("};")
    else:
        lines.append("inline constexpr std::uint32_t kTls[] = {")
        for v in (0x00704F70, 0x05B58700, 0x05B58B50, 0x00704F80):
            lines.append(f"    {_hx(v)},")
        lines.append("}; // STALE")
    lines.append("inline constexpr Import kImports[] = {")
    for m_, f_, r_ in entries:
        lines.append(f'    {{"{m_}", "{f_}", {_hx(r_)}}},')
    lines.append("};")
    lines.append("inline constexpr std::size_t kImportCount = sizeof(kImports) / sizeof(kImports[0]);")
    if klua is None and klua_cands:
        lines.append(f"// kLua candidates (40 53 48 83 EC 30 48 8B DA 48): {', '.join(_hx(c) for c in klua_cands[:24])}")
    lines.append("")
    lines.append("}")
    lines.append("")
    return "\n".join(lines)


def _banner_config(version, pdata, size_image, text_map=V114_TEXT_MAP):
    nr = pdata[1] if pdata else 0x00045B9B
    text_size = text_map + 0xE00
    lines = []
    lines.append("#pragma once")
    lines.append("")
    lines.append("#include <cstdint>")
    lines.append("")
    lines.append('#include "emulator/offsets.h"')
    lines.append("")
    lines.append("namespace emu {")
    lines.append("")
    lines.append("inline constexpr bool kRandHwid = true; // turn this off if u dont want hwid seed randomization")
    lines.append("inline constexpr bool kRandId = false; // kIdJson not re-derived for this build yet")
    lines.append("inline constexpr bool kCloseInsteadOfTray = false; // kTray sites not re-derived for this build yet")
    lines.append("inline constexpr bool kProxyPatch = false; // kProxy site not re-derived for this build yet")
    lines.append("inline constexpr bool kLoadMod = true; // toggle this if u want it to load a module on startup, configure it below")
    lines.append('inline constexpr wchar_t kModDll[] = L"bohrium.dll"; // linked to the bohrium module (falls back via kLoadMod)')
    lines.append("")
    lines.append(f"inline constexpr std::uint32_t kImageSize = {_hx(size_image)};")
    lines.append(f"inline constexpr std::uint32_t kTextRva = {_hx(V114_TEXT_RVA)};")
    lines.append(f"inline constexpr std::uint32_t kTextSize = {_hx(text_size)};")
    lines.append(f"inline constexpr std::uint32_t kTextMap = {_hx(text_map)};")
    lines.append(f"inline constexpr std::uint32_t kTextPad = {_hx(V114_TEXT_PAD)};")
    lines.append("inline constexpr std::uint32_t kRtOff = kTextSize;")
    lines.append("inline constexpr std::uint32_t kRtSize = off::kRtCount * 12u;")
    lines.append("inline constexpr std::uint32_t kPayloadSize = kTextSize + 8u + kRtSize;")
    lines.append("")
    lines.append("}")
    lines.append("")
    return "\n".join(lines)


def write_oracle_v114(version, reader, image, base):
    if not os.path.isdir(V114_DIR):
        return False
    e = _u32(image, 0x3C)
    size_image = _u32(image, e + 0x18 + 0x38)
    pdata = _find_pdata(image, size_image)
    tls = _find_tls_array(image, base, size_image)
    kpng = _find_kpng(image)
    klua = _find_klua(image)
    kproxy = _find_kproxy(image)
    klua_cands = _klua_candidates(image)

    pid = getattr(reader, "pid", None)
    if pid is None:
        from memory.reader import find_roblox_process
        pid = find_roblox_process()
    mods = _modules(pid)
    iat = _scan_iat(image, base, size_image, mods)
    export_cache = {}
    entries = []
    missing = 0
    for slot_rva, target, owner in iat:
        obase = None
        for mb, ms, nm in mods:
            if mb <= target < mb + ms:
                obase = mb
                break
        if obase is None:
            missing += 1
            continue
        if obase not in export_cache:
            export_cache[obase] = _export_map(reader, obase)
        found = export_cache[obase].get(target - obase)
        if not found:
            missing += 1
            continue
        entries.append((owner.lower(), found, slot_rva))

    if iat:
        first_slot = min(s[0] for s in iat)
        text_map = (first_slot & ~0xFFF) - V114_TEXT_RVA
    else:
        text_map = V114_TEXT_MAP
    text_size = text_map + 0xE00

    offsets_text = _render_off_v114(version, image, base, pdata, tls, kpng, klua, kproxy, klua_cands, entries, missing)
    config_text = _banner_config(version, pdata, size_image, text_map)
    with open(V114_OFFSETS, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(offsets_text)
    with open(V114_CONFIG, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(config_text)

    if pdata:
        rt_va, nr = pdata
        text = image[V114_TEXT_RVA:V114_TEXT_RVA + text_size]
        pbytes = image[rt_va:rt_va + nr * 12]
        raw = text + struct.pack("<Q", nr) + pbytes
        with open(V114_PAYLOAD, "wb") as handle:
            handle.write(raw)
        if os.path.isfile(V114_7Z):
            if os.path.isfile(V114_PACKED):
                os.remove(V114_PACKED)
            try:
                subprocess.run(
                    [V114_7Z, "a", "-t7z", "-m0=lzma2", "-mx=7", V114_PACKED, V114_PAYLOAD],
                    capture_output=True, timeout=600)
            except Exception:
                pass

    return True


def render_oracle_emu(version, reader, image, base):
    e = _u32(image, 0x3C)
    opt = e + 0x18
    entry = _u32(image, opt + 0x10)
    size_image = _u32(image, opt + 0x38)

    ent = None
    stub = image[entry:entry + 12]
    if stub[:2] == b"\x48\xB8" and stub[10:12] == b"\xFF\xE0":
        t = _u64(image, entry + 2)
        if base <= t < base + size_image:
            ent = t - base

    pdata = _find_pdata(image, size_image)
    tls = _find_tls_array(image, base, size_image)
    yara = _find_yara(image)
    pkt = _find_pkt(image, yara) if yara else None

    pid = getattr(reader, "pid", None)
    if pid is None:
        from memory.reader import find_roblox_process
        pid = find_roblox_process()
    mods = _modules(pid)

    iat = _scan_iat(image, base, size_image, mods)
    export_cache = {}
    entries = []
    missing = 0
    for slot_rva, target, owner in iat:
        key = target
        found = None
        obase = None
        for mb, ms, nm in mods:
            if mb <= target < mb + ms:
                obase = mb
                break
        if obase is None:
            missing += 1
            continue
        if obase not in export_cache:
            export_cache[obase] = _export_map(reader, obase)
        found = export_cache[obase].get(target - obase)
        if not found:
            missing += 1
            continue
        entries.append((owner.lower(), found, slot_rva))

    stale = []
    if ent is None:
        stale.append("ent")
    if pdata is None:
        stale.append("rt/nr")
    if tls is None:
        stale.append("tls")
    if yara is None:
        stale.append("yara")
    if pkt is None:
        stale.append("pkt")
    stale.extend(["mux", "prc", "png"])

    lines = []
    lines.append("// made and updated by oracle")
    lines.append(f"// regenerated by minh dumper (by minhlo123df) for {version}")
    lines.append(f"// generated {time.strftime('%d/%m/%Y %H:%M')} from the live client")
    if stale:
        lines.append("// STALE (kept from build 02c37bc51a384b8f, could not be re-derived): "
                     + ", ".join(stale))
    if missing:
        lines.append(f"// note: {missing} import slots had no resolvable export name and were skipped")
    lines.append("#pragma once")
    lines.append("#include <cstddef>")
    lines.append("#include <cstdint>")
    lines.append("")
    lines.append("namespace m {")
    lines.append("struct rec {")
    lines.append("  const char *m;")
    lines.append("  const char *f;")
    lines.append("  std::uint32_t r;")
    lines.append("};")
    lines.append(f"inline constexpr std::uint32_t isz = {_hx(size_image)};")
    old_v = entry if entry else 0x0909C004
    ent_v = ent if ent is not None else 0x05B779F0
    note = "  // STALE" if ent is None else ""
    lines.append(f"inline constexpr std::uint32_t old = {_hx(old_v)};")
    lines.append(f"inline constexpr std::uint32_t ent = {_hx(ent_v)};{note}")
    rt_v = pdata[0] if pdata else 0x08B93000
    nr_v = pdata[1] if pdata else 0x00044DAE
    note2 = "  // STALE" if pdata is None else ""
    lines.append(f"inline constexpr std::uint32_t rt = {_hx(rt_v)};")
    lines.append(f"inline constexpr std::uint32_t nr = {_hx(nr_v)};{note2}")
    lines.append(f"inline constexpr std::uint32_t mux = {_hx(0x08A0C938)};  // STALE")
    yara_v = yara if yara else 0x04E57C80
    note3 = "" if yara else "  // STALE"
    lines.append(f"inline constexpr std::uint32_t yara = {_hx(yara_v)};{note3}")
    pkt_v = pkt if pkt else 0x04E579E0
    note4 = "" if pkt else "  // STALE"
    lines.append(f"inline constexpr std::uint32_t pkt = {_hx(pkt_v)};{note4}")
    lines.append(f"inline constexpr std::uint32_t prc = {_hx(0x07E254C0)};  // STALE")
    lines.append(f"inline constexpr std::uint32_t png = {_hx(0x0484DC0D)};  // STALE")
    if tls:
        lines.append("inline constexpr std::uint32_t tls[] = {")
        for v in tls:
            lines.append(f"    {_hx(v)},")
        lines.append("};")
    else:
        lines.append("inline constexpr std::uint32_t tls[] = {")
        for v in (0x007ED3F0, 0x05B771E0, 0x05B77630, 0x007ED400):
            lines.append(f"    {_hx(v)},")
        lines.append("};  // STALE")
    lines.append("inline constexpr rec im[] = {")
    for m_, f_, r_ in entries:
        lines.append(f'    {{"{m_}", "{f_}", {_hx(r_)}}},')
    lines.append("};")
    lines.append("inline constexpr std::size_t ni = sizeof(im) / sizeof(im[0]);")
    lines.append("} // namespace m")
    lines.append("")
    return "\n".join(lines)
