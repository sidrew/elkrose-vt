# Retired: the "Talk about Birth Control" topic was never live -- it was only ever registered as a
# commented-out small-talk option (removed during the merge). Birth-control discussion is covered by the
# bc_methods beat in the merged "Pregnancy & Protection" topic, and this file's distinct persuasion angles
# (natural cycle / family / thrill / health) were salvaged into that beat as consent-routed pitches
# (1.0.14). The original 9-type initial_reaction body is NOT preserved in a .bak file -- recover it
# via git history instead (e.g. `git show HEAD:dialogs/vt_small_talk_birth_control.rpy` / `git log -p`
# on this path), which still has the pre-migration version as of this commit's parent.
# Shims below keep old label references / in-flight saves resolving instead of erroring.
label small_talk_birth_control:
    jump vt_small_talk_birth_control

label vt_small_talk_birth_control:
    jump vt_small_talk_pregnancy

label vt_small_talk_birth_control_followup:
    return
