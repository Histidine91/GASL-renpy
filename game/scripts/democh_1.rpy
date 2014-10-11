# ==============================
# DEMO CHAPTER 1
# ==============================

label democh_1:
    scene bg chapter_intro_splash with dissolve
    play sound "music/New Chapter.wav"
    pause 0.5
    show title title1 at truecenter with dissolve
    pause

    scene bg elsior bridge with fadeSlow
    stop sound
    
    show milfeulle normal with dissolveFast
    play music "music/Milfeulle's Theme.ogg"
    
    milfeulle "Hi, Tact!"
    tact "Hi, Milfie."
    milfeulle "We're making a new game! Isn't this fun?"
    hide milfeulle
    show chitose surprised with dissolveFast
    chitose "Um... is it really okay to put us in a different game like this?"
    tact "It'll be fine, Chitose.\nJapanese copyright rules are more relaxed."
    show chitose normal
    chitose "If you say so, Tact."
    hide chitose
    show milfeulle happy with dissolveFast
    milfeulle "This is gonna be so much fun!"
    tact "Alright, time to go check on the others..."
    
    stop music
    play sound "sfx/door_open.wav"
    scene bg blank with wiperight
    pause 0.5
    scene bg elsior tealounge with fade
    play music "music/The Angel Wing Appears.ogg"
    
    tact "Hi everyone~"
    show ranpha normal with dissolveFast
    ranpha "Hiyo!"
    hide ranpha
    show forte normal at left with dissolveFast
    forte "Ah, Tact.\nGetting ready for the new game?"
    show mint normal at right with dissolveFast
    mint "We're all looking forward to it.\nIt's been nine years since our last game."
    hide forte
    hide mint
    show vanilla normal with dissolveFast
    vanilla "Hopefully it will make us popular outside Japan..."
    hide vanilla
    show ranpha starryeyed with dissolveFast
    ranpha "Starcrossed Lovers!\nI can't wait to play it~"
    hide ranpha
    show mint elegant at center with dissolveFast
    mint "But remember, making a VN is not just about coding and writing.\nYou need skilled artists too."
    tact "Don't worry.\nI've got everything under control."
    tact_oh "Oh, that's right.\nI need to test the intermission screen..."
    
    call intermission
    