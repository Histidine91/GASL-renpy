# ==============================
# PROLOGUE
# ==============================
init 1:
    image cg prologue transbaal = im.Scale("cg/prologue_transbaal.png", SCREENSIZE_X, SCREENSIZE_Y)
    image cg prologue ga1 eonia = im.Scale("cg/prologue_ga1_eonia.png", SCREENSIZE_X, SCREENSIZE_Y)
    image cg prologue ga1 blackmoon = im.Scale("cg/prologue_ga1_blackmoon.png", SCREENSIZE_X, SCREENSIZE_Y)
    image cg prologue ga1 angels = im.Scale("cg/prologue_ga1_angels.png", SCREENSIZE_X, SCREENSIZE_Y)
    image cg prologue ga1 victory = im.Scale("cg/prologue_ga1_victory.png", SCREENSIZE_X, SCREENSIZE_Y)
    image cg prologue ml nephelia = im.Scale("cg/prologue_ml_ogaub.png", SCREENSIZE_X, SCREENSIZE_Y)    #FIXME
    image cg prologue ml ogaub = im.Scale("cg/prologue_ml_ogaub.png", SCREENSIZE_X, SCREENSIZE_Y)
    image cg prologue ml finalweapon1 = im.Scale("cg/prologue_ml_finalweapon1.png", SCREENSIZE_X, SCREENSIZE_Y)  
    image cg prologue ml finalweapon2 = im.Scale("cg/prologue_ml_finalweapon2.png", SCREENSIZE_X, SCREENSIZE_Y)
    image cg prologue el gern = im.Scale("cg/prologue_el_gern.png", SCREENSIZE_X, SCREENSIZE_Y)
    image cg prologue el eden = im.Scale("cg/prologue_el_eden.png", SCREENSIZE_X, SCREENSIZE_Y)  
    image cg prologue el chronoquakebomb = im.Scale("cg/prologue_el_chronoquakebomb.png", SCREENSIZE_X, SCREENSIZE_Y)
    image cg prologue el homecoming = im.Scale("cg/prologue_el_homecoming.png", SCREENSIZE_X, SCREENSIZE_Y)
    image cg prologue partnerselect = im.Scale("cg/prologue_partnerselect.png", SCREENSIZE_X, SCREENSIZE_Y)
    image cg prologue milfeulle = im.Scale("cg/prologue_milfeulle_sandhouse.png", SCREENSIZE_X, SCREENSIZE_Y)
    image cg prologue ranpha = im.Scale("cg/prologue_ranpha_fountain.png", SCREENSIZE_X, SCREENSIZE_Y)
    image cg prologue mint = im.Scale("cg/prologue_mint_park.png", SCREENSIZE_X, SCREENSIZE_Y)
    image cg prologue forte = im.Scale("cg/prologue_forte_dine.png", SCREENSIZE_X, SCREENSIZE_Y)
    image cg prologue vanilla = im.Scale("cg/prologue_vanilla_park.png", SCREENSIZE_X, SCREENSIZE_Y)
    image cg prologue chitose = im.Scale("cg/prologue_chitose_fountain.png", SCREENSIZE_X, SCREENSIZE_Y)
    
screen imagemap_prologue_partnerselect:
    imagemap:
        alpha False
        ground "bg clear"

        hotspot (100, 50, 230, 300) action Return("Ranpha")
        hotspot (430, 50, 230, 300) action Return("Milfeulle")
        hotspot (720, 50, 230, 300) action Return("Vanilla")
        hotspot (100, 450, 230, 300) action Return("Mint")
        hotspot (430, 450, 230, 300) action Return("Chitose")
        hotspot (720, 450, 230, 300) action Return("Forte")

label prologue:
    #play music "music/Reminiscence.ogg"
    #scene cg prologue transbaal with Fade(1,1,1)
    #tact "It has been 434 years since the Chrono Quake that led to the collapse of galactic civilization."
    #tact "From the ashes rose the Transbaal Empire, which is today a peaceful and prosperous union of over a hundred worlds under the protection of the White Moon."
    #tact "But that fragile peace was disturbed many times in recent history."
    
    #scene cg prologue ga1 eonia with dissolve
    #tact "A year and a half ago, the exiled Prince Eonia launched an invasion of Transbaal with an armada of automated ships, in a bid to usurp the throne."
    #scene cg prologue ga1 blackmoon with dissolve
    #tact "He was accompanied by the Black Moon, a rogue manifestation of Lost Technology designed as a weapon of unparalleled destructive capability."
    #scene cg prologue ga1 angels with dissolve
    #tact "Opposing Eonia and the Black Moon were the Moon Angel Wing, the bravest and strongest-hearted young women in the galaxy."
    #tact "We fought side by side, working together to save the people of the Empire. And in the end..."
    #scene cg prologue ga1 victory with dissolve
    #tact "...The Black Moon was destroyed, and peace returned to Transbaal."
    
    #scene cg prologue ml nephelia with fade
    #tact "But six months later, a new threat emerged."
    #tact "Nephelia, an agent of the ancient Val-Fasc alien civilization, recovered the ruins of the Black Moon and started an insurrection in Transbaal."
    #scene cg prologue ml ogaub with dissolve
    #tact "She used the Black Moon's technology to construct the O-Gaub, a supercarrier that proved invulnerable to even our strongest weapons."
    #tact "With our backs to the wall, we joined forces with Noah, the former administrator of the Black Moon."
    #scene cg prologue ml finalweapon1 with dissolve
    #tact "It was Noah who devised the Final Weapon, a dagger to pierce the heart of the O-Gaub and destroy it forever.
    #      Only the strongest of the Angels could pilot it."
    #scene cg prologue ml finalweapon2 with dissolve
    #tact "I went with her, and though it nearly cost us our lives, we defeated the menace and saved the Empire once more."
    #tact "But the fight was not over."
    
    #scene cg prologue el gern with fade
    #tact "The Val-Fasc were still out there, lead by the warlord King Gern."
    #tact "Having conquered our ancestral civilization of Eden six hundred years ago, they now set their sights on Transbaal."
    #scene cg prologue el eden with dissolve
    #tact "But with the Angel Wing leading the way, we fought back, and successfully liberated Eden, the land of our forefathers."
    #tact "The time had come to defeat the Val-Fasc and bring peace to the galaxy once and for all."
    #scene cg prologue el chronoquakebomb with dissolve
    #tact "The Val-Fasc unleashed their ultimate weapon, the Chrono Quake Bomb, in their attempt to lay waste to the galaxy a second time."
    #tact "Once again, I rode with her into the heart of danger, and together we prevented the ultimate calamity from befalling the galaxy."
    #tact "But in the process, we found ourselves stranded in a pocket alternate universe, just the two of us..."
    #scene cg prologue el homecoming with dissolve
    #tact "...until our friends came for us, and we could return home together."
    #tact "Yes.\nThe love of my life..."
    
    play music "music/Reminiscence.ogg" fadeout 0
    scene cg prologue transbaal with Fade(1,1,1)
    tact "It has been 434 years since the Chrono Quake, the catastrophe that led to the collapse of galactic civilization."
    tact "From the ashes rose the Transbaal Empire, which is today a peaceful and prosperous union of over a hundred worlds under the protection of the White Moon."
    tact "But that fragile peace was disturbed many times in recent history."
    
    scene cg prologue ga1 blackmoon with dissolve
    tact_serious "First was the exiled Prince Eonia, who attempted to usurp the throne with the help of the ancient superweapon, the Black Moon."
    scene cg prologue ml ogaub with dissolve
    tact_serious "Then came Nephelia, agent of the alien civilization known as the Val-Fasc, who built an almighty ship from the remains of the Black Moon and tried to seize Transbaal."
    scene cg prologue el gern with fade
    tact_serious "Though her efforts were thwarted, the Val-Fasc declared war on Transbaal. Under the rule of the warlord King Gern, they attempted to add us to their long list of conquests."
    scene cg prologue ga1 angels with dissolve
    tact "Opposing these foes were the Moon Angel Wing, the bravest and strongest-hearted young women in the galaxy."
    tact "We fought side by side, working together to save the people of the Empire and the galaxy."
    tact "No matter the foe, no matter the danger, we were always there as one..."
    
    stop music fadeout 1
    scene bg elsior tealounge with Fade(0.5,1,0.5)
    $ location = "Lounge"
    play music "music/The Angel Wing Appears.ogg"
    
    show milfeulle happy at midleftNoAnchor, dissolveCustom
    milfeulle "Tact, would you like some more cake?"
    tact "Sure, Milfie. Thanks."
    show ranpha furious at midright, dissolveCustom
    ranpha "Oi, Milfie! Don’t give him all the cake!\nI want some too!"
    show milfeulle veryhappy at dissolveCustom
    milfeulle "Now, now. I made plenty for everyone.\nThere's no need to fight."
    show ranpha annoyed at midright, dissolveCustom
    ranpha "Really?\nThen why is it smaller every time I turn around?"
    
    $ location = None
    scene bg blank with fade
    show milfeulle normal at center, dissolveCustom
    tact "This is Milfeulle Sakuraba. She pilots the GA-001, the Lucky Star."
    tact "A cheery girl blessed with extreme luck, both good and bad, she loves nothing more than cooking and baking."
    scene bg blank with fade
    show ranpha normal at center, dissolveCustom
    tact "And this is Ranpha Franboise, pilot of the GA-002 Kung-fu Fighter."
    tact "She’s a martial artist with a fiery personality, but she’s also a hopeless romantic."
    
    scene bg elsior tealounge with fade
    $ location = "Lounge"
    show forte calm at midleft, dissolveCustom
    forte "Calm down, Ranpha.\nWe’re here to relax."
    show mint elegant at midright, dissolveCustom
    mint "That’s right.\nWe finally got away from all those celebrations, so let’s enjoy ourselves, shall we?"
    show forte happy at dissolveCustom
    forte "Besides, Tact’s the star of the party.\nI think he can have an extra helping of cake."
    show mint veryhappy at dissolveCustom
    mint "As long as he first bribes us appropriately, of course."

    $ location = None
    scene bg blank with fade
    show mint normal at center, dissolveCustom
    tact "Mint Blancmanche, telepath and heiress to the powerful Blancmanche Corporation. She pilots the GA-003, the Trick Master."
    tact "She combines the grace of a refined lady with a childlike passion for the fun things in life. Her cute appearance belies a keen mind."
    scene bg blank with fade
    show forte normal at center, dissolveCustom
    tact "Forte Stollen, the Angels’ wing leader and pilot of the Happy Trigger, GA-004."
    tact "Her calm command has brought us victory against the odds many times. She’s also an avid gun collector."

    scene bg elsior tealounge with fade
    $ location = "Lounge"
    show chitose veryhappy at midright, dissolveCustom
    chitose "This is the best orange juice I've ever had.\nI must write it down in my diary."
    show vanilla normal at midleft, dissolveCustom
    vanilla "Chitose... you have already exceeded your recommended daily sugar intake..."
    show chitose shocked at dissolveCustom
    chitose "Ehh?! Really?"
    hide vanilla
    show ranpha relaxed at midleft, dissolveCustom
    ranpha "Now, now, Chitose. We’re having a party.\nThere’s no need to worry about little things like this."
    hide chitose
    show mint veryhappy at midright, dissolveCustom
    mint "This is a time for fun and merriment.\nNo need to hold back."
    hide ranpha
    hide mint
    show chitose startled at center, dissolveCustom
    chitose "Y-Yes."

    $ location = None
    scene bg blank with fade
    show vanilla normal at center, dissolveCustom
    tact "Vanilla H, nanomachine user. She pilots the GA-005, the Harvester."
    tact "Beneath her aloof exterior lies boundless empathy for others. A healer by profession, she also likes to play with animals."
    scene bg blank with fade
    show chitose smallsmile at center, dissolveCustom
    tact "And finally, Karasuma Chitose. The newest member of the Angel Wing, she pilots the GA-006 Sharp Shooter."
    tact "A keen student, she was selected to join the Angels based on her academy record. Though her straightlaced nature made it hard for her to fit in at first, she’s now an integral member of the Angel Wing."

    scene bg elsior tealounge with fade
    $ location = "Lounge"
    show forte concerned at midleft, dissolveCustom
    forte "I’m just glad we managed to get away.\nHonestly. It seemed like there was no end to those celebrations."
    show vanilla normal at midright, dissolveCustom
    vanilla "Because Tact came back..."
    hide forte
    show ranpha relaxed at midleft, dissolveCustom
    ranpha "Well, it's no surprise.\nHe’s the hero of the galaxy, after all."
    tact_amused "Please don't.\nIt's bad enough hearing it from every reporter and government official in the Empire."
    hide vanilla
    show chitose happy at midright, dissolveCustom
    chitose "Not at all, Tact.\nEverything we've accomplished, we owe to your peerless leadership and command."
    hide ranpha
    show forte veryhappy at midleft, dissolveCustom
    forte "We’re complimenting you for a change, so just shut up and accept it already, Mr. Commander."
    hide chitose
    hide forte
    show milfeulle veryhappy at center, dissolveCustom
    milfeulle "Everyone’s together again.\nI’m so happy!"
    tact_sweating "You guys..."
    tact_happy "But yeah, it feels great to be back!"
    hide milfeulle
    show mint elegant at midleft, dissolveCustom
    mint "Great enough to buy us another round of drinks?"
    show ranpha veryhappy at midright, dissolveCustom
    ranpha "And after that, take us shopping!\nDesigner stores, here I come!"
    tact_sweating "...Wait a minute.\nIsn’t this supposed to be a party for {i}me{/i}?"
    show ranpha annoyed at dissolveCustom
    ranpha "What's with you?\nA man should be grateful for the oppurtunity to treat a group of beautiful girls."
    hide mint
    show forte veryhappy at midleft, dissolveCustom
    forte "Ahahahaha!\nAs the commanding officer, Tact, you're supposed give your subordinates goodies. You should know this by now."
    hide ranpha
    show vanilla happy2 at midright, dissolveCustom
    vanilla "He who stands atop greatness shalt spread his blessings around..."
    hide forte
    show chitose veryhappy at midleft, dissolveCustom
    chitose "Indeed.\nThat is the way of a great hero."
    tact_crying "Maybe I should’ve stayed in Another Space..."
    tact "(But that’s just like them.\nThey may be the stars of the galaxy, but deep down inside they just enjoy being ordinary girls.)"
    stop music fadeout 1
    
    $ location = None
    scene bg blank with fade
    play music "music/Reminiscence.ogg"
    tact "Especially her."
    tact "We rode into the heart of danger twice together, risking our lives for our friends, for the people of the Empire... and most of all, for each other."
    tact "Through our trials and tribulations, we were side by side, our bond holding us together in the face of the greatest adversity."
    tact "Yes.\nThe love of my life..."
    
    # Partner selection
    scene cg prologue partnerselect with Fade(0.5,0.5,0.5)
    call screen imagemap_prologue_partnerselect
    
    $ partner = _return
    
    tact "[partner]..."
    
    # prologue reminiscence - dialogue is awful :|
    #if partner == "Milfeulle":
    #    scene cg prologue milfeulle with fade
    #    tact "Always smiling, always there...\nJust being with you brightens everyone's spirit, not least of all mine."
    #    tact "No matter how stormy our days together, I always know the sunshine will come through at the end..."
    #elif partner == "Ranpha":
    #    scene cg prologue ranpha with fade
    #    tact "So soft, yet so strong, always burning with passion..."
    #    tact "Every day with you is an adventure...\nTogether, we're strongest couple in space!"
    #elif partner == "Mint":
    #    scene cg prologue mint with fade
    #    tact "No matter the distance, we can always feel each other's hearts"
    #    tact "Between us, there can be no secrets...\nWith me, you can be who you truly are."
    #elif partner == "Forte":
    #    scene cg prologue forte with fade
    #    tact "No fear, no deceit... that's who you are.\nAlways pushing your team - and yourself - to ever greater heights, giving it your best..."
    #    tact "It is thanks to everything I learned from you that I became who I am now."
    #elif partner == "Vanilla":
    #    scene cg prologue vanilla with fade
    #    tact "None have loved others as you do...\nWhen someone is hurt, in pain, you'll always be there."
    #    tact "To have watched you come out of your shell, spreading your butterfly wings... With you, I'll always feel warm."
    #elif partner == "Chitose":
    #    scene cg prologue chitose with fade
    #    tact "Through all your hard work, you've become someone I'm immensely happy to stand beside."
    #    tact "A beautiful, blossoming flower, growing from a humble sprout to stand tall in the sun."

    scene bg blank with Fade(1,1,1,color="#fff")
    
    # TODO: allow other partners
    if partner != "Milfeulle":
        "Unfortunately, only Milfeulle's route has any content at present.\nWe will now railroad you onto her route.\nThank you for testing!"
        $ partner = "Milfeulle"
        
    python:
        index = getAngelIndexByName(partner)
        setAngelTrust(index, 10)
    stop music fadeout 1
    pause 1
    jump ch1_1
    
    
    