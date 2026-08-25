# VT CORRUPTION SMALL-TALK RESPONSE DATA
#
# Data for the dialog response engine (00_vt_dialog_engine.rpy). DATA ONLY. Lines lifted VERBATIM
# from the live tree(s) in dialogs/vt_small_talk_corruption.rpy. Auto-generated + exhaustively sweep-validated (see the
# affection sibling for the pattern write-up).
#
# STAT-CASCADE PATTERN: the live tree routes on a corruption-tier and, within each tier, on compound
# stat thresholds resolved by if/elif ORDER. Reproduced with dict-threshold `when` values
# ({{"gt": N}} / {{"lt": N}}) mirroring the live `stat > N` / `< N` splits, and `priority` encoding
# if/elif order (earliest branch = highest priority -> first match wins; the final empty-`when` entry
# is the universal fallback). LEFT IN LABEL: per-tier narrator intros and every apply_impacts.
# neutral-only -> behaviour-preserving.

init python:

    vt_register_responses("corruption_smalltalk", [

        {"when": {"corruption": {"lt": 15}, "discipline": {"gt": 70}}, "priority": 310, "lines": {"neutral": ["This is completely inappropriate. I refuse to discuss such matters."]}},
        {"when": {"corruption": {"lt": 15}, "fear": {"gt": 60}}, "priority": 300, "lines": {"neutral": ["Please... don't say things like that. It scares me."]}},
        {"when": {"corruption": {"lt": 15}, "affection": {"gt": 40}}, "priority": 290, "lines": {"neutral": ["I'm disappointed you'd talk about this. I thought you were different."]}},
        {"when": {"corruption": {"lt": 15}, "intellect": {"gt": 70}}, "priority": 280, "lines": {"neutral": ["This conversation lacks any intellectual merit. Let's discuss something meaningful."]}},
        {"when": {"corruption": {"lt": 15}, "naturism": {"gt": 60}}, "priority": 270, "lines": {"neutral": ["Such unnatural thoughts... They disturb the harmony I seek."]}},
        {"when": {"corruption": {"lt": 15}}, "priority": 260, "lines": {"neutral": ["Can we talk about something else?"]}},
        {"when": {"corruption": {"lt": 30}, "discipline": {"gt": 50}, "affection": {"gt": 20}}, "priority": 250, "lines": {"neutral": ["I shouldn't be interested in this... but I am. Why?"]}},
        {"when": {"corruption": {"lt": 30}, "intellect": {"gt": 60}}, "priority": 240, "lines": {"neutral": ["How interesting... from a purely academic perspective, of course."]}},
        {"when": {"corruption": {"lt": 30}, "fear": {"gt": 40}}, "priority": 230, "lines": {"neutral": ["This is wrong... but part of me wants to know more anyway."]}},
        {"when": {"corruption": {"lt": 30}, "naturism": {"gt": 50}}, "priority": 220, "lines": {"neutral": ["Nature has its dark sides too, doesn't it? Tell me more..."]}},
        {"when": {"corruption": {"lt": 30}}, "priority": 210, "lines": {"neutral": ["How interesting..."]}},
        {"when": {"corruption": {"lt": 45, "gt": 35}, "discipline": {"gt": 40}}, "priority": 200, "lines": {"neutral": ["I'm starting to understand why people find this tempting..."]}},
        {"when": {"corruption": {"lt": 45}, "affection": {"gt": 40}, "fear": {"lt": 30}}, "priority": 190, "lines": {"neutral": ["With you, even these thoughts feel exciting somehow."]}},
        {"when": {"corruption": {"lt": 45}, "intellect": {"gt": 60}}, "priority": 180, "lines": {"neutral": ["The psychological implications are fascinating. Humans are such complex creatures."]}},
        {"when": {"corruption": {"lt": 45}, "naturism": {"gt": 60}}, "priority": 170, "lines": {"neutral": ["The wildness in nature reflects the wildness in us, doesn't it?"]}},
        {"when": {"corruption": {"lt": 45}}, "priority": 160, "lines": {"neutral": ["That is {b}so{/b} interesting!"]}},
        {"when": {"corruption": {"lt": 60}, "discipline": {"gt": 30}, "affection": {"gt": 50}}, "priority": 150, "lines": {"neutral": ["I never thought I'd say this, but you're making me question my values."]}},
        {"when": {"corruption": {"lt": 60, "gt": 50}, "fear": {"gt": 30}}, "priority": 140, "lines": {"neutral": ["This scares me, but I can't stop thinking about it. About us."]}},
        {"when": {"corruption": {"lt": 60, "gt": 50}, "intellect": {"gt": 50}}, "priority": 130, "lines": {"neutral": ["Rationality tells me this is wrong, but my curiosity overwhelms reason."]}},
        {"when": {"corruption": {"lt": 60}, "naturism": {"gt": 50}, "affection": {"gt": 40}}, "priority": 120, "lines": {"neutral": ["You bring out the wild side in me I've always tried to suppress."]}},
        {"when": {"corruption": {"lt": 60}}, "priority": 110, "lines": {"neutral": ["Tell me more about this. I want to understand completely."]}},
        {"when": {"corruption": {"lt": 75, "gt": 65}, "discipline": {"gt": 20}}, "priority": 100, "lines": {"neutral": ["Rules are just society's attempt to control what feels natural. With you, I feel free."]}},
        {"when": {"corruption": {"lt": 75}, "fear": {"lt": 20}, "affection": {"gt": 60}}, "priority": 90, "lines": {"neutral": ["I used to be afraid of these thoughts, but with you, I embrace them completely."]}},
        {"when": {"corruption": {"lt": 75}, "intellect": {"gt": 60}, "discipline": {"lt": 30}}, "priority": 80, "lines": {"neutral": ["My mind understands the risks, but my body only understands desire."]}},
        {"when": {"corruption": {"lt": 75}, "naturism": {"gt": 70}}, "priority": 70, "lines": {"neutral": ["You've helped me understand that all of nature's impulses - even the dark ones - are beautiful."]}},
        {"when": {"corruption": {"lt": 75}}, "priority": 60, "lines": {"neutral": ["That is right up my alley, tell me more."]}},
        {"when": {"discipline": {"lt": 20}, "corruption": {"gt": 80}}, "priority": 50, "lines": {"neutral": ["I used to care about right and wrong. Now I only care about what feels good with you."]}},
        {"when": {"fear": {"lt": 10}, "affection": {"gt": 70}}, "priority": 40, "lines": {"neutral": ["There's nothing I wouldn't try with you. You've made me fearless."]}},
        {"when": {"intellect": {"gt": 60}, "corruption": {"gt": 85}}, "priority": 30, "lines": {"neutral": ["Intelligence without corruption is boring. You've awakened my true potential."]}},
        {"when": {"naturism": {"gt": 70}, "discipline": {"lt": 20}}, "priority": 20, "lines": {"neutral": ["In nature, the strongest survive and the most passionate thrive. We're both."]}},
        {"when": {}, "priority": 10, "lines": {"neutral": ["I never knew this part of me existed before you. Now I can't imagine life without it."]}},

    ])
