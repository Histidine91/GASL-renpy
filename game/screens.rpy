# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = True

    

    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:

        # The one window variant.        
        window:
            id "window"
            background "dialoguebox"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"
                       
            window:
                id "window"
                background "dialoguebox"
                yoffset (int(SCREENSIZE_Y/24))

                has vbox:
                    style "say_vbox"

                text what id "what"
                
            if who:   
                window:
                    background "bg clear"
                    style "say_who_window"
                    xoffset (int(SCREENSIZE_X/25.6))
                    yoffset (int(-SCREENSIZE_Y*0.23))
                    text who:
                        id "who"
              
    # If there's a side image, display it above the text.
    if side_image:
        add side_image xanchor 0 xpos (int(SCREENSIZE_X/51.2)) yanchor 1.0 ypos (int(SCREENSIZE_Y*0.96875))
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu
    


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window: 
        style "menu_window"        
        xalign 0.5
        yalign 0.4
        
        vbox:
            style "menu"
            spacing 3
            
            for caption, action, chosen in items:
                
                if action:  
                    
                    button:
                        action action
                        style "menu_choice_button"                        

                        text caption style "menu_choice"
                    
                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True
    
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu
        
##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"
        background "nvlbg"
        top_padding 48
        left_padding -12
        area (192, 128, 768, 512)

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0
    
    #use quick_menu
        
##############################################################################
# Main Menu 
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign 0.5
        yalign 0.74

        has vbox
        imagebutton idle "button start mainmenu" hover "button start mainmenu highlight" action Start()
        imagebutton idle "button load mainmenu" hover "button load mainmenu highlight" action ShowMenu("load")
        imagebutton idle "button config mainmenu" hover "button config mainmenu highlight" action ShowMenu("preferences")
        imagebutton idle "button appendix mainmenu" hover "button appendix mainmenu highlight" action ShowMenu("appendix")
        imagebutton idle "button quit mainmenu" hover "button quit mainmenu highlight"  action Quit(confirm=False)

init -2 python:

    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"


##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98
        
        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"
    

##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

init -1 python:
    def getPartnerSaveImage(partner):
        return "saveimage " + partner.lower()

screen file_picker:

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"
            
            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)
                    
            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5
                
        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"
            
            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)
                    
                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"
                    $ partnerJSON = FileJson(i, "partner")
                    if partnerJSON != None and partnerJSON != "missing" and partnerJSON != "empty":
                        add getPartnerSaveImage(partnerJSON) xalign 0 yalign 1.0 xoffset -120

                    key "save_delete" action FileDelete(i)
                    
                    
screen save:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2 python:
    style.file_picker_frame = Style(style.menu_frame)

    style.file_picker_nav_button = Style(style.small_button)
    style.file_picker_nav_button_text = Style(style.small_button_text)

    style.file_picker_button = Style(style.large_button)
    style.file_picker_text = Style(style.large_button_text)

    

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
    
screen preferences:

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            frame:
                style_group "pref"
                has vbox

                label _("Voice Volume")
                bar value Preference("voice volume")

                if config.sample_voice:
                    textbutton "Test":
                        action Play("voice", config.sample_voice)
                        style "soundtest_button"

init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05
        
        has vbox:
            xalign .5
            yalign .5
            spacing 30
            
        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100
            
            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


init -2 python:    
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"
    
        xanchor 1.0
        xpos 0.96
        yalign 0.75

        #textbutton _("Q.Save") action QuickSave()
        #textbutton _("Q.Load") action QuickLoad()
        #textbutton _("Save") action ShowMenu('save')
        textbutton _("Whale") action ShowMenu('whaleReport')
        imagebutton idle "button minimize" hover "button minimize highlight" action HideInterface()
        imagebutton idle "button skip" hover "button skip highlight" selected_idle "button skip on" selected_hover "button skip highlight" action Skip()
        imagebutton idle "button auto" hover "button auto highlight" selected_idle "button auto on" selected_hover "button auto highlight" action Preference("auto-forward", "toggle")
        #textbutton _("Prefs") action ShowMenu('preferences')
    vbox:
        style_group "quick"
        xanchor 0.5 xpos 0.96 yalign 0.85
        
        imagebutton idle "button system" hover "button system highlight" action ShowMenu('preferences') 
        
        
init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 12
    style.quick_button_text.idle_color = "#888a"
    style.quick_button_text.hover_color = "#fff"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#444a"
    
    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False
    
##############################################################################
# CUSTOM SCREENS
##############################################################################

##############################################################################
# Common functions
init -1 python:
    def getPhase(constant):
        phase = math.sin(2*time.time()%math.pi)
        return phase*(1-constant) + constant
        
transform expandFromUpperLeft(dt, wait=0):
    xzoom 0.0  yzoom 0.0 alpha 0.5
    time wait
    linear dt xzoom 1.0 yzoom 1.0 alpha 1.0
    
transform expandFromCenterVertical(dt, wait=0):
    yzoom 0.0 yanchor 0.5 alpha 0.5
    time wait
    linear dt yzoom 1.0 alpha 1.0
    
transform expandFromLowerLeft(dt, wait=0):
    yanchor 1.0 xzoom 0.0 yzoom 0.0 alpha 0.5
    time wait
    linear dt xzoom 1.0 yzoom 1.0 alpha 1.0

transform contractAndFadeIn(dt, wait=0):
    xzoom 2.0 yzoom 2.0 alpha 0.0
    time wait
    linear dt xzoom 1.0 yzoom 1.0 alpha 1.0
    
transform zoomIn(initZoom, dt, wait=0):
    xzoom initZoom yzoom initZoom alpha 0.5 #rotate 360
    time wait
    linear dt xzoom 1.0 yzoom 1.0 alpha 1.0
    
transform flyInFromLeft(dt, wait=0):
    xoffset -1024 alpha 0.5
    time wait
    linear dt xoffset 0 alpha 1.0
    
transform fadeIn(dt, wait=0):
    alpha 0.0
    time wait
    linear dt alpha 1.0

##############################################################################
# Location display
screen location_display:
    modal False
    if location:
        window:
            xmaximum (SCREENSIZE_X/2)
            ymaximum (SCREENSIZE_Y/8)
            background "locationbox"
            
            text location style "location" text_align 0.0
            #xfill True
            left_margin 64      #this ridiculosity is so we can have both the absence of line breaks and placement of the text in a sensible location
            xanchor 0
            xpos -56
            yalign 0.0
            xoffset 0
            yoffset 8
            top_padding 14
            left_padding 0
            #right_padding 48

##############################################################################
# Intermission screen
transform expandIntermissionScreenButton(wait):
    xzoom 0.0 alpha 0.0
    time wait
    linear 0.5 xzoom 1.0 alpha 1.0
    
screen intermission:
    transform at expandIntermissionScreenButton(0):
        textbutton _("Continue") action Return() xpos 16 yanchor 1.0 ypos (SCREENSIZE_Y-224) xminimum 192
    transform at expandIntermissionScreenButton(0.5):
        textbutton _("Preferences") action ShowMenu("preferences") xpos 32 yanchor 1.0 ypos (SCREENSIZE_Y-192) xminimum 192
    transform at expandIntermissionScreenButton(1.0):
        textbutton _("Save Game") action ShowMenu("save") xpos 16 yanchor 1.0 ypos (SCREENSIZE_Y-160) xminimum 192
    transform at expandIntermissionScreenButton(1.5):
        textbutton _("Load Game") action ShowMenu("load") xpos 32 yanchor 1.0 ypos (SCREENSIZE_Y-128) xminimum 192
    transform at expandIntermissionScreenButton(2.0):
        textbutton _("Main Menu") action MainMenu() xpos 16 yanchor 1.0 ypos (SCREENSIZE_Y-96) xminimum 192
    transform at expandIntermissionScreenButton(2.5):
        textbutton _("Help") action Help() xpos 32 yanchor 1.0 ypos (SCREENSIZE_Y-64) xminimum 192
    transform at expandIntermissionScreenButton(3.0):
        textbutton _("Quit") action Quit() xpos 16 yanchor 1.0 ypos (SCREENSIZE_Y-32) xminimum 192

##############################################################################
# Tactical map
#
# How to handle:
#       Dictionary of unitType-icon pairs
#       List of unit types for sidebar
#       List of units with data:
#               Type
#               Position
#               Facing
#       Arrows as needed        - have the main script render them manually?

init -1 python:
    def getIconAlpha(unitData):
        if (mapHighlightUnit == unitData["type"]) or (('id' in unitData) and mapHighlightUnit == unitData['id']):
            return getPhase(0.5)
        else:
            return 1
            
    def renderUnitIcon(st, at, unitData, unitList, unitTypeList):
        toReturn = At(unitIconMap[unitData['type']], unitIconProperties(unitData, unitList, unitTypeList))
        return (toReturn, 0.1)        

    mapHighlightUnit = None

transform unitIconProperties(unitData, unitList, unitTypeList):
    xalign unitData['xpos'] yalign unitData['ypos'] rotate unitData['heading'] alpha getIconAlpha(unitData)

screen tactical_map(mapImage, unitList, unitTypeList, location):
        modal False
        transform at expandFromCenterVertical(0.25):
            frame id "tacticalDisplay":
                background "tacticaldisplay"
                area (144, 304, 720, 480)
                fixed:
                    #add mapImage xalign 0.55 yalign 0.33
                    text ("AREA: " + location.upper()) font "impact.ttf" xanchor 1.0 yanchor 1.0 xpos 0.63 ypos 0.98 size 16  antialias True #bold True
                    for unitData in unitList:
                        add DynamicDisplayable(renderUnitIcon, unitData, unitList, unitTypeList)
                        if "number" in unitData:
                            text str(unitData["number"]) size 12 outlines {(1,"#000",0,0)} xalign unitData['xpos'] yalign unitData['ypos'] xoffset 16 yoffset 8 
                    vbox xpos 0.68 ypos 0.22:     #area(0.6, 0.2, 0.3, 0.7):
                        for unit in unitTypeList:
                            fixed area(0,0,192,32):
                                add unitIconMap[unit['type']] xanchor 0.5 yanchor 0.5 xpos 24 ypos 0.5
                                text unit['text'] xpos 48 size 16 yoffset 8 #color (160, 224, 255, 255) 
                                
screen unitinfo(unitpic, name, desc):
    modal False
    transform at expandFromLowerLeft(0.1):
        frame id "unitInfo":
            background "unitinfo"
            area (688, 336, 320, 320)
            add unitpic xalign 0.5 yalign 0.5
            text name size 24 xpos 32 ypos 32
            text desc size 16 xpos 48 ypos 56
            
##############################################################################
# Info panel

screen infopanel(img):
    modal False
    transform at expandFromLowerLeft(0.25):
        frame id "infopanel":
            background "infopanel"
            area(144, 550, 720, 480)
            add img xalign 0.5 yalign 0.5
            
##############################################################################
# appendix

init python:
    class MusicRoomPlusTogglePlay(Action):
        def __init__(self, mr, fileName = None):
            self.mr = mr

        def get_selected(self):
            return renpy.music.get_playing(self.mr.channel) is not None     
            
        def __call__(self, filename=None):
            if renpy.music.get_playing(self.mr.channel):
                return self.mr.stop()

            self.mr.shuffled = None
            if filename == None:
                track = getTrackFilename(self.mr.currentIndex)
            return self.mr.play(track)
    
    class MusicRoomPlusNext(Action):
        def __init__(self, mr):
            self.mr = mr        
        
        def __call__(self):
            if renpy.music.is_playing(channel=self.mr.channel):
                self.mr.next()
            else:
                idx = (self.mr.currentIndex + 1) % len(playlist)
                self.mr.currentIndex = idx
                self.mr.currentTrackName = store.playlist[idx]
           
    class MusicRoomPlusPrevious(Action):
        def __init__(self, mr):
            self.mr = mr        
        
        def __call__(self):
            if renpy.music.is_playing(channel=self.mr.channel):
                self.mr.previous()
            else:
                idx = (self.mr.currentIndex - 1) % len(playlist)
                self.mr.currentIndex = idx
                self.mr.currentTrackName = store.playlist[idx]   
    
    class MusicRoomPlus(MusicRoom):
        currentTrackName = playlist[0]
        currentIndex = 0
        
        def play(self, filename=None, offset=0, queue=False):
            playlist = self.unlocked_playlist(filename)

            if not playlist:
                return

            if filename is None:
                filename = renpy.music.get_playing(channel=self.channel)

            try:
                idx = playlist.index(filename)
            except ValueError:
                idx = 0

            idx = (idx + offset) % len(playlist)

            if self.single_track:
                playlist = [ playlist[idx] ]
            elif self.loop:
                playlist = playlist[idx:] + playlist[:idx]
            else:
                playlist = playlist[idx:]

            if queue:
                renpy.music.queue(playlist, channel=self.channel, loop=self.loop)
            else:
                renpy.music.play(playlist, channel=self.channel, fadeout=self.fadeout, fadein=self.fadein, loop=self.loop)
                
            #OVERRIDE: make these values globally available so we don't have to hunt for them
                self.currentIndex = idx
                self.currentTrackName = store.playlist[idx]
        
        def TogglePlay(self, filename = None):
            return MusicRoomPlusTogglePlay(self, filename)
            
        def Next(self):
            return MusicRoomPlusNext(self)

        def Previous(self):
            return MusicRoomPlusPrevious(self)
            
    """
    def getTrackIndex(trackName):
        for index, track in enumerate(playlistRelativePaths):
            if track == trackName:
                return index
                   
    class refreshTrackInfo(Action):
        def __call__(self):
            trackFromRP = musicPlayer.last_playing     #renpy.music.get_playing(musicPlayer.channel)
            if trackFromRP != None and trackFromRP != "":
                index = getTrackIndex(trackFromRP)
                if index != None:
                    musicPlayer.currentIndex = index
                    musicPlayer.currentTrackName = playlist[index]
    """

init 1 python:
    musicPlayer = MusicRoomPlus(fadeout=0, single_track = True)
    trackIndex = 0
    for track in playlist:
        trackIndex = trackIndex + 1
        musicPlayer.add("music/" + track + ".ogg", always_unlocked = True)
    currentTrack = 1

    def getTrackFilename(track):
        return playlistRelativePaths[track]
    
    def renderTrackNumber(st, at):
        #toReturn = At(Text(str(currentTrack+1), size = 42))
        toReturn = At(Text(str(musicPlayer.currentIndex+1), size = 42))
        return (toReturn, 0.2)
        
    def renderTrackTitle(st, at):
        #toReturn = At(Text(playlist[currentTrack], size = 32))
        toReturn = At(Text(musicPlayer.currentTrackName, size = 32))
        return (toReturn, 0.2)    

screen appendix:
    tag menu    # Ensure this replaces the main menu.
    fixed:
        add "bg appendix"
        transform at expandFromCenterVertical(0.5):
            ypos 0.5
            add "bg appendix2" xalign 0.5 yalign 0.25
            add "appendixheader" xalign 0.5 yalign 0
            
            
            transform at contractAndFadeIn(0.1, 0.5):
                imagebutton idle "button appendix otherscenes" hover "button appendix otherscenes highlight" xalign 0.5 yalign 0.3
            transform at contractAndFadeIn(0.1, 0.625):
                imagebutton idle "button appendix milfeulle" hover "button appendix milfeulle highlight" xalign 0.2 yalign 0.4
            transform at contractAndFadeIn(0.1, 0.75):
                imagebutton idle "button appendix chitose" hover "button appendix chitose highlight" xalign 0.8 yalign 0.4
            transform at contractAndFadeIn(0.1, 0.875):
                imagebutton idle "button appendix ranpha" hover "button appendix ranpha highlight" xalign 0.03 yalign 0.1
            transform at contractAndFadeIn(0.1, 1):
                imagebutton idle "button appendix forte" hover "button appendix forte highlight" xalign 0.97 yalign 0.1
            transform at contractAndFadeIn(0.1, 1.125):
                imagebutton idle "button appendix mint" hover "button appendix mint highlight" xalign 0.03 yalign 0.65
            transform at contractAndFadeIn(0.1, 1.25):
                imagebutton idle "button appendix vanilla" hover "button appendix vanilla highlight" xalign 0.97 yalign 0.65
            transform at contractAndFadeIn(0.1, 1.375):
                imagebutton idle "button appendix close" hover "button appendix close highlight" xalign 0.98 yalign 0.975 action Return()
            
            fixed area (32, SCREENSIZE_Y-160, SCREENSIZE_X-64, 96):
                add "bgmbar"
                add DynamicDisplayable(renderTrackNumber) xpos 190 ypos 16 xanchor 0.5
                add DynamicDisplayable(renderTrackTitle) xpos 244 ypos 20
                fixed area(0, 110, 120, 40):
                    transform at flyInFromLeft(0.25, 0.25):
                        add Text("B", size=56, outlines={(4,"#2a8c",0,0)}) xpos 0 yanchor 0.5 rotate -20
                    transform at flyInFromLeft(0.25, 0.5):
                        add Text("G", size=48, outlines={(4,"#2a8c",0,0)}) xpos 40 yanchor 0.5 rotate -20
                    transform at flyInFromLeft(0.25, 0.75):
                        add Text("M", size=52, outlines={(4,"#2a8c",0,0)}) xpos 80 yanchor 0.5 rotate -20
                hbox area (280, 84, 420, 40):
                    imagebutton idle "button music prevtrack" hover "button music prevtrack highlight" action musicPlayer.Previous()
                    imagebutton idle "button music play" hover "button music play highlight" selected_idle "button music play on" selected_hover "button music play highlight" action musicPlayer.TogglePlay()    #FIXME: broken
                    imagebutton idle "button music stop" hover "button music stop highlight" action musicPlayer.Stop()
                    imagebutton idle "button music loop" hover "button music loop highlight" selected_idle "button music loop on" selected_hover "button music loop highlight" action musicPlayer.ToggleLoop()
                    imagebutton idle "button music nexttrack" hover "button music nexttrack highlight" action musicPlayer.Next()
                    
                    #imagebutton idle "button music prevtrack" hover "button music prevtrack highlight" action [SetVariable("currentTrack", getNextTrackIndex(-1)), Play("music", getTrackFilename(getNextTrackIndex(-1)), loop = musicLoop)]
                    #imagebutton idle "button music play" hover "button music play highlight" selected_idle "button music play on" selected_hover "button music play highlight" action Play("music", getTrackFilename(currentTrack), loop = musicLoop)
                    #imagebutton idle "button music stop" hover "button music stop highlight" action Stop("music")
                    #imagebutton idle "button music loop" hover "button music loop highlight" selected_idle "button music loop on" selected_hover "button music loop highlight" action SetVariable("musicLoop", not musicLoop)
                    #imagebutton idle "button music nexttrack" hover "button music nexttrack highlight" action [SetVariable("currentTrack", getNextTrackIndex(1)), Play("music", getTrackFilename(getNextTrackIndex(1)), loop = musicLoop)]
                
                
    on "replace" action [Stop("music"), Play("sound", "sfx/appendix.wav")]
    on "replaced" action [Fade(0.25, 0, 0.25, "#fff"), Play("music", "music/Title Theme (GA1).ogg")]
        


##############################################################################
# text box: auto symbol / "click to continue" arrow

init -1 python:
    def renderAutoIndicator(st, at):
        toReturn = At("textauto", autoIndicatorProperties)
        return (toReturn, 0.1)
    
    def renderTextArrow1(st, at):
        toReturn = At("textarrow 1", textArrowProperties)
        return (toReturn, 0.1)
    def renderTextArrow2(st, at):
        toReturn = At("textarrow 2", textArrowProperties)
        return (toReturn, 0.1)

transform autoIndicatorProperties:
    xpos 0.99 ypos 0.99 xanchor 1.0 yanchor 1.0 alpha getPhase(0.5)
    
transform textArrowProperties:
    xpos 0.99 ypos 0.99 xanchor 1.0 yanchor 1.0
    
##############################################################################
# whale report

init -1 python:
    def getWhaleReportFrame(id):
        if angelAbsent[id]:
            return whaleReportImagesAbsent[id]
        else:
            return whaleReportImagesFrame[id]
        
    def getWhaleReportImage(id):
        return whaleReportImages[id][moods[id]]
    
    def getAngelTrust(id):
        if trust[id] == 0:
            return -1   #fixes tiny remnant on bar
        return trust[id]

screen whaleReport:
    tag menu    # Ensure this replaces the main menu.
    fixed:
        add "bg whalereport"
        transform at contractAndFadeIn(0.1, 0.5):
            add "whalereportheader" xalign 0.5 yalign 0.01
        
        # Ranpha
        transform at contractAndFadeIn(0.15, 0.75):
            add getWhaleReportFrame(2) xpos 46 ypos 32
            add getWhaleReportImage(2) xpos 63 ypos 80
            if not angelAbsent[2]:
                bar value getAngelTrust(2) range 20  xpos 137 ypos 52 style "whalebar"
        # Milfeulle
        transform at contractAndFadeIn(0.15, 0.875):
            add getWhaleReportFrame(1) xalign 0.5 ypos 96
            add getWhaleReportImage(1) xpos (SCREENSIZE_X/2 + 2) xanchor 0.5 ypos 134
            if not angelAbsent[1]:
                bar value getAngelTrust(1) range 20 xpos 453 ypos 337 style "whalebar"
        # Forte
        transform at contractAndFadeIn(0.15, 1):
            add getWhaleReportFrame(4) xpos (SCREENSIZE_X - 42) xanchor 1.0 ypos 32
            add getWhaleReportImage(4) xpos (SCREENSIZE_X - 64) xanchor 1.0 ypos 80
            if not angelAbsent[4]:
                bar value getAngelTrust(4) range 20 xpos 779 ypos 52 style "whalebar"
        # Mint
        transform at contractAndFadeIn(0.15, 1.125):
            add getWhaleReportFrame(3) xpos 40 ypos (SCREENSIZE_Y - 32) yanchor 1.0
            add getWhaleReportImage(3) xpos 63 ypos (SCREENSIZE_Y - 80) yanchor 1.0
            if not angelAbsent[3]:
                bar value getAngelTrust(3) range 20 xpos 144 ypos 707 style "whalebar"
        #Chitose
        transform at contractAndFadeIn(0.15, 1.25):
            add getWhaleReportFrame(6) xalign 0.5 ypos (SCREENSIZE_Y - 96) yanchor 1.0
            add getWhaleReportImage(6) xpos (SCREENSIZE_X/2 - 2) xanchor 0.5 ypos (SCREENSIZE_Y - 134) yanchor 1.0
            if not angelAbsent[6]:
                bar value getAngelTrust(6) range 20 xpos 453 ypos 422 style "whalebar"
        #Vanilla
        transform at contractAndFadeIn(0.15, 1.375):
            add getWhaleReportFrame(5) xpos (SCREENSIZE_X - 40) xanchor 1.0 ypos (SCREENSIZE_Y - 32) yanchor 1.0
            add getWhaleReportImage(5) xpos (SCREENSIZE_X - 56) xanchor 1.0 ypos (SCREENSIZE_Y - 80) yanchor 1.0
            if not angelAbsent[5]:
                bar value getAngelTrust(5) range 20 xpos 776 ypos 707 style "whalebar"
            
        transform at contractAndFadeIn(0.15, 1.5):
            imagebutton idle "button back" hover "button back highlight" xalign 0.5 yalign 0.99 action Return()
            
##############################################################################
# CTC indicator

init -1 python:
    def renderCTC(st, at):
        toReturn = At("icon ctcarrow", ctcProperties)
        return (toReturn, 0.1)        

transform ctcProperties:
    xanchor 0.5 xpos 0.93 yalign 0.98 alpha getPhase(0.5)