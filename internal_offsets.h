#pragma once

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


    const uintptr_t Print = Rebase(0x1d071a0);
    const uintptr_t OpcodeLookupTable = Rebase(0x663e800);


    namespace Luau
    {
        const uintptr_t LuaO_NilObject = Rebase(0x67bb388);
        const uintptr_t LuaH_DummyNode = Rebase(0x67bae28);
        const uintptr_t LuaD_Throw = Rebase(0x2691f10);
        const uintptr_t LuaC_Step = Rebase(0x26b0b80);
        const uintptr_t Luau_Execute = Rebase(0x26bcfd0);
        const uintptr_t LuaVM_Load = Rebase(0x9b3490);
    }


    namespace DataModel
    {
        const uintptr_t Primitive = 0x180;
        const uintptr_t Overlap = 0x200;


        const uintptr_t ScriptContext = 0x440;
        const uintptr_t Children = 0x70;
        const uintptr_t ClassDescriptor = 0x18;


        const uintptr_t FakeDataModelToDataModel = 0x1f8;
        const uintptr_t FakeDataModelPointer = Rebase(0x8f59810);
    }


    namespace Instance
    {
        static constexpr uintptr_t name = 0x68;
        static constexpr uintptr_t name_str = 0x0;
    }


    namespace ExtraSpace
    {
        const uintptr_t ScriptContextResume = Rebase(0x43004b0);
        const uintptr_t ScriptContextToResume = 0x908;
    }


    namespace Identity
    {
        const uintptr_t Identity = Rebase(0x86d8748);
        const uintptr_t GetIdentityStruct = Rebase(0x6bb0);
    }


    namespace Capabilities
    {
        const uintptr_t GetCapabilities = Rebase(0x1d45e30);
        const uintptr_t Capabilities = 0x30;
    }


    namespace Scripts
    {
        const uintptr_t LocalScriptByteCode = 0x180;
        const uintptr_t ModuleScriptByteCode = 0x138;
        const uintptr_t BytecodeStringOffset = 0x18;
        const uintptr_t ServerContextFlag = 0x130;


        const uintptr_t Pointer = 0x10;
        const uintptr_t Size = 0x28;
    }


    namespace InstanceBridge
    {
        const uintptr_t Push = Rebase(0x4246e90);
    }


    namespace Reflection
    {
        const uintptr_t KTable = Rebase(0x85ead60);
        const uintptr_t GetProperty = Rebase(0x1d44010);


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
        const uintptr_t TaskSchedulerPtr = Rebase(0x8f026a8);
        const uintptr_t JobStart = 0xc8;
        const uintptr_t JobName = 0x18;
    }


    namespace Renderer
    {
        const uintptr_t VisualEngine = Rebase(0x89dc1a0);
        const uintptr_t VisualEngineToRenderView = 0xc40;
    }


    namespace RenderView
    {
        const uintptr_t RenderJobToView = 0x1e0;
        const uintptr_t ViewToDevice = 0x8;
        const uintptr_t DeviceToSwapChain = 0x80;
    }


    namespace ScriptContext
    {
        const uintptr_t RequireBypass = 0xA81;
    }


    namespace Touch {
        const uintptr_t FireLeftMouseClick = Rebase(0x5ad4470);
        const uintptr_t FireRightMouseClick = Rebase(0x5ad4610);
        const uintptr_t FireMouseHoverEnter = Rebase(0x5ad2e90);
        const uintptr_t FireMouseHoverLeave = Rebase(0x5ad3040);
        const uintptr_t FireProximityPrompt = Rebase(0x311f590);
        const uintptr_t FireTouchInterest = Rebase(0x2ae8c20);
    }


    namespace Signal {
        const uintptr_t CastArgs = Rebase(0x770f10);
        const uintptr_t DisconnectConnect = Rebase(0x42299a0);
        const uintptr_t EventArguments = 0x50;
        const uintptr_t EventArgumentSize = 0x70;
        const uintptr_t EventArgumentType = 0x8;
    }


    inline const uintptr_t GetFFlag = Rebase(0x49F8D70);
    inline const uintptr_t FLogDataBank = Rebase(0x8e1b0d0);
    inline const uintptr_t SetFFlag = Rebase(0x21c09d0);


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
