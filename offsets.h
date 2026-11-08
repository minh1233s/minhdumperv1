#pragma once
/* 8====================================================D
/*            minh dumper (by minhlo123df)
/* 8====================================================D
/*  Dumped With     : minh dumper (by minhlo123df)
/*  Roblox Version  : version-5a21b87bbc2641cf
/*  Time Taken      : 146681 ms
/*  Total Offsets   : 532
/* 8====================================================D
*/

#include <cstdint>
#include <string>

namespace Offsets {
    inline std::string ClientVersion = "version-5a21b87bbc2641cf";

    namespace AirProperties {
         inline constexpr uintptr_t AirDensity = 0x18;
         inline constexpr uintptr_t GlobalWind = 0x3c;
    }

    namespace AnimationTrack {
         inline constexpr uintptr_t Animation    = 0xa0;
         inline constexpr uintptr_t Animator     = 0xf8;
         inline constexpr uintptr_t Looped       = 0xa0c;
         inline constexpr uintptr_t Speed        = 0xbc;
         inline constexpr uintptr_t TimePosition = 0xc0;
    }

    namespace Animator {
         inline constexpr uintptr_t ActiveAnimations = 0x900;
    }

    namespace Atmosphere {
         inline constexpr uintptr_t Color   = 0xa0;
         inline constexpr uintptr_t Decay   = 0xac;
         inline constexpr uintptr_t Density = 0xb8;
         inline constexpr uintptr_t Glare   = 0xbc;
         inline constexpr uintptr_t Haze    = 0xc0;
         inline constexpr uintptr_t Offset  = 0xc4;
    }

    namespace Attachment {
         inline constexpr uintptr_t Position = 0xac;
    }

    namespace Attribute {
         inline constexpr uintptr_t Key          = 0x0;
         inline constexpr uintptr_t Size         = 0x58;
         inline constexpr uintptr_t TypeIdRva    = 0x8e446f4;
         inline constexpr uintptr_t TypeIdRvaNew = 0x8e446fc;
         inline constexpr uintptr_t Value        = 0x8;
    }

    namespace AttributesMap {
         inline constexpr uintptr_t Attributes = 0x10;
         inline constexpr uintptr_t Length     = 0x0;
    }

    namespace BasePart {
         inline constexpr uintptr_t CastShadow   = 0x120;
         inline constexpr uintptr_t ClusterNode  = 0xe0;
         inline constexpr uintptr_t Color3       = 0x11c;
         inline constexpr uintptr_t Locked       = 0x121;
         inline constexpr uintptr_t Massless     = 0x122;
         inline constexpr uintptr_t Primitive    = 0x178;
         inline constexpr uintptr_t Reflectance  = 0xf4;
         inline constexpr uintptr_t Shape        = 0x1a0;
         inline constexpr uintptr_t Transparency = 0x118;
    }

    namespace Beam {
         inline constexpr uintptr_t Attachment0    = 0x148;
         inline constexpr uintptr_t Attachment1    = 0x158;
         inline constexpr uintptr_t Brightness     = 0x168;
         inline constexpr uintptr_t CurveSize0     = 0x16c;
         inline constexpr uintptr_t CurveSize1     = 0x170;
         inline constexpr uintptr_t LightEmission  = 0x174;
         inline constexpr uintptr_t LightInfluence = 0x178;
         inline constexpr uintptr_t Segments       = 0x180;
         inline constexpr uintptr_t Texture        = 0x128;
         inline constexpr uintptr_t TextureLength  = 0x184;
         inline constexpr uintptr_t TextureSpeed   = 0x18c;
         inline constexpr uintptr_t Width0         = 0x190;
         inline constexpr uintptr_t Width1         = 0x194;
         inline constexpr uintptr_t ZOffset        = 0x198;
    }

    namespace BloomEffect {
         inline constexpr uintptr_t Enabled   = 0x98;
         inline constexpr uintptr_t Intensity = 0xa0;
         inline constexpr uintptr_t Size      = 0xa4;
         inline constexpr uintptr_t Threshold = 0xa8;
    }

    namespace BlurEffect {
         inline constexpr uintptr_t Enabled = 0x98;
         inline constexpr uintptr_t Size    = 0xa0;
    }

    namespace BoxHandleAdornment {
         inline constexpr uintptr_t Adornee = 0xd8;
         inline constexpr uintptr_t Color3  = 0xc0;
         inline constexpr uintptr_t Size    = 0x190;
    }

    namespace ByteCode {
         inline constexpr uintptr_t Pointer = 0x10;
         inline constexpr uintptr_t Size    = 0x28;
    }

    namespace CachedItem {
         inline constexpr uintptr_t FileMeshData = 0x28;
    }

    namespace Camera {
         inline constexpr uintptr_t CameraSubject   = 0xb0;
         inline constexpr uintptr_t CameraType      = 0x120;
         inline constexpr uintptr_t FieldOfView     = 0x128;
         inline constexpr uintptr_t ImagePlaneDepth = 0x2cc;
         inline constexpr uintptr_t Position        = 0xec;
         inline constexpr uintptr_t Rotation        = 0xc8;
         inline constexpr uintptr_t Viewport        = 0x27c;
         inline constexpr uintptr_t ViewportSize    = 0x2bc;
    }

    namespace CharacterMesh {
         inline constexpr uintptr_t BaseTextureId    = 0xb0;
         inline constexpr uintptr_t BodyPart         = 0x130;
         inline constexpr uintptr_t MeshId           = 0xe0;
         inline constexpr uintptr_t OverlayTextureId = 0x110;
    }

    namespace ClickDetector {
         inline constexpr uintptr_t MaxActivationDistance = 0xd0;
         inline constexpr uintptr_t MouseIcon             = 0xb0;
    }

    namespace Clothing {
         inline constexpr uintptr_t Color3   = 0x108;
         inline constexpr uintptr_t Template = 0xe8;
    }

    namespace ColorCorrectionEffect {
         inline constexpr uintptr_t Brightness = 0xac;
         inline constexpr uintptr_t Contrast   = 0xb0;
         inline constexpr uintptr_t Enabled    = 0x98;
         inline constexpr uintptr_t TintColor  = 0xa0;
    }

    namespace ColorGradingEffect {
         inline constexpr uintptr_t Enabled          = 0x98;
         inline constexpr uintptr_t TonemapperPreset = 0xa0;
    }

    namespace DataModel {
         inline constexpr uintptr_t Camera         = 0x4a0;
         inline constexpr uintptr_t CreatorId      = 0x170;
         inline constexpr uintptr_t GameId         = 0x178;
         inline constexpr uintptr_t GameLoaded     = 0x5c8;
         inline constexpr uintptr_t JobId          = 0x108;
         inline constexpr uintptr_t PlaceId        = 0x180;
         inline constexpr uintptr_t PlaceVersion   = 0x1a4;
         inline constexpr uintptr_t PrimitiveCount = 0x418;
         inline constexpr uintptr_t ScriptContext  = 0x440;
         inline constexpr uintptr_t ServerIP       = 0x5b0;
         inline constexpr uintptr_t ToRenderView1  = 0x1b8;
         inline constexpr uintptr_t ToRenderView2  = 0x8;
         inline constexpr uintptr_t ToRenderView3  = 0x28;
         inline constexpr uintptr_t Workspace      = 0x148;
    }

    namespace DepthOfFieldEffect {
         inline constexpr uintptr_t Enabled       = 0x98;
         inline constexpr uintptr_t FarIntensity  = 0xa0;
         inline constexpr uintptr_t FocusDistance = 0xa4;
         inline constexpr uintptr_t InFocusRadius = 0xa8;
         inline constexpr uintptr_t NearIntensity = 0xac;
    }

    namespace DeviceD3D11 {
         inline constexpr uintptr_t Context      = 0x180;
         inline constexpr uintptr_t ContextObj   = 0x1b0;
         inline constexpr uintptr_t ContextPtr   = 0x180;
         inline constexpr uintptr_t DevicePtr    = 0x228;
         inline constexpr uintptr_t SwapChainPtr = 0x80;
         inline constexpr uintptr_t VTableRva    = 0x6ffa390;
    }

    namespace DragDetector {
         inline constexpr uintptr_t ActivatedCursorIcon       = 0x1a8;
         inline constexpr uintptr_t CursorIcon                = 0xb0;
         inline constexpr uintptr_t GamepadModeSwitchKeyCode  = 0x288;
         inline constexpr uintptr_t KeyboardModeSwitchKeyCode = 0x28c;
         inline constexpr uintptr_t MaxActivationDistance     = 0xd0;
         inline constexpr uintptr_t MaxDragAngle              = 0x290;
         inline constexpr uintptr_t MaxDragTranslation        = 0x254;
         inline constexpr uintptr_t MaxForce                  = 0x294;
         inline constexpr uintptr_t MaxTorque                 = 0x298;
         inline constexpr uintptr_t MinDragAngle              = 0x29c;
         inline constexpr uintptr_t MinDragTranslation        = 0x260;
         inline constexpr uintptr_t ReferenceInstance         = 0x1d8;
         inline constexpr uintptr_t Responsiveness            = 0x2a8;
         inline constexpr uintptr_t VRSwitchKeyCode           = 0x2b4;
    }

    namespace FakeDataModel {
         inline constexpr uintptr_t Pointer       = 0x8f59810;
         inline constexpr uintptr_t RealDataModel = 0x1f8;
    }

    namespace FastCluster {
         inline constexpr uintptr_t VTableRva    = 0x7066268;
         inline constexpr uintptr_t VTableRvaSub = 0x7066130;
    }

    namespace FastClusterBinding {
         inline constexpr uintptr_t Owner     = 0x60;
         inline constexpr uintptr_t VTableRva = 0x7067390;
    }

    namespace FastClusterEntity {
         inline constexpr uintptr_t AlphaByte              = 0x14;
         inline constexpr uintptr_t BBoxMaxX               = 0xa4;
         inline constexpr uintptr_t BBoxMaxY               = 0xa8;
         inline constexpr uintptr_t BBoxMaxZ               = 0xac;
         inline constexpr uintptr_t BBoxMinX               = 0x98;
         inline constexpr uintptr_t BBoxMinY               = 0x9c;
         inline constexpr uintptr_t BBoxMinZ               = 0xa0;
         inline constexpr uintptr_t ContextPtr             = 0x8;
         inline constexpr uintptr_t DecalMaterialPtr       = 0x48;
         inline constexpr uintptr_t MaterialPtr            = 0x20;
         inline constexpr uintptr_t PrimitiveIndexArrayPtr = 0x80;
         inline constexpr uintptr_t RenderQueueId          = 0x10;
         inline constexpr uintptr_t TechniqueArrayPtr      = 0x70;
         inline constexpr uintptr_t VTableRva              = 0x7067468;
    }

    namespace FFlag {
         inline constexpr uintptr_t RenderFastClusterOcclusionCulling = 0x862bc90;
    }

    namespace FileMeshData {
         inline constexpr uintptr_t AABBMax = 0x18c;
         inline constexpr uintptr_t AABBMin = 0x180;
    }

    namespace GeometryD3D11 {
         inline constexpr uintptr_t VTableRva = 0x6ffaa80;
    }

    namespace GuiBase2D {
         inline constexpr uintptr_t AbsoluteRotation = 0xd0;
    }

    namespace GuiObject {
         inline constexpr uintptr_t BackgroundColor3       = 0x528;
         inline constexpr uintptr_t BackgroundTransparency = 0x534;
         inline constexpr uintptr_t BorderColor3           = 0x534;
         inline constexpr uintptr_t Image                  = 0x9d8;
         inline constexpr uintptr_t LayoutOrder            = 0x564;
         inline constexpr uintptr_t PlaceholderColor3      = 0xf00;
         inline constexpr uintptr_t Position               = 0x500;
         inline constexpr uintptr_t RichText               = 0xbd0;
         inline constexpr uintptr_t Rotation               = 0xd0;
         inline constexpr uintptr_t ScreenGui_Enabled      = 0x308;
         inline constexpr uintptr_t Size                   = 0x520;
         inline constexpr uintptr_t Text                   = 0xbd0;
         inline constexpr uintptr_t TextColor3             = 0xee8;
         inline constexpr uintptr_t Visible                = 0x595;
         inline constexpr uintptr_t ZIndex                 = 0x58c;
    }

    namespace Humanoid {
         inline constexpr uintptr_t AutoJumpEnabled         = 0x1c8;
         inline constexpr uintptr_t AutomaticScalingEnabled = 0x1ca;
         inline constexpr uintptr_t AutoRotate              = 0x1c5;
         inline constexpr uintptr_t BreakJointsOnDeath      = 0x1cb;
         inline constexpr uintptr_t CameraOffset            = 0x118;
         inline constexpr uintptr_t DisplayDistanceType     = 0x174;
         inline constexpr uintptr_t DisplayName             = 0xa0;
         inline constexpr uintptr_t EvaluateStateMachine    = 0x1cc;
         inline constexpr uintptr_t FloorMaterial           = 0x174;
         inline constexpr uintptr_t Health                  = 0x184;
         inline constexpr uintptr_t HealthDisplayDistance   = 0x17c;
         inline constexpr uintptr_t HealthDisplayType       = 0x180;
         inline constexpr uintptr_t HipHeight               = 0x188;
         inline constexpr uintptr_t HumanoidRootPart        = 0x460;
         inline constexpr uintptr_t HumanoidState           = 0x8a0;
         inline constexpr uintptr_t HumanoidStateID         = 0x20;
         inline constexpr uintptr_t IsWalking               = 0xa1f;
         inline constexpr uintptr_t Jump                    = 0x174;
         inline constexpr uintptr_t JumpHeight              = 0x194;
         inline constexpr uintptr_t JumpPower               = 0x198;
         inline constexpr uintptr_t MaxHealth               = 0x19c;
         inline constexpr uintptr_t MaxSlopeAngle           = 0x1a0;
         inline constexpr uintptr_t MoveDirection           = 0x130;
         inline constexpr uintptr_t MoveToPart              = 0x108;
         inline constexpr uintptr_t MoveToPoint             = 0x154;
         inline constexpr uintptr_t NameDisplayDistance     = 0x1a4;
         inline constexpr uintptr_t NameOcclusion           = 0x1a8;
         inline constexpr uintptr_t PlatformStand           = 0x1a8;
         inline constexpr uintptr_t RequiresNeck            = 0x1d2;
         inline constexpr uintptr_t RigType                 = 0x1b4;
         inline constexpr uintptr_t SeatPart                = 0xf0;
         inline constexpr uintptr_t Sit                     = 0x1d2;
         inline constexpr uintptr_t TargetPoint             = 0x13c;
         inline constexpr uintptr_t UseJumpPower            = 0x1d5;
         inline constexpr uintptr_t Walkspeed               = 0x1c4;
         inline constexpr uintptr_t WalkspeedCheck          = 0x39c;
         inline constexpr uintptr_t WalkTimer               = 0x0;
    }

    namespace Hyperion {
         inline constexpr uintptr_t CastArgs            = 0x770f10;
         inline constexpr uintptr_t DisconnectConnect   = 0x42299a0;
         inline constexpr uintptr_t FireLeftMouseClick  = 0x5ad4470;
         inline constexpr uintptr_t FireMouseHoverEnter = 0x5ad2e90;
         inline constexpr uintptr_t FireMouseHoverLeave = 0x5ad3040;
         inline constexpr uintptr_t FireProximityPrompt = 0x311f590;
         inline constexpr uintptr_t FireRightMouseClick = 0x5ad4610;
         inline constexpr uintptr_t FireTouchInterest   = 0x2ae8c20;
         inline constexpr uintptr_t FLogDataBank        = 0x8e1b0d0;
         inline constexpr uintptr_t GetCapabilities     = 0x1d45e30;
         inline constexpr uintptr_t GetFFlag            = 0x89f0;
         inline constexpr uintptr_t GetIdentityStruct   = 0x6bb0;
         inline constexpr uintptr_t GetProperty         = 0x1d44010;
         inline constexpr uintptr_t HashLookup          = 0x5a88390;
         inline constexpr uintptr_t Identity            = 0x86d8748;
         inline constexpr uintptr_t KTable              = 0x85ead60;
         inline constexpr uintptr_t LuaC_Step           = 0x26b0b80;
         inline constexpr uintptr_t LuaO_NilObject      = 0x67bb388;
         inline constexpr uintptr_t Luau_Execute        = 0x26bcfd0;
         inline constexpr uintptr_t OpcodeLookupTable   = 0x663e800;
         inline constexpr uintptr_t PrintIdentity       = 0x4253000;
         inline constexpr uintptr_t Push                = 0x4246e90;
         inline constexpr uintptr_t SendRaw             = 0x28a2df0;
         inline constexpr uintptr_t SendShared          = 0x28a32e0;
         inline constexpr uintptr_t SendStream          = 0x28a3090;
         inline constexpr uintptr_t SetFFlag            = 0x21c09d0;
    }

    namespace Instance {
         inline constexpr uintptr_t AttributeContainer = 0x40;
         inline constexpr uintptr_t AttributeList      = 0x10;
         inline constexpr uintptr_t AttributeToNext    = 0x58;
         inline constexpr uintptr_t AttributeToValue   = 0x18;
         inline constexpr uintptr_t ChildrenEnd        = 0x8;
         inline constexpr uintptr_t ChildrenStart      = 0x70;
         inline constexpr uintptr_t ClassBase          = 0x1b0;
         inline constexpr uintptr_t ClassDescriptor    = 0x18;
         inline constexpr uintptr_t ClassName          = 0x8;
         inline constexpr uintptr_t Name               = 0x0;
         inline constexpr uintptr_t NameContainer      = 0x68;
         inline constexpr uintptr_t Parent             = 0x60;
         inline constexpr uintptr_t This               = 0x8;
    }

    namespace Lighting {
         inline constexpr uintptr_t Ambient                  = 0xb8;
         inline constexpr uintptr_t Brightness               = 0x100;
         inline constexpr uintptr_t ClockTime                = 0xb0;
         inline constexpr uintptr_t ColorShift_Bottom        = 0xd0;
         inline constexpr uintptr_t ColorShift_Top           = 0xc4;
         inline constexpr uintptr_t EnvironmentDiffuseScale  = 0x104;
         inline constexpr uintptr_t EnvironmentSpecularScale = 0x108;
         inline constexpr uintptr_t ExposureCompensation     = 0x10c;
         inline constexpr uintptr_t FogColor                 = 0xdc;
         inline constexpr uintptr_t FogEnd                   = 0x114;
         inline constexpr uintptr_t FogStart                 = 0x118;
         inline constexpr uintptr_t GeographicLatitude       = 0x11c;
         inline constexpr uintptr_t GlobalShadows            = 0x12c;
         inline constexpr uintptr_t GradientBottom           = 0x178;
         inline constexpr uintptr_t GradientTop              = 0x138;
         inline constexpr uintptr_t LightColor               = 0x144;
         inline constexpr uintptr_t LightDirection           = 0x150;
         inline constexpr uintptr_t MoonPosition             = 0x16c;
         inline constexpr uintptr_t OutdoorAmbient           = 0xe8;
         inline constexpr uintptr_t Sky                      = 0x1b0;
    }

    namespace LocalScript {
         inline constexpr uintptr_t GUID = 0xc0;
         inline constexpr uintptr_t Hash = 0x188;
    }

    namespace LRUHolder {
         inline constexpr uintptr_t MemEnforcedLRUCache = 0x20;
    }

    namespace LRUNode {
         inline constexpr uintptr_t AssetID    = 0x10;
         inline constexpr uintptr_t CachedItem = 0x38;
         inline constexpr uintptr_t Next       = 0x0;
    }

    namespace Luau {
         inline constexpr uintptr_t dumpgco          = 0x26ba1b0;
         inline constexpr uintptr_t lua_checkstack   = 0x422409d;
         inline constexpr uintptr_t lua_newstate     = 0x4222fb0;
         inline constexpr uintptr_t luaD_Throw       = 0x2691f10;
         inline constexpr uintptr_t luaF_freeproto   = 0x26b81a0;
         inline constexpr uintptr_t luaH_dummynode   = 0x67bae28;
         inline constexpr uintptr_t luaL_loadsafe    = 0x26f458c;
         inline constexpr uintptr_t luaO_pushfstring = 0x268d830;
         inline constexpr uintptr_t LuaVMLoad        = 0x9b3490;
         inline constexpr uintptr_t PushInstance     = 0x49e2be0;
         namespace global_State {
              inline constexpr uintptr_t g_gcstepmul = 0x1c;
         }

         namespace lua_State {
              inline constexpr uintptr_t L_global_offset = 0x78;
         }

         namespace Proto {
              inline constexpr uintptr_t code      = 0x50;
              inline constexpr uintptr_t debuginsn = 0x68;
              inline constexpr uintptr_t k         = 0x48;
              inline constexpr uintptr_t lineinfo  = 0x40;
              inline constexpr uintptr_t locvars   = 0x20;
              inline constexpr uintptr_t memcat    = 0x1;
              inline constexpr uintptr_t p         = 0x30;
         }
    }

    namespace MaterialColors {
         inline constexpr uintptr_t Asphalt     = 0x30;
         inline constexpr uintptr_t Basalt      = 0x27;
         inline constexpr uintptr_t Brick       = 0xf;
         inline constexpr uintptr_t Cobblestone = 0x33;
         inline constexpr uintptr_t Concrete    = 0xc;
         inline constexpr uintptr_t CrackedLava = 0x2d;
         inline constexpr uintptr_t Glacier     = 0x1b;
         inline constexpr uintptr_t Grass       = 0x6;
         inline constexpr uintptr_t Ground      = 0x2a;
         inline constexpr uintptr_t Ice         = 0x36;
         inline constexpr uintptr_t LeafyGrass  = 0x39;
         inline constexpr uintptr_t Limestone   = 0x3f;
         inline constexpr uintptr_t Mud         = 0x24;
         inline constexpr uintptr_t Pavement    = 0x42;
         inline constexpr uintptr_t Rock        = 0x18;
         inline constexpr uintptr_t Salt        = 0x3c;
         inline constexpr uintptr_t Sand        = 0x12;
         inline constexpr uintptr_t Sandstone   = 0x21;
         inline constexpr uintptr_t Slate       = 0x9;
         inline constexpr uintptr_t Snow        = 0x1e;
         inline constexpr uintptr_t WoodPlanks  = 0x15;
    }

    namespace MaterialLayer {
         inline constexpr uintptr_t ColorData    = 0x24;
         inline constexpr uintptr_t FillModeByte = 0x11;
         inline constexpr uintptr_t Flags2       = 0x20;
         inline constexpr uintptr_t MatFlags     = 0x18;
         inline constexpr uintptr_t Param        = 0x1c;
         inline constexpr uintptr_t Stride       = 0x88;
    }

    namespace MemEnforcedLRUCache {
         inline constexpr uintptr_t Head = 0x8;
    }

    namespace MeshContentProvider {
         inline constexpr uintptr_t LRUHolder = 0xc0;
    }

    namespace MeshPart {
         inline constexpr uintptr_t MeshId   = 0x2f8;
         inline constexpr uintptr_t MeshSize = 0x210;
         inline constexpr uintptr_t Texture  = 0x328;
    }

    namespace Misc {
         inline constexpr uintptr_t Adornee             = 0xe0;
         inline constexpr uintptr_t AnimationId         = 0xa8;
         inline constexpr uintptr_t Bytecode_xref       = 0x26f4985;
         inline constexpr uintptr_t GetProperty         = 0x4aa60b3;
         inline constexpr uintptr_t NewInstance         = 0x4799870;
         inline constexpr uintptr_t Print               = 0x1d071a0;
         inline constexpr uintptr_t ScriptContextResume = 0x43004b0;
         inline constexpr uintptr_t StringLength        = 0x10;
         inline constexpr uintptr_t Value               = 0xa0;
    }

    namespace Model {
         inline constexpr uintptr_t PrimaryPart = 0x240;
         inline constexpr uintptr_t Scale       = 0x12c;
    }

    namespace ModuleScript {
         inline constexpr uintptr_t Bytecode = 0x138;
         inline constexpr uintptr_t GUID     = 0xc0;
         inline constexpr uintptr_t Hash     = 0x888;
    }

    namespace Motor6D {
         inline constexpr uintptr_t Part0 = 0x100;
         inline constexpr uintptr_t Part1 = 0x110;
    }

    namespace ParticleEmitter {
         inline constexpr uintptr_t Acceleration        = 0x1c8;
         inline constexpr uintptr_t Brightness          = 0x204;
         inline constexpr uintptr_t Drag                = 0x208;
         inline constexpr uintptr_t Lifetime            = 0x1dc;
         inline constexpr uintptr_t LightEmission       = 0x220;
         inline constexpr uintptr_t LightInfluence      = 0x224;
         inline constexpr uintptr_t Rate                = 0x230;
         inline constexpr uintptr_t Rotation            = 0x1ec;
         inline constexpr uintptr_t RotSpeed            = 0x1e4;
         inline constexpr uintptr_t Speed               = 0x1f4;
         inline constexpr uintptr_t SpreadAngle         = 0x1fc;
         inline constexpr uintptr_t Texture             = 0x1a8;
         inline constexpr uintptr_t TimeScale           = 0x244;
         inline constexpr uintptr_t VelocityInheritance = 0x248;
         inline constexpr uintptr_t ZOffset             = 0x24c;
    }

    namespace Player {
         inline constexpr uintptr_t AccountAge            = 0x34c;
         inline constexpr uintptr_t CameraMode            = 0x368;
         inline constexpr uintptr_t DisplayName           = 0x128;
         inline constexpr uintptr_t HealthDisplayDistance = 0x38c;
         inline constexpr uintptr_t LocaleId              = 0x100;
         inline constexpr uintptr_t LocalPlayer           = 0x118;
         inline constexpr uintptr_t MaxZoomDistance       = 0x360;
         inline constexpr uintptr_t MinZoomDistance       = 0x364;
         inline constexpr uintptr_t ModelInstance         = 0x290;
         inline constexpr uintptr_t Mouse                 = 0x1208;
         inline constexpr uintptr_t NameDisplayDistance   = 0x39c;
         inline constexpr uintptr_t Team                  = 0x2d0;
         inline constexpr uintptr_t TeamColor             = 0x3a8;
         inline constexpr uintptr_t UserId                = 0xc8;
    }

    namespace Primitive {
         inline constexpr uintptr_t AssemblyAngularVelocity = 0xec;
         inline constexpr uintptr_t AssemblyLinearVelocity  = 0xe0;
         inline constexpr uintptr_t Flags                   = 0x1be;
         inline constexpr uintptr_t Material                = 0x0;
         inline constexpr uintptr_t Owner                   = 0x218;
         inline constexpr uintptr_t Position                = 0xd4;
         inline constexpr uintptr_t Rotation                = 0xb0;
         inline constexpr uintptr_t Size                    = 0x1c4;
         inline constexpr uintptr_t Validate                = 0x6;
    }

    namespace PrimitiveFlags {
         inline constexpr uintptr_t Anchored   = 0x2;
         inline constexpr uintptr_t CanCollide = 0x8;
         inline constexpr uintptr_t CanQuery   = 0x20;
         inline constexpr uintptr_t CanTouch   = 0x10;
    }

    namespace ProximityPrompt {
         inline constexpr uintptr_t ActionText            = 0x98;
         inline constexpr uintptr_t Enabled               = 0x11e;
         inline constexpr uintptr_t GamepadKeyCode        = 0x104;
         inline constexpr uintptr_t HoldDuration          = 0x108;
         inline constexpr uintptr_t KeyCode               = 0x10c;
         inline constexpr uintptr_t MaxActivationDistance = 0x110;
         inline constexpr uintptr_t ObjectText            = 0xb8;
         inline constexpr uintptr_t RequiresLineOfSight   = 0x98;
    }

    namespace Reflection {
         inline constexpr uintptr_t CreatorTable = 0x8b63c68;
         inline constexpr uintptr_t EntryValue   = 0x8;
         inline constexpr uintptr_t NameRegistry = 0x8681bc0;
         inline constexpr uintptr_t NameTable    = 0x50;
         inline constexpr uintptr_t TableEmpty   = 0x20;
         inline constexpr uintptr_t TableEnd     = 0x8;
         inline constexpr uintptr_t TableStart   = 0x0;
         inline constexpr uintptr_t TableStride  = 0x10;
    }

    namespace RemoteEvent {
         inline constexpr uintptr_t BaseVTableRva     = 0x7057398;
         inline constexpr uintptr_t HookSlotCount     = 0x7;
         inline constexpr uintptr_t InstanceVTableRva = 0x6fe27d8;
         inline constexpr uintptr_t SignalFire        = 0x35b5f70;
         inline constexpr uintptr_t SignalFireSlot    = 0x2;
         inline constexpr uintptr_t VTableRva         = 0x705cd60;
         inline constexpr uintptr_t VTableSlots       = 0x4f;
         namespace Fire {
              inline constexpr uintptr_t FireAllClients     = 0x34def5a;
              inline constexpr uintptr_t FireAllClientsB    = 0x34df55a;
              inline constexpr uintptr_t FireAllClientsPrep = 0x1270;
              inline constexpr uintptr_t FireClient         = 0x34ded28;
              inline constexpr uintptr_t FireClientB        = 0x34df328;
              inline constexpr uintptr_t FireClientPrep     = 0x1270;
              inline constexpr uintptr_t FireServer         = 0x34deb1c;
              inline constexpr uintptr_t FireServerB        = 0x34df11c;
              inline constexpr uintptr_t FireServerPrep     = 0x74d260;
              inline constexpr uintptr_t InvokeClient       = 0x35b2247;
              inline constexpr uintptr_t InvokeClientPrep   = 0x74d260;
              inline constexpr uintptr_t InvokeServer       = 0x35b1e77;
              inline constexpr uintptr_t InvokeServerPrep   = 0x74d260;
         }
    }

    namespace RenderJob {
         inline constexpr uintptr_t FakeDataModel = 0x38;
         inline constexpr uintptr_t RealDataModel = 0x1f0;
         inline constexpr uintptr_t RenderView    = 0x1e0;
    }

    namespace RenderView {
         inline constexpr uintptr_t DeviceD3D11   = 0x8;
         inline constexpr uintptr_t LightingValid = 0x11d;
         inline constexpr uintptr_t SkyValid      = 0x2dc;
         inline constexpr uintptr_t VisualEngine  = 0x18;
         inline constexpr uintptr_t VTableRva     = 0x70633f0;
    }

    namespace RunService {
         inline constexpr uintptr_t HeartbeatFPS  = 0xc8;
         inline constexpr uintptr_t HeartbeatTask = 0xe0;
    }

    namespace Script {
         inline constexpr uintptr_t GUID = 0xc0;
         inline constexpr uintptr_t Hash = 0x188;
    }

    namespace Seat {
         inline constexpr uintptr_t Occupant = 0x200;
    }

    namespace ShaderManager {
         inline constexpr uintptr_t VTableRva = 0x7064978;
    }

    namespace Sky {
         inline constexpr uintptr_t CubeTextures      = 0x3811a10;
         inline constexpr uintptr_t DrawCubeCallA     = 0x3815b49;
         inline constexpr uintptr_t DrawCubeCallB     = 0x3815c21;
         inline constexpr uintptr_t DrawSkyEnv        = 0x3815b49;
         inline constexpr uintptr_t DrawSkyPixel      = 0x3815c21;
         inline constexpr uintptr_t DrawStars         = 0x3816fdc;
         inline constexpr uintptr_t DrawStarsB        = 0x38170a0;
         inline constexpr uintptr_t DrawSun           = 0x381671c;
         inline constexpr uintptr_t MoonAngularSize   = 0x22c;
         inline constexpr uintptr_t MoonTextureId     = 0xb0;
         inline constexpr uintptr_t SkyboxBk          = 0xe0;
         inline constexpr uintptr_t SkyboxDn          = 0x110;
         inline constexpr uintptr_t SkyboxFt          = 0x140;
         inline constexpr uintptr_t SkyboxLf          = 0x170;
         inline constexpr uintptr_t SkyboxOrientation = 0x220;
         inline constexpr uintptr_t SkyboxRt          = 0x1a0;
         inline constexpr uintptr_t SkyboxUp          = 0x1d0;
         inline constexpr uintptr_t SkyGroup          = 0x3810d7a;
         inline constexpr uintptr_t SkyThread         = 0x3812455;
         inline constexpr uintptr_t StarCount         = 0x230;
         inline constexpr uintptr_t SunAngularSize    = 0x224;
         inline constexpr uintptr_t SunTextureId      = 0x200;
    }

    namespace Sound {
         inline constexpr uintptr_t IsPlaying          = 0x128;
         inline constexpr uintptr_t Looped             = 0x125;
         inline constexpr uintptr_t PlaybackSpeed      = 0x104;
         inline constexpr uintptr_t RollOffMaxDistance = 0x108;
         inline constexpr uintptr_t RollOffMinDistance = 0x10c;
         inline constexpr uintptr_t SoundGroup         = 0xd0;
         inline constexpr uintptr_t SoundId            = 0xb0;
         inline constexpr uintptr_t Volume             = 0x118;
    }

    namespace SpawnLocation {
         inline constexpr uintptr_t AllowTeamChangeOnTouch = 0x38;
         inline constexpr uintptr_t Enabled                = 0x1d9;
         inline constexpr uintptr_t ForcefieldDuration     = 0x1d0;
         inline constexpr uintptr_t Neutral                = 0x95;
         inline constexpr uintptr_t TeamColor              = 0x1d4;
    }

    namespace SpecialMesh {
         inline constexpr uintptr_t MeshId = 0xe0;
         inline constexpr uintptr_t Scale  = 0xac;
    }

    namespace StatsItem {
         inline constexpr uintptr_t Value = 0x300;
    }

    namespace SunRaysEffect {
         inline constexpr uintptr_t Enabled   = 0x98;
         inline constexpr uintptr_t Intensity = 0xa0;
         inline constexpr uintptr_t Spread    = 0xa4;
    }

    namespace SurfaceAppearance {
         inline constexpr uintptr_t AlphaMode           = 0x1d8;
         inline constexpr uintptr_t Color               = 0x1c0;
         inline constexpr uintptr_t ColorMap            = 0xb0;
         inline constexpr uintptr_t EmissiveMaskContent = 0xe0;
         inline constexpr uintptr_t EmissiveStrength    = 0x1dc;
         inline constexpr uintptr_t EmissiveTint        = 0x1cc;
         inline constexpr uintptr_t MetalnessMap        = 0x110;
         inline constexpr uintptr_t NormalMap           = 0x140;
         inline constexpr uintptr_t RoughnessMap        = 0x170;
    }

    namespace TaskScheduler {
         inline constexpr uintptr_t JobEnd   = 0xd0;
         inline constexpr uintptr_t JobName  = 0x18;
         inline constexpr uintptr_t JobStart = 0xc8;
         inline constexpr uintptr_t MaxFPS   = 0xb0;
         inline constexpr uintptr_t Pointer  = 0x8f026a8;
    }

    namespace Team {
         inline constexpr uintptr_t BrickColor = 0xa0;
    }

    namespace TechniqueArray {
         inline constexpr uintptr_t BeginOffset = 0x0;
         inline constexpr uintptr_t EndOffset   = 0x8;
         inline constexpr uintptr_t EntryStride = 0x88;
    }

    namespace Terrain {
         inline constexpr uintptr_t GrassLength       = 0x1d8;
         inline constexpr uintptr_t MaterialColors    = 0x4a0;
         inline constexpr uintptr_t WaterColor        = 0x1c8;
         inline constexpr uintptr_t WaterReflectance  = 0x1e0;
         inline constexpr uintptr_t WaterTransparency = 0x1e4;
         inline constexpr uintptr_t WaterWaveSize     = 0x1e8;
         inline constexpr uintptr_t WaterWaveSpeed    = 0x1ec;
    }

    namespace TextLabel {
         inline constexpr uintptr_t ContentText         = 0xe38;
         inline constexpr uintptr_t LocalizedText       = 0xbd0;
         inline constexpr uintptr_t MaxVisibleGraphemes = 0xa0;
         inline constexpr uintptr_t RichText            = 0x306;
         inline constexpr uintptr_t Text                = 0xbd0;
         inline constexpr uintptr_t TextColor3          = 0xee8;
         inline constexpr uintptr_t TextSize            = 0xda4;
    }

    namespace Textures {
         inline constexpr uintptr_t Decal_Texture   = 0x1c8;
         inline constexpr uintptr_t Face            = 0xb8;
         inline constexpr uintptr_t StudsPerTile    = 0x2d8;
         inline constexpr uintptr_t Texture_Texture = 0x1c8;
    }

    namespace UnionOperation {
         inline constexpr uintptr_t AssetId        = 0x2f8;
         inline constexpr uintptr_t FormFactor     = 0x394;
         inline constexpr uintptr_t SmoothingAngle = 0x39c;
    }

    namespace UserInputService {
         inline constexpr uintptr_t WindowInputState = 0x2a8;
    }

    namespace VehicleSeat {
         inline constexpr uintptr_t MaxSpeed      = 0x210;
         inline constexpr uintptr_t SteerFloat    = 0x214;
         inline constexpr uintptr_t ThrottleFloat = 0x218;
         inline constexpr uintptr_t Torque        = 0x21c;
         inline constexpr uintptr_t TurnSpeed     = 0x220;
    }

    namespace ViewBase {
         inline constexpr uintptr_t VTableRva = 0x7063668;
    }

    namespace ViewportFrame {
         inline constexpr uintptr_t Ambient           = 0xa10;
         inline constexpr uintptr_t CameraFieldOfView = 0xa40;
         inline constexpr uintptr_t LightColor        = 0xa28;
         inline constexpr uintptr_t LightDirection    = 0xa34;
    }

    namespace VisualEngine {
         inline constexpr uintptr_t Dimensions    = 0xb10;
         inline constexpr uintptr_t FakeDataModel = 0xaf0;
         inline constexpr uintptr_t Pointer       = 0x89dc1a0;
         inline constexpr uintptr_t RenderView    = 0xc40;
         inline constexpr uintptr_t ViewMatrix    = 0x1b0;
    }

    namespace Weld {
         inline constexpr uintptr_t Part0 = 0x100;
         inline constexpr uintptr_t Part1 = 0x110;
    }

    namespace WeldConstraint {
         inline constexpr uintptr_t Part0 = 0xa0;
         inline constexpr uintptr_t Part1 = 0xb0;
    }

    namespace WindowInputState {
         inline constexpr uintptr_t CapsLock       = 0x40;
         inline constexpr uintptr_t CurrentTextBox = 0x48;
    }

    namespace Workspace {
         inline constexpr uintptr_t CurrentCamera       = 0x4a0;
         inline constexpr uintptr_t DistributedGameTime = 0x4c8;
         inline constexpr uintptr_t ReadOnlyGravity     = 0x9c8;
         inline constexpr uintptr_t World               = 0x3f8;
    }

    namespace World {
         inline constexpr uintptr_t AirProperties            = 0x238;
         inline constexpr uintptr_t FallenPartsDestroyHeight = 0x214;
         inline constexpr uintptr_t Gravity                  = 0x220;
         inline constexpr uintptr_t Primitives               = 0x2b0;
         inline constexpr uintptr_t worldStepsPerSec         = 0x860;
    }

    namespace WorldRoot {
         inline constexpr uintptr_t RaycastBoundDesc = 0x86e0d50;
         inline constexpr uintptr_t RaycastBoundFn   = 0x90;
    }

}
