# ==============================
# CHAPTER 1-2 (Milfeulle)
# ==============================
init 1:
        image bg city = im.Scale("bg/city.png", SCREENSIZE_X, SCREENSIZE_Y)
        image bg mall1 = im.Scale("bg/mall1.png", SCREENSIZE_X, SCREENSIZE_Y)
        image bg mall2 = im.Scale("bg/mall2.png", SCREENSIZE_X, SCREENSIZE_Y)
    
label ch1_2_milfeulle:
        scene bg mall2 with fadeSlow
        $ location = "Mall"
        play music "music/Milfeulle's Theme.ogg"
        show milfeulle happy at center, dissolveCustom
        milfeulle "Come on, Tact!\nOnly three more stores to go!"
        tact_stressed "Huff... huff...\nThree more?!"
        show milfeulle normal at dissolveCustom
        milfeulle "Yep!\nWe still need to get sugar, flour and eggs, then pick up fertilizer from the gardening section..."
        show milfeulle enthusiastic at dissolveCustom
        milfeulle "And lastly, that super cute designer apron!"
        tact_crying "I'm going to collapse if we keep going like this, Milfie..."
        show milfeulle normal at dissolveCustom
        milfeulle "Oh, don't be such a big baby.\nYou're a strong man. I know you can do this!"
        tact_sweating "All the same..."
        show milfeulle happy at dissolveCustom
        milfeulle "Well, if you insist... why don't we sit on that bench over there?"
        
        play sound "sfx/footsteps.wav"
        $ location = None
        scene bg dark with wiperight
        scene bg mall1 with fade
        $ location = "Mall"
        stop sound
        
        tact_crying "Thank goodness...\nI thought my biceps were going to burst..."
        show milfeulle normal at center, dissolveCustom
        milfeulle "Those bags are heavy, aren't they, Tact?"
        tact_sweating "Yeah... maybe I should have gone to the gym more often..."
        show milfeulle veryhappy at dissolveCustom
        milfeulle "But if it's for me, you don't mind, right?"
        tact_happy "Not at all!\nAnything for you, Milfie!"
        show milfeulle normal at dissolveCustom
        milfeulle "I'm glad to hear that."
        show milfeulle happy at dissolveCustom
        milfeulle "Oh, I know!\nWhen we get back, I'll make it up to you with some nice chocolate muffins!"
        tact_oh "Milfie, you don't have to..."
        show milfeulle normal at dissolveCustom
        milfeulle "But I want to."
        tact_oneeye "You sure know how to bribe a man..."
        tact_happy "Alright, then!\nI accept your generous offer!"
        show milfeulle veryhappy at dissolveCustom
        milfeulle "That's right!\nI'll make it extra special just for you!"
        hide milfeulle at dissolveCustom
        tact_oh "...Hmm? What's that on the news?"
        stop music fadeout 1
        newscaster "...numerous spacegoers have reported as-yet unconfirmed sightings of unidentified ships throughout the Transbaal sector." 
        newscaster "Witness reports are sketchy and conflicting, but all agree that these are not ships of human origin.\nAll attempts to communicate with the vessels have failed."
        newscaster "Some sources claim that these so-called \"alien\" ships are involved in the recent attacks on shipping in the Empire. While the Navy has refused to comment on the matter, ..."
        tact_oh "...Another raider fleet?"
        show milfeulle oh at center, dissolveCustom
        milfeulle "Aliens...?\nTact, do you know anything about this?"
        tact_oh "No, nothing.\nIt's possible the Navy is still trying to confirm the reports before calling in the Angel Wing, though."
        tact_oneeye "For starters, where would aliens be coming from, anyway?"
        milfeulle "What do they look like? What do they want? Can we talk with them?"
        tact_amused "Who can say?\nThat's why they're called aliens, after all."
        show milfeulle concerned at dissolveCustom
        milfeulle "If they're really attacking civilians, won't we have to do something eventually?"
        tact_oneeye "Probably."
        tact_crying "Aaaaaah.\nThis happened the last time too..."
        milfeulle "Aw geez.\nI'm tired of fighting already."
        tact "Well...until we get more information, there's no point worrying about it."
        tact "For now, let's finish our shopping and head back to the Elsior."
        show milfeulle happy at dissolveCustom
        milfeulle "Y-Yes!"
    
        $ location = None
        scene bg blank with fadeSlow
        play sound "sfx/door_open.wav"
        scene bg elsior cabin milfeulle with wiperight
        $ location = "Milfeulle's Room"
        play music "music/Milfeulle's Theme.ogg"
        stop sound
        show milfeulle happy at center, dissolveCustom
        milfeulle "Thanks for your help, Tact!"
        tact "Anytime, Milfie."
        tact_happy "Now, how about those muffins?"
        milfeulle "Sure!\nJust take a seat over there~"
        show milfeulle enthusiastic at dissolveCustom
        milfeulle "One set of chocolate muffins, coming right up!"
        hide milfeulle at dissolveCustom
        # tact "(Milfie...)"
        scene bg elsior cabin milfeulle with fadeSlow
        tact_happy "That was amazing."
        show milfeulle happy at center, dissolveCustom
        milfeulle "I added some raisins, just for you.\nDid you like them?"
        tact_happy "Absolutely!\nYou know the way to my heart, Milfie!"
        show milfeulle veryhappy at dissolveCustom
        milfeulle "Aww, Tact~\nYou're making me blush~"
        show milfeulle enthusiastic at dissolveCustom
        milfeulle "I still have many more recipes to try.\nBe sure to eat them all, okay?"
        tact_happy "Anytime!"
        show milfeulle happy at dissolveCustom
        milfeulle "~"
        hide milfeulle at dissolveCustom
        tact_oh "(She's leaning on my shoulder...)"
        tact "(So comfortable... I could stay like this forever...)"
        tact "..."
        tact "Say, Milfie."
        show milfeulle oh at center, dissolveCustom
        milfeulle "Hm?"
        tact "Now that the galaxy is peaceful again...have you thought about settling down somewhere?\nJust like after the war with Eonia."
        tact "Just the two of us, in that dream house you always wanted...\nWe could live the rest of our lives together..."
        show milfeulle blushing at dissolveCustom
        milfeulle "Tact..."
        milfeulle "Well, I'd like that very much..."
        show milfeulle sad at dissolveCustom
        milfeulle "But I'd feel bad about leaving the Angels..."
        show milfeulle blushing at dissolveCustom
        milfeulle "But at the same time, nothing would make me happier than being with you..."
        tact "You don't have to decide right now, Milfie.\nTake your time and think it through."
        tact "What we have now is enough."
        milfeulle "..."
        show milfeulle happy at dissolveCustom
        milfeulle "You're right, Tact.\nLet's enjoy the time we have now together."
        hide milfeulle at dissolveCustom
        stop music fadeout 1
        play sound "sfx/comm_open.wav"
        pause 1.5
        stop sound
        lester_serious "Tact, you there?"
        tact_stressed "...Oi, Lester.\nYou sure know how to interrupt a romantic moment, don't you?"
        lester_grim "Well, I'm sorry about that, but we don't have time for relaxation.\nThere's a situation up here."
        tact_oh "What is it?"
        lester_serious "You know those \"aliens\" that have been making the news lately?"
        lester_aggressive "...They're here.\nIn the Transbaal system."
        tact_angry "What?!"
        lester_serious "That's right. So get your butt up here.\nAnd tell your wife to get ready to deploy."
        tact_serious "Got it.\nI'll be there."
        play sound "sfx/comm_close.wav"
        show milfeulle oh at center, dissolveCustom
        milfeulle "Tact?"
        tact_oneeye "It seems trouble follows us everywhere.\nAnd we were so comfortable too..."
        tact "I'm going up to the bridge.\nMilfie, get ready to sortie."
        show milfeulle serious at dissolveCustom
        milfeulle "Yes. I'll get to the hangar right away."
        tact "And, Milfie..."
        show milfeulle oh at dissolveCustom
        milfeulle "Hm?"
        tact "When we get back, we'll definitely continue where we left off."
        show milfeulle happy at dissolveCustom
        milfeulle "Yes!"
        tact "Alright.\nI'm heading out now."
        play sound "sfx/footsteps.wav"
        play sound "sfx/door_open.wav"
        scene bg dark with wiperight
        pause 1
        
        jump ch1_3
        
        
        
    
    