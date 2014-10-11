# ==============================
# CHAPTER 1-3 (Pre Battle 1)
# ==============================
image cg ch1 neinzulattack = im.Scale("cg/ch1_neinzul_attack.png", 630, 360)
image cg tutorial adv1 = "cg/advtutorial_1.png"
image cg tutorial adv2 = "cg/advtutorial_2.png"
image cg tutorial adv3 = "cg/advtutorial_3.png"

label ch1_3:
    play sound "sfx/door_open.wav"
    scene bg elsior bridge with wiperight
    $ location = "Bridge"
    play music "music/Bridge.ogg"
    tact_serious "Status?"
    show coco normal at midright, dissolveCustom
    coco "We have a number of large ships accompanied by many smaller ones.\nPutting up on screen now."
    hide coco
    
    show screen infopanel("cg ch1 neinzulattack")
    play music "music/Omen.ogg"
    tact_serious "Aliens, huh..."
    lester_serious "It's hard to believe, even now... but there's nothing like those ships anywhere we know of."
    tact_serious "How far out are they?"
    #show almo normal at midleft with dissolveFast
    coco "They're about 15,000 klicks out; least-time intercept in twenty minutes."
    almo "We've tried hailing them, but no response so far."
    tact_oneeye "Do they even use the same communication protocols we do?"
    
    hide screen infopanel 
    #with dissolve
    show lester serious at center, dissolveCustom
    lester "The Navy detachment in orbit sent out a squadron to intercept and examine the alien fleet. The x-rays opened fire and took out a destroyer; the other ships pulled back."
    tact_oneeye "So we can safely assume they're hostile."
    show lester grim at dissolveCustom
    lester "Lethal force... awful way to make first contact."
    hide lester at dissolveCustom
    show almo normal at midleft, dissolveCustom
    almo "Um... are we going to war again?"
    tact_oneeye "Hard to say.\nFor now, let's focus on the situation in front of us."
    hide almo with dissolveFast
    show lester serious at center, dissolveCustom
    lester "Most of the fleet is performing exercises on the other side of the system. They're heading back right now, but for now we're the only ones on point."
    tact "So, we're the first responders then."
    lester "They caught us while we were doing refit on the Emblem Frames... We've only got half the Angel Wing actually ready to sortie. This could be dangerous."
    tact "Even at half strength, we're still the most powerful fighting force in the known galaxy.\nWe're not going to back down from a fight."
    hide lester at dissolveCustom
    tact "Almo, patch me through to the Angel Wing."
    almo "Yes, sir."
    
    play sound "sfx/comm_open.wav"
    tact "This is Tact.\nAngel Wing, what's your status?"
    if partner == "Milfeulle" or partner == "Forte" or partner == "Chitose":
        milfeulle "Lucky Star, all systems green."
    if partner == "Milfeulle" or partner == "Ranpha" or partner == "Vanilla":
        ranpha_serious "Kung-fu Fighter, ready for action."
    if partner == "Ranpha" or partner == "Mint" or partner == "Chitose":
        mint "Trick Master here.\nJust say they word."
    if partner == "Milfeulle" or partner == "Mint" or partner == "Forte":
        forte "Happy Trigger, guns are hot."
    if partner == "Ranpha" or partner == "Forte" or partner == "Vanilla":
        vanilla "Harvester is ready to deploy."
    if partner == "Mint" or partner == "Vanilla" or partner == "Chitose":
        chitose "Sharpshooter, awaiting takeoff clearance."
        
    tact "Alright.\nListen up, everyone..."
    play music "music/Time to Fight.ogg"
    tact_serious "There's an alien fleet out there, right on our doorstep."
    tact_serious "We don't know who they are, where they're from, or what they want."
    tact_serious "Regardless of the situation we find ourselves in, however, one thing is clear: it's up to us to stop them before anyone else dies."
    if partner == "Milfeulle" or partner == "Forte" or partner == "Chitose":
        milfeulle_happy "Don't worry, Tact!\nWe won't let them hurt anyone else!"
    if partner == "Milfeulle" or partner == "Ranpha" or partner == "Vanilla":
        ranpha_aggressive "If those aliens think they can show up at our home and walk all over us, they'd better think again!"
    if partner == "Ranpha" or partner == "Mint" or partner == "Chitose":
        mint_angry "Indeed. We shall not let them walk all over us."
    if partner == "Milfeulle" or partner == "Mint" or partner == "Forte":
        forte_serious "Whoever they are, we can't let them run roughshod over the Empire and its people."
    if partner == "Ranpha" or partner == "Forte" or partner == "Vanilla":
        vanilla "We must defend the people of Transbaal..."
    if partner == "Mint" or partner == "Vanilla" or partner == "Chitose":
        chitose_annoyed "So long as I draw breath, those who would hurt the innocent shall find no rest!"
        
    tact "Thank you, everyone."
    tact_serious "All units, prepare for action."
    
    $ location = None
    scene bg blank with fade
    call intermission
    
    play music "music/Briefing.ogg"
    scene bg elsior bridge with fadeSlow
    $ location = "Bridge"
    show lester serious at center, dissolveCustom
    lester "Before we begin, Tact.\nYou've been keeping up your command training, haven't you?"
    tact_serious "Of course I have!"
    show lester grim at dissolveCustom
    lester "Really? Including familiarization with the latest evaluations of the Emblem Frames' characteristics?"
    menu:
        tact_sweating "Well..."
        "I could use a refresher.":
            tact_happy "Actually, could you give me a quick refresher course?"
            show lester stressed at dissolveCustom
            lester "What, you think we have time to write a tutorial just for you?\nWait for the full version."
            tact_oneeye "Tch. Fine."
        "Just run me through the new stuff.":
            tact "Just give me a quick review of the new features.\nI think I can handle the rest."
            show lester serious at dissolveCustom
            lester "...Fine."
            call tutorial_2
        "I'm good, thanks.":
            tact "Don't worry, I got it."
            show lester amused at dissolveCustom
            lester "Excellent. It seems you've finally learned something after all this time."
            
    hide lester at dissolveCustom
    tact "Almo, tactical view on main screen."
    almo "Yes, sir."
    jump ch1_3_briefing

label ch1_3_briefing:
    show screen tactical_map(None, unitLists["mission1_milfeulle"], unitTypeLists["mission1_milfeulle"], battleLocations["mission1_milfeulle"])
    lester_serious "This is the present situation."
    $ mapHighlightUnit = "elsior"
    show reticule blue at definePos(0.54, 0.58), zoomIn(4, 0.6) onlayer abovescreen
    lester_serious "The Elsior's current position is here."
    $ mapHighlightUnit = None
    hide reticule onlayer abovescreen
    
    lester_serious "We have three types of ship in the enemy formation.\nIntel on them is virtually nonexistent, but NavInt has put together some... educated guesses based on previously reported encounters with the alien ships."
    show screen unitinfo("unitpic yngcommando", "<unknown-1>", "Alien Fighter")
    $ mapHighlightUnit = "yngcommando"
    lester_serious "First is this small ship.\nIt appears to be a lightning fast fighter, lightly armed and armored."
    hide screen unitinfo 
    #with dissolveExtraFast
    
    show screen unitinfo("unitpic yngtiger", "<unknown-2>", "Alien Bomber")
    $ mapHighlightUnit = "yngtiger"
    lester_serious "This is another fighter-sized vessel.\nIntel suggests it's an attack bomber of some sort; might want to keep the Elsior away from it."
    hide screen unitinfo 
    #with dissolveExtraFast
    
    show screen unitinfo("unitpic enclavestar", "<unknown-3>", "Alien Mothership")
    $ mapHighlightUnit = "enclavestar"
    lester_serious "Lastly, we have these... odd-looking large ships here.\nThey appear to serve as carriers for the small vessels."
    lester_serious "It doesn't appear to have much armament or defense of its own, but it may have other tricks up its sleeve.\nBe careful."
    hide screen unitinfo 
    #with dissolveExtraFast
    $ mapHighlightUnit = None
    
    # draw arrows
    tact_oneeye "Looks like our plan is simple then.\nAngels, pick your targets, and sweep up the enemy task force. The Elsior will support as needed."
    tact_serious "I'm counting on you, everyone."
    hide screen tactical_map 
    with dissolveFast
    
    nvl clear
    nvl show dissolveFast
    nvlChar "{b}Enemy Units{/b}\n
    UNK-F x 6{space=72}UNK-B x 4\n
    UNK-CV x 2\n
    \n
    {b}Victory Conditions{/b}\n
    Destroy all enemies\n
    \n
    {b}Defeat Conditions{/b}\n
    Elsior destroyed"
    nvl hide dissolveExtraFast

    show lester serious at center, dissolveCustom
    menu:
        lester "Would you like to go over the plan one more time?"
        "Let's review it.":
            tact "Yeah, let's review it just to be sure."
            hide lester at dissolveCustom
            jump ch1_3_briefing
        "There's no need.":
            hide lester at dissolveCustom
            tact_serious "No, there's no need.\nIs everyone ready?"
            tact_aggressive "Angel Wing, engage!"
            all "Yes, sir!"

    call run_spring("mission1_milfeulle")
    $renpy.block_rollback()
    if _return == 0:
        jump gameOver
    elif _return == -1:
        return
    
    jump ch1_4
    
label tutorial_1:
    # TODO
    $ print("bla")
    
label tutorial_2:
    while True:
        $ location = None
        scene cg tutorial adv1 with dissolve
        lester_serious "The first thing you need to know about is {b}suppression{/b}."
        lester_serious "I don't think I need to tell you this, but people tend to perform better when they're not being shot at."
        lester "If one of our Angels is shot at by an enemy on her six while she's engaging someone else, she's going to lose effectiveness. This is {i}suppression{/i}, which reduces the affected unit's rate of fire and accuracy."
        lester_relaxed "Of course, it depends on the Angel's morale as well.\nIf she's feeling on top of the world, no amount of incoming fire will faze her."
        lester_serious "Suppression decays on its own if the shooting stops for a while. If one of our Angels comes under fire and gets pinned down, have one of her wing mates come to her aid and take some of the heat off."
        
        scene cg tutorial adv2 with dissolve
        lester_serious "Next is {b}armor penetration{/b}."
        lester_relaxed "As you'll know if you ever tried to sink a cruiser with a BB gun, low-power shots against heavy armor aren't going to do you any good."
        lester_serious "If a kinetic weapon has less armor penetration than a target's armor, its damage will be reduced proportionally.\nConversely, if the armor penetration equals or exceeds the target's armor, the weapon does full damage."
        lester "Energy weapons interact with armor in a similar, but slightly different fashion.\nConsult the manual for full details."
        lester_serious "What this means in practice is target selection. Light, low-penetration weapons are most effective against fighters and other soft targets, while a heavy weapon is best used against heavily-armored enemies."
        
        scene cg tutorial adv3 with dissolve
        lester_serious "Lastly, we have {b}special abilities{/b}."
        lester_serious "Using knowledge gained during the previous wars, we have been able to modify the Emblem Frames with a number of active abilities, which can be used during a battle."
        lester "Each Emblem Frame has two unique abilities, which can augment its strengths or support allies.\nUsing abilities costs energy, and both abilities have a shared cooldown."
        lester_serious "Unfortunately we haven't had time to install the new systems on the Emblem Frames yet, but they should be usable in subsequent battles."
        
        scene bg elsior bridge with dissolve
        $ location = "Bridge"
        show lester serious at center, dissolveCustom
        menu:
            lester "Would you like me to repeat that one more time?"
            "Yes, please.":
                tact "Yes, please.\nI want to make sure I got it all."
                show lester stressed at dissolveCustom
                lester "Sigh... fine."
            "I got it, thanks.":
                tact "I'm good, thanks."
                show lester amused at dissolveCustom
                lester "Good to hear.\nIt seems your skull isn't impermeable after all."
                return