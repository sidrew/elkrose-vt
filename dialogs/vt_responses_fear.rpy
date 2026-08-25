# VT FEAR SMALL-TALK RESPONSE DATA
#
# Data for the dialog response engine (00_vt_dialog_engine.rpy). DATA ONLY. Lines lifted VERBATIM
# from the live tree(s) in dialogs/vt_small_talk_fear.rpy. Auto-generated + exhaustively sweep-validated (see the
# affection sibling for the pattern write-up).
#
# STAT-CASCADE PATTERN: the live tree routes on a fear-tier and, within each tier, on compound
# stat thresholds resolved by if/elif ORDER. Reproduced with dict-threshold `when` values
# ({{"gt": N}} / {{"lt": N}}) mirroring the live `stat > N` / `< N` splits, and `priority` encoding
# if/elif order (earliest branch = highest priority -> first match wins; the final empty-`when` entry
# is the universal fallback). LEFT IN LABEL: per-tier narrator intros and every apply_impacts.
# neutral-only -> behaviour-preserving.

init python:

    vt_register_responses("fear_smalltalk", [

        {"when": {"fear": {"lt": 15}, "discipline": {"gt": 70}}, "priority": 310, "lines": {"neutral": ["Is this supposed to intimidate me? It's rather pathetic."]}},
        {"when": {"fear": {"lt": 15}, "corruption": {"gt": 60}}, "priority": 300, "lines": {"neutral": ["I've heard worse threats from people who actually meant them. Try harder."]}},
        {"when": {"fear": {"lt": 15}, "intellect": {"gt": 70}}, "priority": 290, "lines": {"neutral": ["Your attempts at psychological manipulation are transparent and poorly executed."]}},
        {"when": {"fear": {"lt": 15}, "affection": {"gt": 40}}, "priority": 280, "lines": {"neutral": ["Why are you saying these things? I thought you cared about me."]}},
        {"when": {"fear": {"lt": 15}, "naturism": {"gt": 60}}, "priority": 270, "lines": {"neutral": ["Nature's true threats are far more impressive than this. You're like a storm that's lost its power."]}},
        {"when": {"fear": {"lt": 15}}, "priority": 260, "lines": {"neutral": ["I don't understand why you're saying this. It's not scary at all."]}},
        {"when": {"fear": {"lt": 30}, "discipline": {"gt": 50}}, "priority": 250, "lines": {"neutral": ["I won't let you see that you're getting to me. I'm stronger than that."]}},
        {"when": {"fear": {"lt": 30}, "corruption": {"gt": 40}}, "priority": 240, "lines": {"neutral": ["Interesting approach. Most people try bribery first."]}},
        {"when": {"fear": {"lt": 30}, "affection": {"gt": 30}}, "priority": 230, "lines": {"neutral": ["Why are you doing this? I thought we had something special."]}},
        {"when": {"fear": {"lt": 30}, "intellect": {"gt": 60}}, "priority": 220, "lines": {"neutral": ["I recognize what you're doing, but I must admit it's... somewhat effective."]}},
        {"when": {"fear": {"lt": 30}}, "priority": 210, "lines": {"neutral": ["I'm not sure what you're trying to accomplish with this conversation."]}},
        {"when": {"fear": {"lt": 45}, "discipline": {"gt": 40}}, "priority": 200, "lines": {"neutral": ["I'm trying to remain calm, but you're making it difficult."]}},
        {"when": {"fear": {"lt": 45}, "corruption": {"gt": 50}}, "priority": 190, "lines": {"neutral": ["You're playing a dangerous game. I hope you know what you're doing."]}},
        {"when": {"fear": {"lt": 45}, "affection": {"gt": 40}}, "priority": 180, "lines": {"neutral": ["Please don't say things like that. You're scaring me, but I still care about you."]}},
        {"when": {"fear": {"lt": 45, "gt": 35}, "intellect": {"gt": 50}}, "priority": 170, "lines": {"neutral": ["My mind knows this is manipulation, but my body is responding anyway."]}},
        {"when": {"fear": {"lt": 45}}, "priority": 160, "lines": {"neutral": ["I'd rather you didn't talk about these things."]}},
        {"when": {"fear": {"lt": 60}, "discipline": {"gt": 30}}, "priority": 150, "lines": {"neutral": ["I'm trying to stay strong, but you're breaking down my defenses."]}},
        {"when": {"fear": {"lt": 60}, "corruption": {"gt": 40}}, "priority": 140, "lines": {"neutral": ["You're awakening something dark in me. I'm not sure how I feel about that."]}},
        {"when": {"fear": {"lt": 60}, "affection": {"gt": 50}}, "priority": 130, "lines": {"neutral": ["I know I should run, but part of me still wants to stay with you."]}},
        {"when": {"fear": {"lt": 60}, "intellect": {"gt": 50}}, "priority": 120, "lines": {"neutral": ["I understand the psychology behind what you're doing, but knowing doesn't make it less effective."]}},
        {"when": {"fear": {"lt": 60}}, "priority": 110, "lines": {"neutral": ["Please... can we talk about something else?"]}},
        {"when": {"fear": {"lt": 75}, "discipline": {"gt": 20}}, "priority": 100, "lines": {"neutral": ["I've always prided myself on my control, but with you... I feel powerless."]}},
        {"when": {"fear": {"lt": 75}, "corruption": {"gt": 50}}, "priority": 90, "lines": {"neutral": ["There's a part of me that's terrified, and another part that's terrifyingly excited."]}},
        {"when": {"fear": {"lt": 75}, "affection": {"gt": 60}}, "priority": 80, "lines": {"neutral": ["I should hate you for making me feel this way, but I can't. I still need you."]}},
        {"when": {"fear": {"lt": 75}, "intellect": {"lt": 40}}, "priority": 70, "lines": {"neutral": ["I don't understand what's happening. I just know I'm scared."]}},
        {"when": {"fear": {"lt": 75}}, "priority": 60, "lines": {"neutral": ["I'll do whatever you want. Just please don't hurt me."]}},
        {"when": {"discipline": {"gt": 10}}, "priority": 50, "lines": {"neutral": ["All my principles, all my training... none of it matters when I'm with you."]}},
        {"when": {"corruption": {"gt": 60}}, "priority": 40, "lines": {"neutral": ["I never knew fear and desire could feel so similar. You've taught me so much."]}},
        {"when": {"affection": {"gt": 70}}, "priority": 30, "lines": {"neutral": ["I'm terrified of you, but I'm more terrified of losing you. Does that make sense?"]}},
        {"when": {"naturism": {"gt": 50}}, "priority": 20, "lines": {"neutral": ["You're like a force of nature. I can't resist you any more than I can resist a storm."]}},
        {"when": {}, "priority": 10, "lines": {"neutral": ["Please... I'll do anything. Just tell me what you want."]}},

    ])

    vt_register_responses("fear_lower_smalltalk", [

        {"when": {"fear": {"gt": 85}, "discipline": {"gt": 50}}, "priority": 310, "lines": {"neutral": ["I don't understand why you're saying this. Is this another trick?"]}},
        {"when": {"fear": {"gt": 85}, "corruption": {"gt": 60}}, "priority": 300, "lines": {"neutral": ["I don't believe you're being sincere. What's your real angle?"]}},
        {"when": {"fear": {"gt": 85}, "affection": {"lt": 30}}, "priority": 290, "lines": {"neutral": ["Please don't hurt me. I'll do whatever you want."]}},
        {"when": {"fear": {"gt": 85}, "intellect": {"gt": 60}}, "priority": 280, "lines": {"neutral": ["This sudden change in approach seems strategically motivated rather than genuine."]}},
        {"when": {"fear": {"gt": 90}}, "priority": 270, "lines": {"neutral": ["I don't understand why you're saying this. Please don't hurt me."]}},
        {"when": {"fear": {"gt": 85}}, "priority": 260, "lines": {"neutral": ["I want to believe you, but I'm still scared."]}},
        {"when": {"fear": {"gt": 70}, "discipline": {"gt": 40}}, "priority": 250, "lines": {"neutral": ["I appreciate your effort to be less intimidating, but trust takes time."]}},
        {"when": {"fear": {"gt": 70}, "corruption": {"gt": 50}}, "priority": 240, "lines": {"neutral": ["This softer approach doesn't suit you. I liked the other you better."]}},
        {"when": {"fear": {"gt": 70}, "affection": {"gt": 40}}, "priority": 230, "lines": {"neutral": ["Thank you. It means a lot that you're trying to make me more comfortable."]}},
        {"when": {"fear": {"gt": 70}, "intellect": {"gt": 50}}, "priority": 220, "lines": {"neutral": ["I recognize this as a de-escalation technique, but I appreciate it nonetheless."]}},
        {"when": {"fear": {"gt": 70}}, "priority": 210, "lines": {"neutral": ["I'm still a little nervous, but this helps."]}},
        {"when": {"fear": {"gt": 55}, "discipline": {"gt": 30}}, "priority": 200, "lines": {"neutral": ["Your gentler side is unexpected. I'm curious to see more of it."]}},
        {"when": {"fear": {"gt": 55}, "corruption": {"gt": 40}}, "priority": 190, "lines": {"neutral": ["Don't think this makes me weak. I'm just allowing you this small victory."]}},
        {"when": {"fear": {"gt": 55}, "affection": {"gt": 50}}, "priority": 180, "lines": {"neutral": ["This is the person I hoped was inside you all along."]}},
        {"when": {"fear": {"gt": 55}, "intellect": {"lt": 50}}, "priority": 170, "lines": {"neutral": ["You're not as scary when you talk like this. I like it."]}},
        {"when": {"fear": {"gt": 55}}, "priority": 160, "lines": {"neutral": ["I feel like I can breathe a little easier now."]}},
        {"when": {"fear": {"gt": 40}, "discipline": {"gt": 20}}, "priority": 150, "lines": {"neutral": ["I'm beginning to see different sides of you. It's... intriguing."]}},
        {"when": {"fear": {"gt": 40}, "corruption": {"gt": 30}}, "priority": 140, "lines": {"neutral": ["I wonder which version of you is real - the terrifying one or this gentle one."]}},
        {"when": {"fear": {"gt": 40}, "affection": {"gt": 60}}, "priority": 130, "lines": {"neutral": ["When you're like this, I can forget all the times you scared me."]}},
        {"when": {"fear": {"gt": 40}, "intellect": {"gt": 50}}, "priority": 120, "lines": {"neutral": ["Your adaptability is impressive. You switch between intimidation and reassurance effortlessly."]}},
        {"when": {"fear": {"gt": 40}}, "priority": 110, "lines": {"neutral": ["I feel safer with you now."]}},
        {"when": {"fear": {"gt": 25}, "discipline": {"gt": 10}}, "priority": 100, "lines": {"neutral": ["I'm letting my guard down with you. I hope you won't make me regret it."]}},
        {"when": {"fear": {"gt": 25}, "corruption": {"gt": 20}}, "priority": 90, "lines": {"neutral": ["I almost miss the dangerous edge you had before. Almost."]}},
        {"when": {"fear": {"gt": 25}, "affection": {"gt": 70}}, "priority": 80, "lines": {"neutral": ["This is the person I knew was there. I'm so glad to finally meet you."]}},
        {"when": {"fear": {"gt": 25}, "naturism": {"gt": 50}}, "priority": 70, "lines": {"neutral": ["Like a storm passing, you've left behind calm and new growth. I like this version of you."]}},
        {"when": {"fear": {"gt": 25}}, "priority": 60, "lines": {"neutral": ["I'm starting to feel like I can trust you."]}},
        {"when": {"discipline": {"gt": 0}}, "priority": 50, "lines": {"neutral": ["I never thought I'd feel this comfortable with you. It's a pleasant surprise."]}},
        {"when": {"corruption": {"gt": 10}}, "priority": 40, "lines": {"neutral": ["Don't get too comfortable. I like you better when you're a little dangerous."]}},
        {"when": {"affection": {"gt": 80}}, "priority": 30, "lines": {"neutral": ["This is the person I fell for. I'm so glad you're letting me see them more often."]}},
        {"when": {"intellect": {"gt": 50}}, "priority": 20, "lines": {"neutral": ["Your emotional intelligence is surprising. You know exactly when to switch approaches."]}},
        {"when": {}, "priority": 10, "lines": {"neutral": ["I feel safe with you. It's a nice feeling."]}},

    ])
