from instances.scanvalue import scan_for_value


def dump_joint_offsets(reader, ctx, store):
    tree = ctx["tree"]
    workspace = ctx["workspace"]
    if not workspace:
        return
    rig = tree.find(workspace, "Rig")
    if not rig:
        return
    torso = tree.find(rig, "Torso")
    if not torso:
        return
    right_arm = tree.find(rig, "Right Arm")
    motor = tree.find(torso, "Right Shoulder")
    if not (motor and right_arm):
        return
    scan_for_value(reader, store, "Part1", "Motor6D", [motor], [right_arm], "u64")
    parent_off = (ctx.get("instance_offsets") or {}).get("Parent")
    off = scan_for_value(reader, store, "Part0", "Motor6D", [motor], [torso], "u64")
    if parent_off is not None and off == parent_off:
        store.get("Motor6D", {}).pop("Part0", None)
        scan_for_value(reader, store, "Part0", "Motor6D", [motor], [torso],
                       "u64", start=parent_off + 8)


def dump_adornment_offsets(reader, ctx, store):
    tree = ctx["tree"]
    workspace = ctx["workspace"]
    if not workspace:
        return
    adorn = tree.find(workspace, "BoxHandleAdornment")
    if not adorn:
        return
    pos_part = tree.find(workspace, "Position")
    if pos_part:
        scan_for_value(reader, store, "Adornee", "BoxHandleAdornment",
                       [adorn], [pos_part], "u64")
    scan_for_value(reader, store, "Color3", "BoxHandleAdornment", [adorn],
                   [(0.05098039284348488, 0.4117647111415863,
                     0.6745098233222961)], "color3", eps=0.01)
    scan_for_value(reader, store, "Size", "BoxHandleAdornment", [adorn],
                   [(1.0, 1.0, 1.0)], "v3", eps=0.001)


def dump_viewport_offsets(reader, ctx, store):
    tree = ctx["tree"]
    workspace = ctx["workspace"]
    if not workspace:
        return
    vf = tree.find(workspace, "ViewportFrame")
    if not vf:
        return
    scan_for_value(reader, store, "Ambient", "ViewportFrame", [vf],
                   [(0.7843137383460999, 0.7843137383460999,
                     0.7843137383460999)], "color3", eps=0.001)
    scan_for_value(reader, store, "LightColor", "ViewportFrame", [vf],
                   [(0.5490196347236633, 0.5490196347236633,
                     0.5490196347236633)], "color3", eps=0.001)
    scan_for_value(reader, store, "LightDirection", "ViewportFrame", [vf],
                   [(-1.0, -1.0, -1.0)], "v3", eps=0.001)
    scan_for_value(reader, store, "CameraFieldOfView", "ViewportFrame", [vf],
                   [1.4952349662780762], "float", eps=0.001)


def dump_union_offsets(reader, ctx, store):
    tree = ctx["tree"]
    workspace = ctx["workspace"]
    if not workspace:
        return
    u1 = tree.find(workspace, "Union")
    u2 = tree.find(workspace, "Union2")
    if u1 and u2:
        scan_for_value(reader, store, "SmoothingAngle", "UnionOperation",
                       [u1, u2], [168.0, 180.0], "float", eps=0.01)
        scan_for_value(reader, store, "FormFactor", "UnionOperation",
                       [u1, u2], [3, 3], "int")


def dump_humanoid_extra_offsets(reader, ctx, store):
    tree = ctx["tree"]
    workspace = ctx["workspace"]
    if not workspace:
        return
    hs = [tree.find(workspace, "Humanoid%d" % i) for i in range(2, 8)]
    if not all(hs):
        return
    scan_for_value(reader, store, "RequiresNeck", "Humanoid", hs,
                   [True, True, False, True, False, True], "bool")
    scan_for_value(reader, store, "BreakJointsOnDeath", "Humanoid", hs,
                   [True, True, True, True, False, False], "bool")
    scan_for_value(reader, store, "AutomaticScalingEnabled", "Humanoid", hs,
                   [True, True, True, False, False, False], "bool")
    scan_for_value(reader, store, "UseJumpPower", "Humanoid", hs,
                   [False, True, True, True, False, True], "bool")
    scan_for_value(reader, store, "AutoJumpEnabled", "Humanoid", hs,
                   [True, True, True, False, False, True], "bool")
    scan_for_value(reader, store, "EvaluateStateMachine", "Humanoid", hs,
                   [True, True, True, False, True, True], "bool")


def dump_extra_offsets(reader, ctx, store):
    dump_joint_offsets(reader, ctx, store)
    dump_adornment_offsets(reader, ctx, store)
    dump_viewport_offsets(reader, ctx, store)
    dump_union_offsets(reader, ctx, store)
    dump_humanoid_extra_offsets(reader, ctx, store)
