# VT NATURISM SMALL-TALK RESPONSE DATA
#
# Data for the dialog response engine (00_vt_dialog_engine.rpy). DATA ONLY. Lines lifted VERBATIM
# from the live tree(s) in dialogs/vt_small_talk_naturism.rpy. Auto-generated + exhaustively sweep-validated (see the
# affection sibling for the pattern write-up).
#
# STAT-CASCADE PATTERN: the live tree routes on a naturism-tier and, within each tier, on compound
# stat thresholds resolved by if/elif ORDER. Reproduced with dict-threshold `when` values
# ({{"gt": N}} / {{"lt": N}}) mirroring the live `stat > N` / `< N` splits, and `priority` encoding
# if/elif order (earliest branch = highest priority -> first match wins; the final empty-`when` entry
# is the universal fallback). LEFT IN LABEL: per-tier narrator intros and every apply_impacts.
# neutral-only -> behaviour-preserving.

init python:

    vt_register_responses("naturism_smalltalk", [

        {"when": {"naturism": {"lt": 15}, "discipline": {"gt": 70}}, "priority": 360, "lines": {"neutral": ["This seems impractical and unhygienic. I prefer modern comforts."]}},
        {"when": {"naturism": {"lt": 15}, "corruption": {"gt": 60}}, "priority": 350, "lines": {"neutral": ["Why would anyone want to live like that? It sounds boring."]}},
        {"when": {"naturism": {"lt": 15}, "intellect": {"gt": 70}}, "priority": 340, "lines": {"neutral": ["There's no scientific evidence supporting these lifestyle choices. It's sentimental nonsense."]}},
        {"when": {"naturism": {"lt": 15}, "fear": {"gt": 60}}, "priority": 330, "lines": {"neutral": ["Being exposed to nature like that seems dangerous. What about animals and weather?"]}},
        {"when": {"naturism": {"lt": 15}, "affection": {"gt": 40}}, "priority": 320, "lines": {"neutral": ["I know this is important to you, but I'm not sure about it."]}},
        {"when": {"naturism": {"lt": 15}}, "priority": 310, "lines": {"neutral": ["I'm not sure about this. Can we talk about something else?"]}},
        {"when": {"naturism": {"lt": 30}, "discipline": {"gt": 50}}, "priority": 300, "lines": {"neutral": ["I don't normally consider such things, but there might be some merit to it."]}},
        {"when": {"naturism": {"lt": 30}, "corruption": {"gt": 40}}, "priority": 290, "lines": {"neutral": ["I suppose there's a certain freedom in it, but it seems limiting in other ways."]}},
        {"when": {"naturism": {"lt": 30}, "intellect": {"gt": 60}}, "priority": 280, "lines": {"neutral": ["From an evolutionary perspective, I can see the logic, but modern life has advantages."]}},
        {"when": {"naturism": {"lt": 30}, "fear": {"gt": 40}}, "priority": 270, "lines": {"neutral": ["It sounds... interesting, but I'm not sure I could handle the wilderness."]}},
        {"when": {"naturism": {"lt": 30}, "affection": {"gt": 30}}, "priority": 260, "lines": {"neutral": ["If it's important to you, I'd like to understand it better."]}},
        {"when": {"naturism": {"lt": 30}}, "priority": 250, "lines": {"neutral": ["This is unexpected, but I'm open to learning more."]}},
        {"when": {"naturism": {"lt": 45}, "discipline": {"gt": 40}}, "priority": 240, "lines": {"neutral": ["I'm finding myself drawn to these ideas, even though they conflict with my usual values."]}},
        {"when": {"naturism": {"lt": 45}, "corruption": {"gt": 30}}, "priority": 230, "lines": {"neutral": ["There's something primal about it that appeals to me. I never expected that."]}},
        {"when": {"naturism": {"lt": 45}, "intellect": {"gt": 50}}, "priority": 220, "lines": {"neutral": ["The more I learn, the more I realize how disconnected we've become from our roots."]}},
        {"when": {"naturism": {"lt": 45}, "fear": {"gt": 30}}, "priority": 210, "lines": {"neutral": ["I'm still a bit nervous about it, but I'm starting to see the appeal."]}},
        {"when": {"naturism": {"lt": 45}, "affection": {"gt": 40}}, "priority": 200, "lines": {"neutral": ["When you explain it like that, I can feel how important it is to you."]}},
        {"when": {"naturism": {"lt": 45}}, "priority": 190, "lines": {"neutral": ["I'm really enjoying this conversation. Tell me more!"]}},
        {"when": {"naturism": {"lt": 60}, "discipline": {"gt": 30}}, "priority": 180, "lines": {"neutral": ["I'm starting to question the artificial boundaries we've created for ourselves."]}},
        {"when": {"naturism": {"lt": 60}, "corruption": {"gt": 20}}, "priority": 170, "lines": {"neutral": ["There's a raw honesty to natural living that I find refreshing."]}},
        {"when": {"naturism": {"lt": 60}, "intellect": {"gt": 40}}, "priority": 160, "lines": {"neutral": ["The ecological and psychological benefits are becoming clearer to me now."]}},
        {"when": {"naturism": {"lt": 60}, "fear": {"gt": 20}}, "priority": 150, "lines": {"neutral": ["I used to be afraid of nature, but now I feel like I'm part of it."]}},
        {"when": {"naturism": {"lt": 60}, "affection": {"gt": 50}}, "priority": 140, "lines": {"neutral": ["Being with you in nature feels so right, like we're meant to be this way."]}},
        {"when": {"naturism": {"lt": 60}}, "priority": 130, "lines": {"neutral": ["I'm really enjoying this conversation. Tell me more!"]}},
        {"when": {"naturism": {"lt": 75}, "discipline": {"gt": 20}}, "priority": 120, "lines": {"neutral": ["I used to think control and order were everything, but nature has taught me the beauty of chaos."]}},
        {"when": {"naturism": {"lt": 75}, "corruption": {"gt": 10}}, "priority": 110, "lines": {"neutral": ["I used to think power came from dominance, but now I see it comes from harmony with nature."]}},
        {"when": {"naturism": {"lt": 75}, "intellect": {"gt": 30}}, "priority": 100, "lines": {"neutral": ["My mind once rejected these ideas, but my body and soul have embraced them."]}},
        {"when": {"naturism": {"lt": 75}, "fear": {"gt": 10}}, "priority": 90, "lines": {"neutral": ["The wilderness no longer frightens me. It feels like home."]}},
        {"when": {"naturism": {"lt": 75}, "affection": {"gt": 60}}, "priority": 80, "lines": {"neutral": ["Being natural with you feels more real than anything I've experienced before."]}},
        {"when": {"naturism": {"lt": 75}}, "priority": 70, "lines": {"neutral": ["This is exactly what I love to talk about. Let's dive deeper."]}},
        {"when": {"discipline": {"gt": 10}}, "priority": 60, "lines": {"neutral": ["I've learned that true discipline comes from listening to nature, not fighting against it."]}},
        {"when": {"corruption": {"gt": 0}}, "priority": 50, "lines": {"neutral": ["The artificial pleasures I once sought seem hollow compared to the joy of natural living."]}},
        {"when": {"intellect": {"gt": 20}}, "priority": 40, "lines": {"neutral": ["I used to think humanity was above nature, but now I know we are nature."]}},
        {"when": {"fear": {"gt": 0}}, "priority": 30, "lines": {"neutral": ["I once feared the wild, but now I fear a life without it more."]}},
        {"when": {"affection": {"gt": 70}}, "priority": 20, "lines": {"neutral": ["With you, I've discovered my true nature. We're like two animals finding their mate in the wild."]}},
        {"when": {}, "priority": 10, "lines": {"neutral": ["This is who I am now. I could never go back to living the way I did before."]}},

    ])
