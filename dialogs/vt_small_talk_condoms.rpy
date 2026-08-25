# Retired: the Condoms topic was a stale duplicate of the protection menu in
# vt_small_talk_pregnancy.rpy (older raw-scalar tuning, no vt_say). Merged into the
# "Talk about Pregnancy & Protection" topic (1.0.14). Original body is NOT preserved in a .bak
# file -- recover it via git history instead (e.g. `git show HEAD:dialogs/vt_small_talk_condoms.rpy`
# / `git log -p` on this path), which still has the pre-migration version as of this commit's
# parent. Shims below keep old label references / in-flight saves resolving instead of erroring.
label small_talk_condoms:
    jump vt_small_talk_condoms

label vt_small_talk_condoms:
    jump vt_small_talk_pregnancy

label vt_small_talk_condoms_followup:
    return
