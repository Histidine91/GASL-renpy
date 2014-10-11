# ==============================
# CHAPTER 1-4
# ==============================
    
label ch1_4:
    scene bg elsior bridge with fade
    play music "music/Ambience - Bridge.ogg"
    $ location = "Bridge"
    coco "Scopes are clear. The First Fleet is one hour out and ready to secure the system."
    tact_oneeye "..."
    show lester serious at center, dissolveCustom
    lester "Tact..."
    play music "music/An Obscure Unease.ogg" 
    tact_oneeye "That feeling just now... was it just my imagination?"
    
    play sound "sfx/comm_open.wav"
    pause 1.5
    $ location = None
    if partner == "Milfeulle" or partner == "Forte" or partner == "Chitose":
        scene cg cockpit milfeulle2
        milfeulle_sad "Tact... I feel sick..."
        tact_oh "Milfie... you felt it too?"
    if partner == "Milfeulle" or partner == "Mint" or partner == "Forte":
        scene cg cockpit forte2
        forte_worried "I think we all did."
    if partner == "Milfeulle" or partner == "Ranpha" or partner == "Vanilla":
        scene cg cockpit ranpha2
        ranpha_sad "I didn't notice anything when the fighters died."
        ranpha_worried "But... when the large ships went down..."
    if partner == "Milfeulle" or partner == "Mint" or partner == "Forte":
        scene cg cockpit forte2
        forte_sad "It was like a thousand screams were silenced all at once."
    if partner == "Milfeulle" or partner == "Ranpha" or partner == "Vanilla":
        scene cg cockpit ranpha2
        ranpha_worried "I don't think I'll be able to sleep tonight..."
    
    $ location = "Bridge"
    scene bg elsior bridge
    tact "Nevertheless, you did well.\nCome on home, everyone."
    if partner == "Milfeulle":
        milfeulle_sad "Yes..."
    elif partner == "Ranpha":
        ranpha_stressed "Roger.\nComing home now..."
    elif partner == "Mint" or partner == "Forte":
        forte_serious "Yes, sir."
    elif partner == "Vanilla" or partner == "Chitose":
        chitose "Yes, sir.\nSharpshooter, returning to the Elsior."
    play sound "sfx/comm_close.wav"
    pause 1
    tact_oneeye "...Lester... what did we do?"
    show lester grim at center, dissolveCustom
    lester "...I'm sorry, but I can't answer that question for you."
    show lester serious at dissolveCustom
    lester "For now, let's return to Transbaal. I'm sure the brass is going to be grilling us about the battle today."
    show lester normal at dissolveCustom
    lester "And try to cheer up.\nThe Angel Wing doesn't need to see you like this."
    tact_oneeye "Sorry."
    tact "Better?"
    show lester relaxed at dissolveCustom
    lester "Better."
    hide lester at dissolveCustom
    tact "Alright, then. Let's head home."
    
    $ location = None
    scene bg blank with fade
    tact_oneeye "A hostile alien fleet in Transbaal...\nAre we on the brink of yet another war?"
    
    scene bg blank with fade
    call intermission
    
    scene bg whitemoon hallway with fadeSlow
    play music "music/Ambience - Whirr.ogg"
    $ location = "Hallway"
    tact_stressed "Ahhh, what a pain.\nI thought I was going to go into a coma."
    show lester serious at center, dissolveCustom
    lester "You need to be more professional, Tact.\nWhat do you think it looks like when the CO of the elite Angel Wing spaces out during meetings?"
    tact_oneeye "You don't seem to particularly miss it yourself, Lester."
    show lester grim at dissolveCustom
    lester "...Goddamn intel pukes..."
    tact_oh "Huh...\nLester, didn't you come up the intel track yourself?"
    show lester relaxed at dissolveCustom
    lester "Sure, but I've seen what the action is like.\nI'm not some REMF like those clowns ONI foisted off on us."
    tact_oneeye "Action, huh..."
    show lester serious at dissolveCustom
    lester "Bah. Just because we've won one engagement with the mystery aliens from nowhere, they seem to think we're clairvoyant or something."
    tact "Well, we're one of the few units that actually had any contact with them. I'm sure the Navy is desperate for any credible information it can get on them."
    lester "Fair enough."
    show lester grim at dissolveCustom
    lester "In fact, considering how chilling the intel we do have is, I can't say I really blame them."
    tact_oneeye "It's that bad, huh..."
    show lester serious at dissolveCustom
    lester "You've seen the reports.\nTransbaal is still recovering from three consecutive wars in the span of less than a year..."
    lester "...and the requirements for occupation of the Val-Fasc systems has stretched the Navy even thinner. We're hopelessly spread out, and now this."
    lester "Alien ships no-one has ever seen before, that can travel light-years in the blink of an eye... This is precisely the sort of scenario calculated to give strategic defense planners nightmares."
    tact_oneeye "It's going to get worse, too.\nWe can't keep sitting on the reports of all the attacks on civilian shipping forever, and when the public figures out just how bad things are..."
    tact_stressed "And of course, we're going to be the ones fixing it.\nAaaahh, not a day of rest..."
    show lester relaxed at dissolveCustom
    lester "You should be used to it by now.\nBuckle up, Hero of the Empire."
    tact "Well, anyway, none of us can really do anything until we have more information.\nLet's just try to relax for now."
    show lester serious at dissolveCustom
    lester "Why am I not surprised that you're saying something like that?"
    show lester normal at dissolveCustom
    lester "...Well, I suppose you're right. We'll just have to wait and see."
    
    
    hide lester with dissolve
    play sound "sfx/footsteps.wav"
    tact_oh "Hmm? Someone's coming down this way?"
    #play sound "sfx/footsteps_approach.wav"
    show shiva normal at midleft, dissolveCustom
    shiva "Meyers."
    play music "music/Shiva.ogg"
    tact_surprised "Lady Shiva?!\n...What are you doing here?"
    show luft normal at midright, dissolveCustom
    luft "Tact! Lester!\nI see you finally got away from that endless meeting."
    hide shiva
    hide luft
    show lester aggressive at center, dissolveCustom
    lester "Your Majesty! Admiral Luft!"
    hide lester with dissolveFast
    show shiva thinking at midleft, dissolveCustom
    shiva "Luft has briefed me on the situation.\nIt would seem my reign is condemned to be a long string of military crises."
    tact_sweating "Don't say that, Lady Shiva...\nI'm sure everything will turn out fine in the end.\nRight, Lester?"
    hide shiva
    show lester serious at center, dissolveCustom
    lester "W-Why are you asking me?!"
    hide lester
    show shiva normal at center, dissolveCustom
    shiva "Optimistic as ever, Meyers..."
    show shiva happy at dissolveCustom
    shiva "But perhaps that is what is most endearing about you."
    shiva "In any case, I have to thank you and the Angel Wing for your superb handling of the previous battle."
    show shiva veryhappy at dissolveCustom
    shiva "Your efforts may well have saved countless Navy and civilian lives... and the White Moon.\nYou have Transbaal's gratitude once more."
    tact "It was but our duty, Lady Shiva."
    hide shiva
    show lester relaxed at midright, dissolveCustom
    lester "(How unusually modest of you...)"
    tact_oneeye "(Oh, shush.)"
    hide lester
    show shiva serious at center, dissolveCustom
    shiva "In any case, it seems we will be calling on your services again in the near future. I can only pray that this new crisis will be brief."
    hide shiva
    show luft thinking at center, dissolveCustom
    luft "The Angel Wing remains our strongest force... and at the moment, it's the only real strategic reserve we've got."
    show luft serious at dissolveCustom
    luft "We need to cover over a hundred inhabited systems at once, and we don't dare uncover Transbaal or the Core Worlds any further than we already have. If the enemy shows up again, in greater force..."
    tact_sweating "Seems like we're going to be working eighteen-hour days again..."
    hide luft
    show lester relaxed at center, dissolveCustom
    lester "Quit your whining.\nYou've still got it way better than Admiral Luft here."
    hide lester
    show luft amused at center, dissolveCustom
    luft "Ahahahaha!\nToo true, Lester, too true."
    show luft thinking at dissolveCustom
    luft "Honestly, civilian head of government {i}and{/i} Chief of Naval Operations? I still don't know why I let Her Majesty convince me this was a good idea..."
    hide luft
    show shiva happy at center, dissolveCustom
    shiva "No two people could have done a better job than you have, Luft.\nI do not know where we'd be without you."  
    shiva "If there's anyone else in the Empire I trust more to see us through this new danger, I have yet to meet them."
    hide shiva
    show luft normal at center, dissolveCustom
    luft "I'll do my best to live up to your expectations again, Your Majesty."
    hide luft
    show shiva happy at center, dissolveCustom
    shiva "Indeed?\nIn that case, should we not get started right away."
    hide shiva
    show luft amused at center, dissolveCustom
    luft "Haha!\nAs you command, Your Majesty."
    hide luft
    show shiva normal at center, dissolveCustom
    shiva "You too, Meyers. I am counting on you."
    tact "Of course, Lady Shiva."
    
    $ location = None
    scene bg blank with fadeSlow
    scene bg elsior bridge with fadeSlow
    $ location = "Bridge"
    play music "music/Elsior.ogg"
    tact "Morning, everyone."
    show lester normal at center, dissolveCustom
    lester "Mm.\nYou're up early today."
    show lester relaxed with dissolveFast
    lester "I guess Her Majesty is one of the few people who can actually motivate you to work."
    hide lester
    show almo happy at midleft, dissolveCustom
    almo "Normally, XO Coolduras has to resort to beatings to get Commander Meyers to take his duties seriously."
    show coco happy at midright, dissolveCustom
    coco "I guess we can skip the thumbscrews today, eh, Almo?"
    tact_sweating "Harsh..."
    tact "Anyway, has anything happened during my break?"
    show almo normal at dissolveCustom
    almo "Nothing out of the ordinary here.\nJust the usual comm traffic."
    show coco normal at dissolveCustom
    coco "We've got a bunch of civilian ships running around, but no sign of the hostiles."
    hide almo
    hide coco
    show lester serious at center, dissolveCustom
    lester "Although the reports of combat just keep trickling in...\nAt least the frequency of encounters seems to be easing off a little."
    tact_oneeye "Yeah, but we're still out here because of a cruiser lost with all hands."
    tact_oneeye "Also, a merchant skipper claims to have sighted a Val-Fasc ship...\nIs something happening out there?"
    lester "Rather unlikely.\nThe last report from Governor Tiptree and Admiral Laumer was that almost all organized resistance had been suppressed."
    show lester relaxed at dissolveCustom
    lester "Besides, we're on the opposite end of the Empire from Val-Vaross. There's absolutely no reason for any insurgents to be operating all the way over here."
    show lester normal at dissolveCustom
    lester "It's probably just a straggler from Nephelia's invasion. We'll need to deal with it eventually, but it's not a long-term danger."
    tact "Maybe you're right."
    tact_serious "Even so, we can't let our guard down.\nI want a..."
    hide lester at dissolveCustom
    
    stop music fadeout 1
    play sound "sfx/alarm.wav"
    pause 3
    play music "music/Ambience - Bridge.ogg"
    
    show coco shocked at midright, dissolveCustom
    coco "Commander Meyers! Emergency!"
    tact_surprised "Coco! What is it?"
    coco "Unidentified alien fleet has appeared dead ahead of us!\nThere's thirty - no, forty of them!"
    tact_aggressive "?! So that's what happened to the Herschel?"
    show coco surprised at dissolveCustom
    coco "They're different from the ones we've seen before.\nCIC's still trying to refine our data..."
    hide coco
    show lester aggressive at center, dissolveCustom
    lester "All hands, general quarters!\nPrepare to scramble the Angel Wing!"
    #hide lester with dissolveFast
    #show coco normal at midright with dissolveFast
    tact_serious "Coco, hostile movement patterns?"
    coco "They're on an intercept vector. Range 20 k-klicks and closing..."
    coco_shocked "Oh my god! Now there's {i}two{/i} fleets in front of us!\nAnd this one's huge!"
    tact_aggressive "What?!"
    #show lester aggressive at dissolveCustom
    lester "Damn it all... did the maintenance techs install an alien attractor on our ship during the last refit cycle or something?"
    hide lester
    show almo shocked at midleft, dissolveCustom
    almo "T-This is no time for jokes, sir!"
    tact_oneeye "If they're both hostile, we're going to be in a lot of trouble..."
    
    hide almo at dissolveCustom
    coco "Wait, the first fleet is turning around..."
    coco_shocked "It's opening fire on the second!"
    tact_oh "Whoa, what?"
    almo_surprised "It seems the two fleets differ from each other as well as the one we encountered at Transbaal..."
    show lester serious at center, dissolveCustom
    lester "Looks like we're dealing with at least two alien factions here. Maybe three."
    tact_serious "And half to two thirds of them are openly attacking us.\nThe remainder, at least, seem to be the enemy of our enemy..."
    show lester grim at dissolveCustom
    lester "...is my enemy's enemy. No more. No less."
    tact_oneeye "True..."
    tact "We'll play it by ear.\nLet's wait and see if they're ready to parley... and be prepared to run if they're not."
    hide lester at dissolveCustom
    almo "Contact Alpha has taken thirty percent losses and climbing. The survivors are retreating..."
    coco_surprised "...Whoa. They've just... vanished..."
    tact_oh "Vanished...?\nIs it some kind of stealth system?"
    coco "I don't think so.\nThere's no trace of them at all... it's like they just left the system completely in an instant."
    lester_serious "...and Contact Beta?"
    coco "They're moving into a... wedge formation, but they're not closing."
    show almo surprised at midleft, dissolveCustom
    almo "Commander! We're picking up an electromagnetic signature from the alien fleet... It has characteristics consistent with a communications signal!"
    tact_oh "Communications...\nAre they trying to hail us?" 
    tact_serious "Almo, establish first contact comm protocols!"
    almo "Yes, sir!"
    hide almo
    hide coco
    show lester serious at center, dissolveCustom
    lester "Trying to talk?\nWell, that's a change, alright..."
    tact_oneeye "It's probably just as well, considering the tonnage disparity we're looking at..."
    tact_serious "Lester, I want you to chart a navigation route if we have to run for it. I hope these guys are friendly, but we're not going to bet our lives on it."
    show lester relaxed at dissolveCustom
    lester "Already done."
    hide lester at dissolveCustom
    almo "Handshake complete. Beginning two-way transmission now."
    
    # TO BE CONTINUED
    $ location = None
    scene bg blank with fadeSlow
    "TO BE CONTINUED..."
    
    
    # ==============================
    # old scene version
    
    #alarm!
    #play sound "sfx/alarm.wav"
    #pause 2
    #tact_oh "What's going on?"
    #play sound "sfx/comm_open.wav"
    #show luft serious with dissolveFast
    #luft "Luft, here. Why is the general quarters alarm sounding?"
    #show luft aggressive with dissolveFast
    #luft "What?\nGot it. I'll be there."
    #play sound "sfx/comm_close.wav"
    #hide luft
    #show lester serious with dissolveFast
    #lester "What's the matter, Admiral?"
    #hide lester
    #show luft serious with dissolveFast
    #luft "...Another alien fleet is in-system.\nIt's much larger than any previously reported."
    #hide luft
    #show lester aggressive with dissolveFast
    #lester "...!"
    #hide lester
    #show luft serious at midright with dissolveFast
    #luft "Your Majesty. Tact. Lester.\nPlease come with me."
    #show shiva serious at midleft with dissolveFast
    #shiva "...Yes.\nLead the way, Luft."
    #play sound "sfx/footsteps_running.wav"
    #$ location = None
    
    #scene bg conferenceroom with fade
    #$ location = "Conference Room"
    #show luft aggressive with dissolveFast
    #luft "Ops, what's the situation?"
    
    
    