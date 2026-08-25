# VT AFFECTION SMALL-TALK RESPONSE DATA
#
# Data for the dialog response engine (00_vt_dialog_engine.rpy). DATA ONLY -- no control flow.
# Lines lifted VERBATIM from the live tree in dialogs/vt_small_talk_affection.rpy.
#
# STAT-CASCADE PATTERN (differs from the pregnancy small-talk's approach/role routing):
# the live tree routes on an AFFECTION TIER (<15 / <30 / <45 / <60 / <75 / else) and, within each
# tier, on compound stat thresholds (fear>60, corruption>40 and fear<40, ...) resolved by if/elif
# ORDER (first match wins). Two mechanics reproduce that here:
#   1. dict-threshold `when` values -- {"gt": N} / {"lt": N} / {"ge": N, "lt": N} -- mirror the live
#      `stat > N` / `stat < N` splits exactly (the cut points are the mod author's, not new constants).
#      A branch's affection bound folds the tier range together with any in-branch affection test
#      (e.g. tier [60,75) AND affection>65  ->  {"gt": 65, "lt": 75}).
#   2. `priority` encodes if/elif ORDER: earliest branch = highest priority, so the max-priority
#      filter picks the first matching branch, and the per-tier `else` (affection-range only) is the
#      lowest priority in its tier -> it wins only when no earlier branch matched. Priorities descend
#      globally in source order; tiers are disjoint on affection so they never co-match anyway.
#
# LEFT IN LABEL (not migrated): the per-tier narrator intros ("[selected_girl] seems guarded..."),
# every per-branch `apply_impacts`, and each tier's trailing `apply_impacts({"affection": ...})`.
# Only the spoken `selected_girl.character` line migrates. neutral-only -> behaviour-preserving
# (vt_voice resolves neutral for every register; register enrichment is a later, separate track).

init python:

    vt_register_responses("affection_smalltalk", [

        # ===== TIER: affection < 15  (guarded) ==================================================
        {"when": {"affection": {"lt": 15}, "fear": {"gt": 60}}, "priority": 1000, "lines": {
            "neutral": ["Please... I don't want to talk about this. Can't we just leave it alone?"]}},
        {"when": {"affection": {"lt": 15}, "discipline": {"gt": 60}}, "priority": 990, "lines": {
            "neutral": ["This conversation is inappropriate. I'd prefer if we discussed something else."]}},
        {"when": {"affection": {"lt": 15}, "corruption": {"gt": 60}}, "priority": 980, "lines": {
            "neutral": ["If you're trying to get something from me, just say it directly. I don't have time for games."]}},
        {"when": {"affection": {"lt": 15}, "intellect": {"gt": 70}}, "priority": 970, "lines": {
            "neutral": ["I fail to see the practical value in this conversation. Can we move on?"]}},
        {"when": {"affection": {"lt": 15}, "naturism": {"gt": 60}}, "priority": 960, "lines": {
            "neutral": ["Human interactions feel so forced sometimes. I'd rather be in nature."]}},
        {"when": {"affection": {"lt": 15}}, "priority": 950, "lines": {
            "neutral": ["I'm not comfortable discussing this with you."]}},

        # ===== TIER: 15 <= affection < 30  (warming up) =========================================
        {"when": {"affection": {"ge": 15, "lt": 30}, "intellect": {"gt": 70}, "discipline": {"gt": 50}}, "priority": 900, "lines": {
            "neutral": ["That's an interesting perspective. I'd like to explore the logical implications further."]}},
        {"when": {"affection": {"ge": 15, "lt": 30}, "naturism": {"gt": 70}}, "priority": 890, "lines": {
            "neutral": ["This reminds me of how connected we all are to nature's cycles. Have you ever noticed...?"]}},
        {"when": {"affection": {"ge": 15, "lt": 30}, "corruption": {"gt": 40}, "fear": {"lt": 40}}, "priority": 880, "lines": {
            "neutral": ["I might be interested... but what's in it for me?"]}},
        {"when": {"affection": {"ge": 15, "lt": 30}, "fear": {"gt": 50}}, "priority": 870, "lines": {
            "neutral": ["I... suppose I can listen for a little while. Please don't make this uncomfortable."]}},
        {"when": {"affection": {"ge": 15, "lt": 30}}, "priority": 860, "lines": {
            "neutral": ["I've never really thought about it that way before."]}},

        # ===== TIER: 30 <= affection < 45  (more engaged) =======================================
        {"when": {"affection": {"ge": 30, "lt": 45}, "discipline": {"gt": 60}, "corruption": {"lt": 30}}, "priority": 800, "lines": {
            "neutral": ["I find myself wanting to open up to you, even though it goes against my usual principles."]}},
        {"when": {"affection": {"gt": 35, "lt": 45}, "fear": {"gt": 40}}, "priority": 790, "lines": {
            "neutral": ["I'm scared of these feelings, but I can't deny that I'm drawn to you."]}},
        {"when": {"affection": {"ge": 30, "lt": 45}, "naturism": {"gt": 50}, "intellect": {"lt": 60}}, "priority": 780, "lines": {
            "neutral": ["Being with you feels as natural as breathing. I've never felt this way before."]}},
        {"when": {"affection": {"ge": 30, "lt": 45}, "corruption": {"gt": 50}, "discipline": {"lt": 40}}, "priority": 770, "lines": {
            "neutral": ["You know how to say all the right things. I like that in a person."]}},
        {"when": {"affection": {"ge": 30, "lt": 45}}, "priority": 760, "lines": {
            "neutral": ["I'm starting to enjoy our conversations more than I expected."]}},

        # ===== TIER: 45 <= affection < 60  (leaning in) =========================================
        {"when": {"affection": {"gt": 50, "lt": 60}, "fear": {"gt": 40}}, "priority": 700, "lines": {
            "neutral": ["Even though part of me is still afraid, being with you feels right."]}},
        {"when": {"affection": {"ge": 45, "lt": 60}, "discipline": {"gt": 60}, "corruption": {"gt": 30}}, "priority": 690, "lines": {
            "neutral": ["You're making me question everything I thought I knew about myself."]}},
        {"when": {"affection": {"ge": 45, "lt": 60}, "naturism": {"gt": 60}, "intellect": {"gt": 60}}, "priority": 680, "lines": {
            "neutral": ["The natural order and intellectual pursuits converge when I'm with you. It's fascinating."]}},
        {"when": {"affection": {"ge": 45, "lt": 60}, "corruption": {"gt": 60}, "fear": {"lt": 30}}, "priority": 670, "lines": {
            "neutral": ["I like the way you think. We should explore these ideas more... privately."]}},
        {"when": {"affection": {"ge": 45, "lt": 60}}, "priority": 660, "lines": {
            "neutral": ["I find myself looking forward to our conversations. What does that mean?"]}},

        # ===== TIER: 60 <= affection < 75  (completely focused) =================================
        {"when": {"affection": {"ge": 60, "lt": 75}, "corruption": {"gt": 70}}, "priority": 600, "lines": {
            "neutral": ["I've learned that what we want matters more than what others think we should want. And right now, I want you."]}},
        {"when": {"affection": {"ge": 60, "lt": 75}, "discipline": {"gt": 70}, "corruption": {"lt": 40}}, "priority": 590, "lines": {
            "neutral": ["I've always followed the rules, but with you... I find myself wanting to break them all."]}},
        {"when": {"affection": {"gt": 65, "lt": 75}, "fear": {"gt": 50}}, "priority": 580, "lines": {
            "neutral": ["Even though part of me is terrified, I've never felt more alive than when I'm with you."]}},
        {"when": {"affection": {"ge": 60, "lt": 75}, "naturism": {"gt": 60}, "discipline": {"lt": 40}}, "priority": 570, "lines": {
            "neutral": ["Our bodies know what our minds try to deny. I can feel how right this is between us."]}},
        {"when": {"affection": {"ge": 60, "lt": 75}, "intellect": {"gt": 70}, "corruption": {"gt": 40}}, "priority": 560, "lines": {
            "neutral": ["The rational choice would be to maintain distance, but my emotions override that logic with you."]}},
        {"when": {"affection": {"ge": 60, "lt": 75}}, "priority": 550, "lines": {
            "neutral": ["I've never felt this connection with anyone before. I want to explore it further."]}},

        # ===== TIER: affection >= 75  (complete trust) ==========================================
        {"when": {"affection": {"ge": 75}, "discipline": {"gt": 70}, "corruption": {"gt": 50}}, "priority": 500, "lines": {
            "neutral": ["You've shown me that rules are meant to be broken, and I've never felt more free."]}},
        {"when": {"affection": {"gt": 80}, "fear": {"gt": 40}}, "priority": 490, "lines": {
            "neutral": ["You've helped me overcome so many fears. With you, I feel brave enough to face anything."]}},
        {"when": {"affection": {"ge": 75}, "naturism": {"gt": 70}, "intellect": {"gt": 70}}, "priority": 480, "lines": {
            "neutral": ["With you, I've found the perfect balance between intellect and instinct, mind and nature."]}},
        {"when": {"affection": {"ge": 75}, "corruption": {"gt": 80}}, "priority": 470, "lines": {
            "neutral": ["I used to think there were limits to what I'd do, but with you, I want to explore every dark corner of desire."]}},
        {"when": {"affection": {"ge": 75}, "fear": {"lt": 20}, "discipline": {"gt": 60}}, "priority": 460, "lines": {
            "neutral": ["You've made me feel safe enough to let go of control, and disciplined enough to know my own boundaries."]}},
        {"when": {"affection": {"ge": 75}}, "priority": 450, "lines": {
            "neutral": ["I never imagined I could feel this way about someone. You've changed everything for me."]}},

    ])
