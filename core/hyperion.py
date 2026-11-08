import struct

from guides.guides import _resolve_guide, _func_start_before
from xrefs.xrefs import _cached_xref_map
from ib.decode import decode_one, rip_target, call_target, scan_string_rva


_KTABLE_ANCHOR = b"Trying to call method on object of type: `%s` with incorrect arguments."

_PROLOGUES = (
    b"\x40\x55\x53\x56\x57\x41\x54\x41\x55\x41\x56\x41\x57",
    b"\x48\x8B\xC4",
    b"\x48\x89\x54\x24",
    b"\x48\x89\x4C\x24",
    b"\x48\x89\x5C\x24",
    b"\x40\x53\x56\x57",
    b"\x40\x55\x53\x56",
    b"\x55\x53\x56\x57",
)


def _valid_rva(image, rva):
    return 0 <= rva < len(image)


def _prologue_start(image, base, site_rva, window=0x6000):
    lo = max(0x1000, site_rva - window)
    best = None
    best_score = -1
    for pat in _PROLOGUES:
        pos = image.rfind(pat, lo, site_rva)
        while pos != -1:
            before = image[pos - 1] if pos > 0 else 0
            score = 0
            if before in (0xCC, 0xC3, 0x90, 0x00):
                score += 10
            if pat[:2] in (b"\x40\x55", b"\x55\x53"):
                score += 1
            score += pos / float(len(image))
            if score > best_score:
                best = pos
                best_score = score
            pos = image.rfind(pat, lo, pos)
    return best


def _real_calls_after(image, base, site_rva, window=0x400, limit=6):
    at = base + site_rva
    end = at + window
    calls = []
    while at < end and len(calls) < limit:
        ins = decode_one(image, at, base)
        if ins is None:
            at += 1
            continue
        if ins.mnem == "call":
            t = call_target(ins)
            if t and 0x10000 <= t - base < len(image):
                calls.append(t - base)
        at += ins.size
    return calls


def _last_call_before(image, base, site_rva, window=0x240):
    at = base + max(0x1000, site_rva - window)
    end = base + site_rva
    last = None
    while at < end:
        ins = decode_one(image, at, base)
        if ins is None:
            at += 1
            continue
        if ins.mnem == "call":
            t = call_target(ins)
            if t and 0x10000 <= t - base < len(image):
                last = t - base
        at += ins.size
    return last


def _resolve_nilobject(image, base, store):
    xr = _cached_xref_map(image)

    ranked = []
    for target, hits in xr.items():
        if len(hits) < 24 or target < 0x6000000 or target > len(image) - 16:
            continue
        if image[target:target + 16] != b"\x00" * 16:
            continue
        ranked.append((len(hits), target))
    ranked.sort(reverse=True)
    for top_n, top_t in ranked[:8]:
        dummynode = top_t - 0x560
        if not _valid_rva(image, dummynode):
            continue
        if image[dummynode:dummynode + 16] != b"\x00" * 16:
            continue
        if len(xr.get(dummynode, [])) < 16:
            continue
        store.setdefault(("Luau",), {})["luaH_dummynode"] = dummynode
        return top_t

    dummynode = store.get(("Luau",), {}).get("luaH_dummynode")
    if dummynode:
        cand = dummynode + 0x560
        if _valid_rva(image, cand) and image[cand:cand + 16] == b"\x00" * 16 \
                and len(xr.get(cand, [])) >= 32:
            return cand
        best = None
        for target, hits in xr.items():
            if abs(target - dummynode) > 0x1000 or len(hits) < 32:
                continue
            if not _valid_rva(image, target) or image[target:target + 16] != b"\x00" * 16:
                continue
            if best is None or len(hits) > best[1]:
                best = (target, len(hits))
        if best:
            return best[0]
    return 0


def _resolve_ktable(image, base, store):
    from patterns.patterns import _signature_regex
    rx = _signature_regex("48 8d 0d ? ? ? ? 48 8d 54 24 ? 48 8b 04 c1")
    for m in rx.finditer(image, 0x1000, len(image)):
        h = m.start()
        disp = struct.unpack_from("<i", image, h + 3)[0]
        target = h + 7 + disp
        if 0x80F1000 <= target <= 0x8F987D0:
            return target

    xr = _cached_xref_map(image)
    pos = image.find(_KTABLE_ANCHOR)
    if pos == -1:
        return 0
    sites = xr.get(pos)
    if not sites:
        return 0
    excluded = set()
    for ns in (("Luau",), ("Hyperion",)):
        fields = store.get(ns, {})
        for key in ("luaH_dummynode", "LuaO_NilObject"):
            value = fields.get(key)
            if value:
                excluded.add(value)
    targets = {}
    for site in sites:
        func_va = _func_start_before(image, base, base + site)
        lo = (func_va - base) if func_va else max(0, site - 0x400)
        hi = lo + 0x2000
        for target, target_sites in xr.items():
            for s in target_sites:
                if lo <= s < hi:
                    targets.setdefault(target, 0)
                    targets[target] += 1
    best, best_score = None, -1
    for target, hits in targets.items():
        if target < 0x6436000 or target > len(image) - 16:
            continue
        if target in excluded:
            continue
        chunk = image[target:target + 1]
        if not chunk or 0x20 <= chunk[0] < 0x7F:
            continue
        value = int.from_bytes(image[target:target + 8], "little")
        if not (value == 0 or 0x10000 <= value < 0x7FFFFFFFFFFF):
            continue
        score = (1 if value else 0) + min(hits, 3)
        if score > best_score:
            best, best_score = target, score
    return best or 0


def _resolve_identity(image, base, store):
    import re
    from patterns.patterns import _signature_regex
    sig = _signature_regex(
        "40 53 48 83 EC ? 48 8B D9 48 8B 0D ? ? ? ? E8")
    results = []
    for m in sig.finditer(image, 0x1000, min(len(image), 0x643458c)):
        start = m.start()
        va = base + start
        seq = []
        saw_call = False
        while va < base + start + 0x40:
            ins = decode_one(image, va, base)
            if ins is None:
                break
            seq.append(ins)
            if saw_call:
                break
            if ins.mnem == "call":
                saw_call = True
            va += ins.size
        for i, ins in enumerate(seq):
            if ins.mnem == "call":
                prev = None
                for j in range(i - 1, -1, -1):
                    if seq[j].mnem == "mov" and "[rip" in seq[j].ops:
                        prev = seq[j]
                        break
                if prev is None:
                    continue
                g = rip_target(prev, base)
                callee = call_target(ins) - base
                nxt = seq[i + 1] if i + 1 < len(seq) else None
                if g and 0x80F1000 <= g <= 0x8F987D0 and nxt and nxt.mnem == "lea":
                    value = struct.unpack_from("<Q", image, g)[0]
                    results.append((start, g, callee, value))
    if not results:
        return None
    start, g, callee, value = results[0]
    return {"Identity": g, "GetIdentityStruct": callee, "PrintIdentity": start}


def _resolve_flagbank(image, base, store):
    xr = _cached_xref_map(image)
    banks = []
    for anchor in (b"EnableLoadModule", b"AnimGraphServerAuthorityNodeIndices"):
        pos = image.find(anchor)
        if pos == -1:
            continue
        if image[pos - 1:pos] == b"\x00":
            pos -= 1
        sites = xr.get(pos) or xr.get(pos + 1) or []
        if not sites:
            continue
        fs = _prologue_start(image, base, sites[0], window=0x600)
        if fs is None:
            continue
        va = base + fs
        end = base + fs + 0x120
        seen_before = None
        while va < end:
            ins = decode_one(image, va, base)
            if ins is None:
                va += 1
                continue
            if ins.mnem == "mov" and "[rip" in ins.ops:
                t = rip_target(ins, base)
                if t and 0x80F1000 <= t <= 0x8F987D0:
                    seen_before = t
            if ins.mnem == "call":
                break
            va += ins.size
        if seen_before:
            banks.append(seen_before)
    if not banks:
        return None
    if len(banks) >= 2 and banks[0] != banks[1]:
        return None
    return banks[0]


def _resolve_proximity_prompt(image, base, store):
    pos = image.find(b"ProximityPrompt_Triggered")
    if pos == -1:
        return None
    text_end = min(len(image), 0x643458C)
    sites = []
    for modrm_val in (0x05, 0x0D, 0x15, 0x1D, 0x25, 0x2D, 0x35, 0x3D):
        modrm = bytes((modrm_val,))
        q = image.find(modrm, 0x1000, text_end - 5)
        while q != -1:
            disp = struct.unpack_from("<i", image, q + 1)[0]
            if q + 5 + disp == pos:
                sites.append(q)
            q = image.find(modrm, q + 1, text_end - 5)
    if not sites:
        return None
    site = sites[0]
    fs = _prologue_start(image, base, site, window=0x10000)
    if fs is None:
        fs_va = _func_start_before(image, base, base + site, window=0x10000)
        fs = (fs_va - base) if fs_va else None
    if fs is None:
        return None
    return {"FireProximityPrompt": fs}


def _resolve_touch_interest(image, base, store):
    pos = image.find(b"new overlap in different world")
    sites = _cached_xref_map(image).get(pos, [])
    if not sites:
        return None
    for site in sites:
        calls = _real_calls_after(image, base, site, window=0x300, limit=6)
        if len(calls) >= 3:
            return {"FireTouchInterest": calls[2]}
        if len(calls) == 2:
            return {"FireTouchInterest": calls[1]}
    return None


def _resolve_disconnect(image, base, store):
    pos = image.find(b"Function Connection.Disconnect is not safe to call in parallel")
    sites = _cached_xref_map(image).get(pos, [])
    if not sites:
        return None
    fs = _prologue_start(image, base, sites[0], window=0x4000)
    if fs is None:
        return None
    return {"DisconnectConnect": fs}


def _resolve_castargs(image, base, store):
    pos = image.find(b"Argument %d missing or nil")
    sites = _cached_xref_map(image).get(pos, [])
    if len(sites) < 2:
        return None
    site = sites[1]
    fs = _prologue_start(image, base, site, window=0x8000)
    if fs is None:
        return None
    calls = _real_calls_after(image, base, fs, window=0x200, limit=4)
    if len(calls) < 2:
        return None
    return {"CastArgs": calls[1]}


def _resolve_getproperty(image, base, store):
    needle = b"Could not find property descriptor"
    pos = image.find(needle)
    while pos != -1:
        sites = _cached_xref_map(image).get(pos, [])
        if sites:
            for site in sites:
                at = base + max(0x1000, site - 0x180)
                end = base + site
                insns = []
                while at < end:
                    ins = decode_one(image, at, base)
                    if ins is None:
                        at += 1
                        continue
                    insns.append(ins)
                    at += ins.size
                for i in range(len(insns) - 1, -1, -1):
                    ins = insns[i]
                    if ins.mnem != "call":
                        continue
                    window = insns[max(0, i - 10):i]
                    setup = any(it.mnem in ("lea", "mov") and "0x1d8]" in it.ops
                                and it.ops.startswith("rcx")
                                for it in window)
                    if setup:
                        t = call_target(ins)
                        if t and 0x10000 <= t - base < len(image):
                            return {"GetProperty": t - base}
        pos = image.find(needle, pos + 1)
    return None


def _resolve_capabilities(image, base, store):
    consts = (b"\x03\x00\x00\x00\x00\x00\x00\x20", b"\x0B\x00\x00\x00\x00\x00\x00\x30",
              b"\x0B\x00\x00\x00\x00\x00\x00\x70")
    votes = {}
    for const in consts:
        q = image.find(const, 0x1000, min(len(image), 0x643458C))
        while q != -1:
            fs = _fn_start_cc(image, q, 0x400)
            if fs:
                votes[fs] = votes.get(fs, 0) + 1
            q = image.find(const, q + 1, min(len(image), 0x643458C))
    if not votes:
        return None

    def _score(fs):
        n = votes[fs]
        body = image[fs:fs + 0x120]
        if b"\x48\x63\x01" in body[:0x10]:
            n += 2
        if any(x in body for x in (b"\x8b\x41\x30", b"\xf6\x41\x30", b"\x48\x8b\x41\x30")):
            n += 2
        idioms = body.count(b"\x74\x08\x48\x8d\x05") + body.count(b"\x73\x08\x48\x8d\x05")
        if idioms >= 3:
            n -= 4
        if b"\x48\xc7\x42\x08" in body:
            n -= 2
        return n

    best = max(votes, key=_score)
    if _score(best) <= 0:
        return None
    return {"GetCapabilities": best}


def _resolve_setfflag(image, base, store):
    from patterns.patterns import _signature_regex
    sig = _signature_regex(
        "48 89 5C 24 ? 55 56 57 41 54 41 55 41 56 41 57 48 8D AC 24 ? ? ? ? 48 81 EC")
    candidates = []
    for m in sig.finditer(image, 0x1000, min(len(image), 0x643458C)):
        start = m.start()
        va = base + start
        frame = None
        spill = False
        for _ in range(24):
            ins = decode_one(image, va, base)
            if ins is None:
                va += 1
                continue
            if ins.mnem == "arith" and "rsp" in ins.ops and "0x" in ins.ops and frame is None:
                try:
                    frame = int(ins.ops.split("0x")[-1], 16)
                except ValueError:
                    pass
            if frame is not None and ins.mnem == "mov" and ins.ops.startswith("[rsp") \
                    and ins.ops.endswith(", r9d"):
                spill = True
                break
            if ins.mnem == "ret":
                break
            va += ins.size
        if frame == 0x1D0 and spill:
            candidates.append(start)
    if not candidates:
        return None
    return {"SetFFlag": candidates[0]}


def _resolve_opcode_table(image, base, store):
    best = None
    n = len(image)
    end = min(n, 0x643458C)

    def _try(disp):
        nonlocal best
        if not (0x6436000 <= disp <= n - 256):
            return
        table = image[disp:disp + 256]
        if table != bytes(range(256)) and sorted(table) == list(range(256)):
            if best is None or disp < best:
                best = disp

    pos = 0x1000
    while pos < end - 8:
        idx = image.find(b"\x0F\xB6", pos, end)
        if idx == -1:
            break
        pos = idx + 2
        modrm = image[idx + 2]
        if 0x80 <= modrm <= 0xBF and (modrm & 7) == 4:
            sib = image[idx + 3]
            if (sib & 0xC0) == 0 and (sib & 7) != 5:
                _try(struct.unpack_from("<I", image, idx + 4)[0])

    if best is None:
        from patterns.patterns import _signature_regex
        for sig in ("0F B6 8C 30 ? ? ? ?", "42 0F B6 8C 30 ? ? ? ?"):
            rx = _signature_regex(sig)
            for m in rx.finditer(image, 0x1000, end):
                _try(struct.unpack_from("<I", image, m.start() + len(sig.split()) - 4)[0])
    if best is None:
        return None
    return {"OpcodeLookupTable": best}


def _resolve_luau_execute(image, base, store):
    from patterns.patterns import _signature_regex
    for off in range(16):
        sig = "80 79 %02X 00 0F 85 ? ? ? ? E9 ? ? ? ?" % off
        rx = _signature_regex(sig)
        for m in rx.finditer(image, 0x2500000, 0x2e00000):
            h = m.start()
            jne_rel = struct.unpack_from("<i", image, h + 6)[0]
            jne_tgt = h + 10 + jne_rel
            jmp_rel = struct.unpack_from("<i", image, h + 11)[0]
            jmp_tgt = h + 15 + jmp_rel
            if not (0x2500000 <= jne_tgt <= 0x2e00000 and 0x2500000 <= jmp_tgt <= 0x2e00000):
                continue
            if jne_tgt == jmp_tgt:
                continue
            start = h
            if h > 0 and image[h - 1] not in (0xCC, 0xC3):
                fs = _prologue_start(image, base, h, window=0x80)
                if fs is not None:
                    start = fs
            return {"Luau_Execute": start}
    return None


def _resolve_push(image, base, store):
    from patterns.patterns import _signature_regex
    sig = ("48 89 5C 24 08 57 48 83 EC ? 48 8B FA 48 8B D9 E8 ? ? ? ? "
           "84 C0 74 ? 48 8B D7 48 8B CB 48 8B 5C 24")
    rx = _signature_regex(sig)
    for m in rx.finditer(image, 0x1000, len(image)):
        return {"Push": m.start()}
    return None


def _resolve_mouse_clicks(image, base, store):
    from patterns.patterns import _signature_regex
    result = {}

    click_right = None
    head_rx = _signature_regex(
        "40 53 56 57 48 83 EC 70 49 8B 59 08 49 8B F8 48 8B F1")
    for m in head_rx.finditer(image, 0x1000, len(image)):
        click_right = m.start()
        break
    if click_right is None:
        junction = _signature_regex("49 8B 59 08 49 8B F8 48 8B F1")
        for m in junction.finditer(image, 0x1000, len(image)):
            fs = _prologue_start(image, base, m.start(), window=0x20)
            if fs is not None:
                click_right = fs
                break

    if click_right is not None:
        click_left = click_right - 0x1A0
        head = image[click_left:click_left + 4]
        readable = bool(head) and head != b"\x00" * len(head) and not head.startswith(b"\xcc")
        if click_left > 0x1000 and readable:
            result["FireLeftMouseClick"] = click_left
            result["FireRightMouseClick"] = click_right

            enter = click_left - 0x15E0
            leave = click_right - 0x15D0
            hover_head = image[enter:enter + 0x1C]
            if hover_head.startswith(
                    b"\x48\x89\x5C\x24\x20\x4C\x89\x44\x24\x18\x55\x56\x57"):
                result["FireMouseHoverEnter"] = enter
                if leave > enter and image[leave - 1] == 0xCC:
                    result["FireMouseHoverLeave"] = leave

    if "FireMouseHoverEnter" not in result:
        hover = _signature_regex(
            "48 89 5C 24 20 4C 89 44 24 18 55 56 57 41 54 41 55 41 56 41 57 48 8B EC 48 83 EC")
        for m in hover.finditer(image, 0x1000, len(image)):
            enter = m.start()
            if enter < 0x1000 or image[enter - 1] != 0xCC:
                continue
            leave = None
            lo = enter + 0x170
            hi = enter + 0x200
            pos = image.find(b"\xcc\xcc", lo, hi)
            if pos != -1:
                nxt = pos + 2
                while nxt < hi and image[nxt] == 0xCC:
                    nxt += 1
                if image[nxt:nxt + 10].startswith(b"\x48\x89\x74\x24\x10\x57\x48\x83\xEC"):
                    leave = nxt
            if leave is None:
                continue
            result["FireMouseHoverEnter"] = enter
            result["FireMouseHoverLeave"] = leave
            click_left = enter + 0x15E0
            click_right = leave + 0x15D0
            if 0x1000 < click_left < len(image) and 0x1000 < click_right < len(image):
                result["FireLeftMouseClick"] = click_left
                result["FireRightMouseClick"] = click_right
            break

    return result or None


def _fn_start_cc(image, rva, max_back=0x400):
    lo = max(0x1000, rva - max_back)
    i = rva - 1
    ccs = 0
    while i > lo:
        if image[i] == 0xCC:
            ccs += 1
            if ccs >= 2:
                j = i + 1
                while j < rva and image[j] == 0xCC:
                    j += 1
                return j
        else:
            ccs = 0
        i -= 1
    return None


def _resolve_identity_v2(image, base, store):
    caps = store.get(("Hyperion",), {}).get("GetCapabilities")
    if not caps:
        return None
    from patterns.patterns import _signature_regex
    from guides.guides import _scan_call_sites_to
    votes = {}
    for site_va in _scan_call_sites_to(image, base, caps):
        site = site_va - base
        at = base + max(0x1000, site - 0x60)
        end = base + site
        last_global = None
        last_call = None
        while at < end:
            ins = decode_one(image, at, base)
            if ins is None:
                at += 1
                continue
            if ins.mnem == "mov" and "[rip" in ins.ops:
                t = rip_target(ins, base)
                if t is not None and 0x80F1000 <= t <= 0x8F987D0:
                    last_global = t
            if ins.mnem == "call":
                t = call_target(ins)
                if t and t - base != caps:
                    last_call = t - base
            at += ins.size
        if last_global and last_call:
            votes[(last_global, last_call)] = votes.get((last_global, last_call), 0) + 1
    if not votes:
        return None
    (g, t), _ = max(votes.items(), key=lambda kv: kv[1])
    return {"Identity": g, "GetIdentityStruct": t}


def _resolve_hashlookup(image, base, store):
    pat = b"\x4C\x8B\xC9\x49\xC7\xC0\xFF\xFF\xFF\xFF"
    end = min(len(image), 0x643458C)
    pos = 0x1000
    while True:
        pos = image.find(pat, pos, end)
        if pos == -1:
            return None
        if b"\x93\x01\x00\x01" in image[pos:pos + 0x80]:
            return {"HashLookup": pos}
        pos += 1


def _resolve_taskdefer(image, base, store):
    from patterns.patterns import _signature_regex
    sig = _signature_regex(
        "48 89 5C 24 ? 48 89 6C 24 ? 56 57 41 56 48 81 EC ? ? ? ? 48 BF ? ? ? ? ? ? ? ? 49 89 C1")
    end = min(len(image), 0x643458C)
    m = sig.search(image, 0x1000, end)
    if m is None:
        return None
    return {"TaskDefer": m.start()}


def _resolve_getfflag(image, base, store):
    g = store.get(("Hyperion",), {}).get("FLogDataBank")
    if not g:
        return None
    pats = (b"\x48\x8B\x0D", b"\x48\x8B\x05", b"\x48\x8B\x15", b"\x48\x8B\x1D",
            b"\x4C\x8B\x05", b"\x4C\x8B\x0D", b"\x4C\x8B\x15", b"\x4C\x8B\x1D")
    end = min(len(image), 0x643458C)
    votes = {}
    for pat in pats:
        p = 0x1000
        while True:
            p = image.find(pat, p, end)
            if p == -1:
                break
            d = struct.unpack_from("<i", image, p + 3)[0]
            if p + 7 + d == g:
                at = base + p
                for _ in range(16):
                    ins = decode_one(image, at, base)
                    if ins is None:
                        at += 1
                        continue
                    if ins.mnem == "call":
                        t = call_target(ins)
                        if t:
                            votes[t - base] = votes.get(t - base, 0) + 1
                        break
                    at += ins.size
            p += 1
    if not votes:
        return None
    best = max(votes.items(), key=lambda kv: kv[1])[0]
    if votes[best] < 3:
        return None
    return {"GetFFlag": best}


def _resolve_network(image, base, store):
    from patterns.patterns import _signature_regex
    out = {}
    sigs = (
        ("SendRaw", "40 53 55 57 41 54 41 56 41 57 48 81 EC A8 00 00 00"),
        ("SendStream", "40 53 41 54 41 55 41 56 41 57 48 81 EC B0 00 00 00"),
        ("SendShared", "40 53 56 41 54 41 55 41 56 41 57 48 81 EC A8 00 00 00"),
    )
    for name, sig in sigs:
        rx = _signature_regex(sig)
        for m in rx.finditer(image, 0x1000, len(image)):
            out[name] = m.start()
            break
    return out or None


def dump_hyperion_offsets(image, base, store):
    def _store(fields):
        if fields:
            store.setdefault(("Hyperion",), {}).update(fields)

    try:
        rva = _resolve_nilobject(image, base, store)
        if rva:
            _store({"LuaO_NilObject": rva})
    except Exception:
        pass
    try:
        rva = _resolve_ktable(image, base, store)
        if rva:
            _store({"KTable": rva})
    except Exception:
        pass
    try:
        rva = _resolve_guide(image, base, "luaC_step")
        if rva:
            _store({"LuaC_Step": rva})
    except Exception:
        pass
    try:
        _store(_resolve_identity(image, base, store))
    except Exception:
        pass
    try:
        _store(_resolve_hashlookup(image, base, store))
    except Exception:
        pass
    try:
        _store(_resolve_taskdefer(image, base, store))
    except Exception:
        pass
    try:
        bank = _resolve_flagbank(image, base, store)
        if bank:
            _store({"FLogDataBank": bank})
    except Exception:
        pass
    try:
        _store(_resolve_getfflag(image, base, store))
    except Exception:
        pass
    try:
        _store(_resolve_proximity_prompt(image, base, store))
    except Exception:
        pass
    try:
        _store(_resolve_touch_interest(image, base, store))
    except Exception:
        pass
    try:
        _store(_resolve_disconnect(image, base, store))
    except Exception:
        pass
    try:
        _store(_resolve_castargs(image, base, store))
    except Exception:
        pass
    try:
        _store(_resolve_getproperty(image, base, store))
    except Exception:
        pass
    try:
        _store(_resolve_capabilities(image, base, store))
    except Exception:
        pass
    try:
        if "Identity" not in store.get(("Hyperion",), {}):
            _store(_resolve_identity_v2(image, base, store))
    except Exception:
        pass
    try:
        _store(_resolve_setfflag(image, base, store))
    except Exception:
        pass
    try:
        _store(_resolve_opcode_table(image, base, store))
    except Exception:
        pass
    try:
        _store(_resolve_luau_execute(image, base, store))
    except Exception:
        pass
    try:
        _store(_resolve_push(image, base, store))
    except Exception:
        pass
    try:
        _store(_resolve_mouse_clicks(image, base, store))
    except Exception:
        pass
    try:
        _store(_resolve_network(image, base, store))
    except Exception:
        pass
    return store
