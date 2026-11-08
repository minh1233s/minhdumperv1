INTERNAL_FILENAME = "internal_offsets.h"
ENCS_FILENAME = "encs.h"


_INTERNAL_MAP = (
    ("__PRINT__", ("Misc",), "Print", "0x1ce58f0"),
    ("__LUAO_NILOBJECT__", ("Hyperion",), "LuaO_NilObject", "0x667f848"),
    ("__LUAH_DUMMYNODE__", ("Luau",), "luaH_dummynode", "0x667f2e8"),
    ("__LUAD_THROW__", ("Luau",), "luaD_Throw", "0x262DDC0"),
    ("__LUAC_STEP__", ("Hyperion",), "LuaC_Step", "0x2644300"),
    ("__LUAVM_LOAD__", ("Luau",), "LuaVMLoad", "0x41a3610"),
    ("__KTABLE__", ("Hyperion",), "KTable", "0x846baa0"),
    ("__DM_SCRIPTCONTEXT__", ("DataModel",), "ScriptContext", "0x440"),
    ("__DM_CHILDREN__", ("Instance",), "ChildrenStart", "0x78"),
    ("__DM_CLASSDESCRIPTOR__", ("Instance",), "ClassDescriptor", "0x18"),
    ("__FDM_TO_DM__", ("FakeDataModel",), "RealDataModel", "0x1f8"),
    ("__FDM_POINTER__", ("FakeDataModel",), "Pointer", "0x8dc8000"),
    ("__INSTANCE_NAME__", ("Instance",), "NameContainer", "0x70"),
    ("__INSTANCE_NAME_STR__", ("Instance",), "Name", "0x8"),
    ("__SCRIPTCONTEXT_RESUME__", ("Misc",), "ScriptContextResume", "0x4258330"),
    ("__MODULESCRIPT_BYTECODE__", ("ModuleScript",), "Bytecode", "0x128"),
    ("__BYTECODE_POINTER__", ("ByteCode",), "Pointer", "0x18"),
    ("__BYTECODE_SIZE__", ("ByteCode",), "Size", "0x28"),
    ("__REFLECTION_GETPROPERTY__", ("Hyperion",), "GetProperty", "0x1d223a0"),
    ("__OPCODE_TABLE__", ("Hyperion",), "OpcodeLookupTable", "0x71433e0"),
    ("__LUAU_EXECUTE__", ("Hyperion",), "Luau_Execute", "0x265f2b0"),
    ("__PUSH__", ("Hyperion",), "Push", "0x4193580"),
    ("__FIRE_LEFT__", ("Hyperion",), "FireLeftMouseClick", "0x3bd1060"),
    ("__FIRE_RIGHT__", ("Hyperion",), "FireRightMouseClick", "0x3bd1200"),
    ("__HOVER_ENTER__", ("Hyperion",), "FireMouseHoverEnter", "0x3bd2650"),
    ("__HOVER_LEAVE__", ("Hyperion",), "FireMouseHoverLeave", "0x3bd27f0"),
    ("__IDENTITY__", ("Hyperion",), "Identity", "0x854f778"),
    ("__GET_IDENTITY__", ("Hyperion",), "GetIdentityStruct", "0x6bb0"),
    ("__FLOG_DATABANK__", ("Hyperion",), "FLogDataBank", "0x8C885C8"),
    ("__FIRE_PROMPT__", ("Hyperion",), "FireProximityPrompt", "0x30d1720"),
    ("__FIRE_TOUCH__", ("Hyperion",), "FireTouchInterest", "0x1521d60"),
    ("__SIGNAL_CASTARGS__", ("Hyperion",), "CastArgs", "0x4102410"),
    ("__SIGNAL_DISCONNECT__", ("Hyperion",), "DisconnectConnect", "0x416B600"),
    ("__GETCAPABILITIES__", ("Hyperion",), "GetCapabilities", "0x1d241c0"),
    ("__SET_FFLAG__", ("Hyperion",), "SetFFlag", "0x49F8270"),
    ("__TASKSCHEDULER_PTR__", ("TaskScheduler",), "Pointer", "0x8d71348"),
    ("__TASKSCHEDULER_JOBSTART__", ("TaskScheduler",), "JobStart", "0xC8"),
    ("__TASKSCHEDULER_JOBNAME__", ("TaskScheduler",), "JobName", "0x18"),
    ("__VISUALENGINE_PTR__", ("VisualEngine",), "Pointer", "0x884c2e0"),
    ("__VE_TO_RENDERVIEW__", ("VisualEngine",), "RenderView", "0xc30"),
    ("__RENDERJOB_TO_VIEW__", ("RenderJob",), "RenderView", "0x1E0"),
    ("__VIEW_TO_DEVICE__", ("RenderView",), "DeviceD3D11", "0x8"),
    ("__DEVICE_TO_SWAPCHAIN__", ("DeviceD3D11",), "SwapChainPtr", "0x80"),
)


_INTERNAL_TEMPLATE = """#pragma once

#include <lua.h>
#include <Windows.h>
#include <cstddef>
#include <cstdint>
#include <memory>
#include <string>


#define Rebase(Address) ((Address) == 0 ? uintptr_t{0} : ((Address) + reinterpret_cast<uintptr_t>(GetModuleHandleA(nullptr))))


struct lua_State;
struct YieldState;
struct YieldingLuaThread;


namespace Offsets
{


    const uintptr_t Print = Rebase(__PRINT__);
    const uintptr_t OpcodeLookupTable = Rebase(__OPCODE_TABLE__);


    namespace Luau
    {
        const uintptr_t LuaO_NilObject = Rebase(__LUAO_NILOBJECT__);
        const uintptr_t LuaH_DummyNode = Rebase(__LUAH_DUMMYNODE__);
        const uintptr_t LuaD_Throw = Rebase(__LUAD_THROW__);
        const uintptr_t LuaC_Step = Rebase(__LUAC_STEP__);
        const uintptr_t Luau_Execute = Rebase(__LUAU_EXECUTE__);
        const uintptr_t LuaVM_Load = Rebase(__LUAVM_LOAD__);
    }


    namespace DataModel
    {
        const uintptr_t Primitive = 0x180;
        const uintptr_t Overlap = 0x200;


        const uintptr_t ScriptContext = __DM_SCRIPTCONTEXT__;
        const uintptr_t Children = __DM_CHILDREN__;
        const uintptr_t ClassDescriptor = __DM_CLASSDESCRIPTOR__;


        const uintptr_t FakeDataModelToDataModel = __FDM_TO_DM__;
        const uintptr_t FakeDataModelPointer = Rebase(__FDM_POINTER__);
    }


    namespace Instance
    {
        static constexpr uintptr_t name = __INSTANCE_NAME__;
        static constexpr uintptr_t name_str = __INSTANCE_NAME_STR__;
    }


    namespace ExtraSpace
    {
        const uintptr_t ScriptContextResume = Rebase(__SCRIPTCONTEXT_RESUME__);
        const uintptr_t ScriptContextToResume = 0x908;
    }


    namespace Identity
    {
        const uintptr_t Identity = Rebase(__IDENTITY__);
        const uintptr_t GetIdentityStruct = Rebase(__GET_IDENTITY__);
    }


    namespace Capabilities
    {
        const uintptr_t GetCapabilities = Rebase(__GETCAPABILITIES__);
        const uintptr_t Capabilities = 0x30;
    }


    namespace Scripts
    {
        const uintptr_t LocalScriptByteCode = 0x180;
        const uintptr_t ModuleScriptByteCode = __MODULESCRIPT_BYTECODE__;
        const uintptr_t BytecodeStringOffset = 0x18;
        const uintptr_t ServerContextFlag = 0x130;


        const uintptr_t Pointer = __BYTECODE_POINTER__;
        const uintptr_t Size = __BYTECODE_SIZE__;
    }


    namespace InstanceBridge
    {
        const uintptr_t Push = Rebase(__PUSH__);
    }


    namespace Reflection
    {
        const uintptr_t KTable = Rebase(__KTABLE__);
        const uintptr_t GetProperty = Rebase(__REFLECTION_GETPROPERTY__);


        constexpr uintptr_t InstanceSelf = 0x8;
        constexpr uintptr_t ClassDescriptor = 0x18;
        constexpr uintptr_t PropertyMap = 0x1D8;
        constexpr uintptr_t MapIndices = 0x8, MapEntries = 0x10, MapMask = 0x18, MapEntrySize = 0x10;
        constexpr uintptr_t EntryKind = 0x8;


        constexpr uintptr_t TypeInfo = 0x70;
        constexpr uintptr_t TypeNum = 0x30;
        constexpr uintptr_t Flags = 0x94;
        constexpr std::uint32_t FlagScriptable = 0x10;
        constexpr uintptr_t GetSet = 0x98;
        constexpr uintptr_t GetterSlot = 0x18, SetterSlot = 0x20;


        constexpr uintptr_t SharedStringCanary = 0x00;
        constexpr std::uint32_t SharedStringCanaryValue = 0xF1F1F1F1u;
        constexpr uintptr_t SharedStringPayload = 0x18;
        constexpr uintptr_t SharedStringRefcount = 0x40;
    }


    namespace TaskScheduler
    {
        const uintptr_t TaskSchedulerPtr = Rebase(__TASKSCHEDULER_PTR__);
        const uintptr_t JobStart = __TASKSCHEDULER_JOBSTART__;
        const uintptr_t JobName = __TASKSCHEDULER_JOBNAME__;
    }


    namespace Renderer
    {
        const uintptr_t VisualEngine = Rebase(__VISUALENGINE_PTR__);
        const uintptr_t VisualEngineToRenderView = __VE_TO_RENDERVIEW__;
    }


    namespace RenderView
    {
        const uintptr_t RenderJobToView = __RENDERJOB_TO_VIEW__;
        const uintptr_t ViewToDevice = __VIEW_TO_DEVICE__;
        const uintptr_t DeviceToSwapChain = __DEVICE_TO_SWAPCHAIN__;
    }


    namespace ScriptContext
    {
        const uintptr_t RequireBypass = 0xA81;
    }


    namespace Touch {
        const uintptr_t FireLeftMouseClick = Rebase(__FIRE_LEFT__);
        const uintptr_t FireRightMouseClick = Rebase(__FIRE_RIGHT__);
        const uintptr_t FireMouseHoverEnter = Rebase(__HOVER_ENTER__);
        const uintptr_t FireMouseHoverLeave = Rebase(__HOVER_LEAVE__);
        const uintptr_t FireProximityPrompt = Rebase(__FIRE_PROMPT__);
        const uintptr_t FireTouchInterest = Rebase(__FIRE_TOUCH__);
    }


    namespace Signal {
        const uintptr_t CastArgs = Rebase(__SIGNAL_CASTARGS__);
        const uintptr_t DisconnectConnect = Rebase(__SIGNAL_DISCONNECT__);
        const uintptr_t EventArguments = 0x50;
        const uintptr_t EventArgumentSize = 0x70;
        const uintptr_t EventArgumentType = 0x8;
    }


    inline const uintptr_t GetFFlag = Rebase(0x49F8D70);
    inline const uintptr_t FLogDataBank = Rebase(__FLOG_DATABANK__);
    inline const uintptr_t SetFFlag = Rebase(__SET_FFLAG__);


}


namespace Hyperion
{
    inline auto Print = (uintptr_t(*)(int, const char*, ...))Offsets::Print;
    inline const auto GetFFlag = reinterpret_cast<int(__fastcall*)(uintptr_t, std::string*, std::string*, bool)>(Offsets::GetFFlag);
    inline const auto SetFFlag = reinterpret_cast<int(__fastcall*)(uintptr_t, std::string*, std::string*, int, int, int)>(Offsets::SetFFlag);


    inline auto CastArgs = reinterpret_cast<uintptr_t(__fastcall*)(lua_State*, int, void*, bool, int)>(Offsets::Signal::CastArgs);
    inline auto DisconnectConnection = (void(__fastcall*)(uintptr_t*))Offsets::Signal::DisconnectConnect;


    using fireclick_t = void(__fastcall*)(void* clickDetector, float distance, void* player);
    inline auto FireMouseClick = reinterpret_cast<fireclick_t>(Offsets::Touch::FireLeftMouseClick);
    inline auto FireRightMouseClick = reinterpret_cast<fireclick_t>(Offsets::Touch::FireRightMouseClick);


    using firehover_t = void(__fastcall*)(void* clickDetector, void* player);
    inline auto FireMouseHover = reinterpret_cast<firehover_t>(Offsets::Touch::FireMouseHoverEnter);
    inline auto FireMouseHoverLeave = reinterpret_cast<firehover_t>(Offsets::Touch::FireMouseHoverLeave);


    inline auto FireProximityPrompt = (void(__thiscall*)(uintptr_t))Offsets::Touch::FireProximityPrompt;
    inline auto FireTouchInterest = (void(__fastcall*)(uintptr_t, uintptr_t, uintptr_t, bool, bool))Offsets::Touch::FireTouchInterest;


    inline auto LuaVM_Load = (int(__fastcall*)(lua_State * thread, void* bytecode, const char* chunkName, int env))Offsets::Luau::LuaVM_Load;
    inline auto Luau_Execute = (void(__fastcall*)(lua_State*))Offsets::Luau::Luau_Execute;


    inline auto ScriptContextResume = (uint64_t(__fastcall*)(uint64_t, YieldState*, YieldingLuaThread**, uint32_t, uint8_t, uint64_t))Offsets::ExtraSpace::ScriptContextResume;
    inline auto LuaD_Throw = (void(__fastcall*)(lua_State*, int))Offsets::Luau::LuaD_Throw;
    inline auto GetIdentityStruct = (uintptr_t(__fastcall*)(uintptr_t))Offsets::Identity::GetIdentityStruct;


    inline auto GetCapabilities = (__int64(__fastcall*)(int*))Offsets::Capabilities::GetCapabilities;


    namespace InstanceBridge
    {
        inline auto UintPtr = (void(__fastcall*)(lua_State*, std::uintptr_t))Offsets::InstanceBridge::Push;
        inline auto Shared = (void(__fastcall*)(lua_State*, std::shared_ptr<std::uintptr_t*>))Offsets::InstanceBridge::Push;
        inline auto Void = (void(__fastcall*)(lua_State*, void**))Offsets::InstanceBridge::Push;
        inline auto Void2 = (void(__fastcall*)(lua_State*, void*))Offsets::InstanceBridge::Push;
        inline auto Weak = (void(__fastcall*)(lua_State*, std::weak_ptr<std::uintptr_t>))Offsets::InstanceBridge::Push;
    }
}
"""


_ENCS_CONTENT = """#pragma once


#include <Windows.h>


template<typename T>
struct vmval1
{
private:
    T Storage;


public:
    operator const T() const
    {
        return (T)((uintptr_t)Storage - (uintptr_t)this);
    }


    void operator=(const T& Value)
    {
        Storage = (T)((uintptr_t)Value + (uintptr_t)this);
    }


    const T operator->() const
    {
        return operator const T();
    }


    T Get() const
    {
        return operator const T();
    }


    void Set(const T& Value)
    {
        operator=(Value);
    }
};


template<typename T>
struct vmval2
{
private:
    T Storage;


public:
    operator const T() const
    {
        return (T)((uintptr_t)this - (uintptr_t)Storage);
    }


    void operator=(const T& Value)
    {
        Storage = (T)((uintptr_t)this - (uintptr_t)Value);
    }


    const T operator->() const
    {
        return operator const T();
    }


    T Get() const
    {
        return operator const T();
    }


    void Set(const T& Value)
    {
        operator=(Value);
    }
};


template<typename T>
struct vmval3
{
private:
    T Storage;


public:
    operator const T() const
    {
        return (T)((uintptr_t)this ^ (uintptr_t)Storage);
    }


    void operator=(const T& Value)
    {
        Storage = (T)((uintptr_t)Value ^ (uintptr_t)this);
    }


    const T operator->() const
    {
        return operator const T();
    }


    T Get() const
    {
        return operator const T();
    }


    void Set(const T& Value)
    {
        operator=(Value);
    }
};


template<typename T>
struct vmval4
{
private:
    T Storage;


public:
    operator const T() const
    {
        return (T)((uintptr_t)this + (uintptr_t)Storage);
    }


    void operator=(const T& Value)
    {
        Storage = (T)((uintptr_t)Value - (uintptr_t)this);
    }


    const T operator->() const
    {
        return operator const T();
    }


    T Get() const
    {
        return operator const T();
    }


    void Set(const T& Value)
    {
        operator=(Value);
    }
};


#define CLOSURE_CONT_ENC vmval4
#define LSTATE_STACKSIZE_ENC vmval3
#define PROTO_ABSLINEINFO_ENC vmval4
#define PROTO_DEBUGINSN_ENC vmval3
#define PROTO_DEBUGNAME_ENC vmval3
#define PROTO_LINEINFO_ENC vmval3
#define PROTO_LOCVARS_ENC vmval3
#define PROTO_SOURCE_ENC vmval1
#define PROTO_TYPEINFO_ENC vmval3
#define PROTO_UPVALUES_ENC vmval2
#define PROTO_USERDATA_ENC vmval2
#define TSTRING_HASH_ENC vmval1
#define UDATA_META_ENC vmval1
"""


def _resolve(local_map, namespace, field, fallback):
    if namespace is not None:
        value = local_map.get(namespace, {}).get(field)
        if value is not None:
            return "0x%x" % value
    return fallback


def render_internal_offsets(version, local_map):
    text = _INTERNAL_TEMPLATE
    for marker, namespace, field, fallback in _INTERNAL_MAP:
        text = text.replace(marker, _resolve(local_map, namespace, field, fallback))
    return text


def render_encs():
    return _ENCS_CONTENT
