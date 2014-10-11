# ==============================
# CHAPTER 1 - Lost Children - PART 1
# ==============================
init 1:
    image title title1 = Text(chapterTitles[1], size=48, outlines={(4,"#228",0,0)}) #"gui/title_ch1.png"
    image cg ch1 chronostorm = im.Scale("cg/ch1_chronostorm.png", SCREENSIZE_X, SCREENSIZE_Y)

label ch1_1:
    $ currentChapter = 1
    play sound "music/New Chapter.wav"
    scene bg chapter_intro_splash with fadeSlow
    pause 0.5
    show title title1 at truecenter with dissolve
    pause

    stop sound fadeout 1
    scene bg dark with fadeSlow
    
    lester_serious "Oi, Tact."
    tact_oneeye "Mmmh?"
    lester_grim "Stop nodding off on the job.\nWe’re in the middle of something very important here."

    scene bg elsior bridge with fadeSlow
    $ location = "Bridge"
    play music "music/Bridge.ogg"
    tact_oneeye "Yaaawn..."
    show lester annoyed at center, dissolveCustom
    lester "Tact...\nJust because it's peacetime doesn't mean you get to not take things seriously."
    tact_aggressive "Hey now.\nI'll have you know I'm taking my rest very seriously indeed."
    show lester stressed at dissolveCustom
    lester "...Honestly.\nYou never change..."
    hide lester
    show noah hurm at center, dissolveCustom
    noah "Knock it off, you two.\nI'm trying to calibrate this meson detector here."
    tact_sweating "...My apologies, Lady Noah."

    $ location = None
    scene cg ch1 chronostorm with dissolve
    lester_serious "Chrono Storms, huh."
    tact "Supposedly they’re rifts in spacetime that connect to parallel universes."
    lester_relaxed "If you’d kept on spacing out like that, you could’ve ended up flying us into one of them."
    lester_relaxed "We’d be stranded in another universe with no way to get back."
    tact_sweating "No thanks.\nOnce is enough for me."
    tact_oh "But wouldn’t it be possible to figure out where they lead and recover us that way?\nWe’ve already done it once."
    noah_hurm "What do you think I’ve been working on?"
    noah "In any case, once I refine the theory enough, we should be able to predict where a given storm leads, even before it happens."
    noah "Given enough time and research, we could even use them to travel between two universes."
    lester "Thanks to your help, we’re already able to predict where a storm is going to occur and avoid it.\nA lot of spacegoers owe their lives to you."
    noah_hurm "Whatever, whatever.\nJust keep those sensors running."
    tact "Exploration of parallel universes...\nWe're on the verge of the greatest scientific breakthrough in Transbaal's history."
    noah_thinking "...Hopefully, yes."
    noah "Even once we work out all the physical theory involved, it'll take some time before we have an implementation we can control."
    lester_relaxed "Even so, this is an incredible achievement.\nImagine what kind of things we could find on the other side."
    tact_happy "Yeah.\nLike hot alien babes..."
    lester_stressed "...I hate you."

    scene bg elsior bridge with fadeSlow
    $ location = "Bridge"
    show noah normal at center, dissolveCustom
    noah "Well, storm’s over.\nLet’s gather our probes and leave."
    tact_oneeye "Ahh, how annoying.\nI want to go home already."
    hide noah
    show lester annoyed at center, dissolveCustom
    lester "We’re almost done here.\nYou don’t have to be so impatient."
    hide lester
    if partner == "Vanilla":
        show noah serious at center, dissolveCustom
        noah "If you're anxious to go home and make out with your wife, just say so."
        show noah hurm at dissolveCustom
        noah "Honestly, taking a fourteen-year-old for a bride...\nYou sick perv."
        tact_aggressive "That's not what it's like at all!"
        hide noah
        show lester stressed at center, dissolveCustom
    else:
        show noah hurm at center, dissolveCustom
        if partner == "Chitose":
            noah "If you're anxious to go home and bang your fiancée, just say so."
        else:
            noah "If you're anxious to go home and bang your wife, just say so."
        tact_aggressive "That's not why I..."
        hide noah
        show lester serious at center, dissolveCustom
        lester "..."
        tact_sweating "Maybe a little."
        show lester stressed at dissolveCustom
    lester "Whatever.\nJust keep it off the bridge."
    hide lester
    show noah normal at center, dissolveCustom
    noah "In any case, I’ve got everything I need.\nOnce we're back on the White Moon, I can start analyzing these readings."
    tact "Alright, we're heading back.\nElsior, set a course for Transbaal."
    $ location = None
    scene bg blank with fadeSlow
    stop music fadeout 1

    #go to next
    if partner == "Milfeulle":
        jump ch1_2_milfeulle
    