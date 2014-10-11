# ============================================================
# INIT
# ============================================================
init -2 python:
    import time
    import math

init python:
    SCREENSIZE_X = config.screen_width
    SCREENSIZE_Y = config.screen_height
    BASE_SCREENSIZE_X = 640.0   # what resolution the art assets were drawn for
    BASE_SCREENSIZE_Y = 480.0
    BASE_SCREENSIZE_X_LARGE = 1024.0
    BASE_SCREENSIZE_Y_LARGE = 480.0
    
    SCALE_X = SCREENSIZE_X / BASE_SCREENSIZE_X  # remember int vs. float division!
    SCALE_Y = SCREENSIZE_Y / BASE_SCREENSIZE_Y
    SCALE_X_LARGE = SCREENSIZE_X / BASE_SCREENSIZE_X_LARGE
    SCALE_Y_LARGE = SCREENSIZE_Y / BASE_SCREENSIZE_Y_LARGE
    
    PORTRAIT_SIZE_X = 111       # unused
    PORTRAIT_SIZE_Y = 125
    
    SPRITE_SCALE_X = SCALE_X
    SPRITE_SCALE_Y = SCALE_Y
    PORTRAIT_SCALE_X = SCALE_X
    PORTRAIT_SCALE_Y = SCALE_Y
    
    #style.portrait = Style(style.default)

    style.window.left_padding = int(0.22*SCREENSIZE_X)
    style.window.right_padding = int(SCREENSIZE_X/16)
    style.window.top_padding = int(-SCREENSIZE_Y/96)
    
    style.location = Style(style.window)
    #style.location.bold = True
    style.location.yalign = 0
    style.location.text_align = 0.5
    #style.location.layout = "greedy"
    
    location = None
    currentChapter = 0
    intermissionBG = "bg intermission ml"
    
    def writePartnerToJSON(dict):
        dict['partner'] = partner
        return dict

    config.save_json_callbacks = [writePartnerToJSON]

define fadeSlow = Fade(0.5, 0.5, 0.5)
#deprecated
define dissolveSlow = Dissolve(1)
define dissolveFast = Dissolve(0.2)
define dissolveExtraFast = Dissolve(0.1)

transform midleft:
    xanchor 0.5
    xpos 0.25
    yalign 1.0

transform midright:
    xanchor 0.5
    xpos 0.75
    yalign 1.0

# use for manually centered images, e.g. Milfie's sprites
transform midleftNoAnchor:
    xpos 0.25
    yalign 1.0
    
transform midrightNoAnchor:
    xpos 0.75
    yalign 1.0

# http://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=14823&hilit=ATL+transition#p193210
transform dissolveCustom(dt=0.25):
    on show:
        alpha 0.0
        linear dt alpha 1.0
    on hide:
        linear dt alpha 0.0
    on replace:      # when new image appears
        #alpha 0.0      # this causes an annoying ghost effect
        linear dt alpha 1.0
    on replaced:     # when old image disappears
        linear dt alpha 0.0    

transform definePos(x=0, y=0):
    xanchor 0.5
    yanchor 0.5
    xpos x
    ypos y

# ============================================================
# ============================================================
# The game starts here.
label start:
    stop music fadeout 1
    
    show screen location_display
    jump prologue

    return
    
label gameOver:
    stop music fadeout 1
    $ location = None
    scene bg gameover with fade
    pause 0.5
    show title gameover at truecenter with dissolve
    pause
    
    return

label intermission:
    stop music fadeout 1
    $ location = None
    scene bg blank with fade
    $renpy.scene()
    $renpy.show(intermissionBG)
    with fade
    play sound "music/Intermission.wav"
    
    call screen intermission
    stop sound
    scene bg blank with fade
    return
