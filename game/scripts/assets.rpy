
# ============================================================
# STRINGS
# ============================================================
init python:
    chapterTitles = [
        "Prologue",
        "Lost Children",
        "A Dark Remnant",
        "In Vengeance Born",
        "Into the Shadows",
        "Rising Light"
    ]

# ============================================================
# BACKGROUNDS
# ============================================================
image bg chapter_intro_splash = im.Scale("bg/chapter_intro_splash.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg gameover = im.Scale("bg/gameover.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg intermission ml = im.Scale("bg/intermission_ml.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg intermission el = im.Scale("bg/intermission_el.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg mainmenu = im.Scale("bg/mainmenu_ga1.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg appendix = im.Scale("bg/appendix.png", SCREENSIZE_X, SCREENSIZE_Y) 
image bg whalereport = im.Scale("bg/whalereport.png", SCREENSIZE_X, SCREENSIZE_Y)

image bg dark = im.Scale("bg/dark.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg blank = im.Scale("bg/blank.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg clear = im.Scale("bg/clear.png", SCREENSIZE_X, SCREENSIZE_Y)

image bg elsior bridge = im.Scale("bg/elsior_bridge.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg elsior corridor = im.Scale("bg/elsior_corridor.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg elsior tealounge = im.Scale("bg/elsior_tealounge.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg elsior hangar = im.Scale("bg/elsior_hangar.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg elsior cabin outside = im.Scale("bg/elsior_cabin_outside.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg elsior cabin milfeulle = im.Scale("bg/elsior_cabin_milfeulle.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg elsior cabin vanilla = im.Scale("bg/elsior_cabin_vanilla.png", SCREENSIZE_X, SCREENSIZE_Y)

image bg whitemoon hallway = im.Scale("bg/whitemoon_hallway.png", SCREENSIZE_X, SCREENSIZE_Y)
image bg conferenceroom = im.Scale("bg/conferenceroom.png", SCREENSIZE_X, SCREENSIZE_Y)

image bg appendix2 = im.FactorScale("bg/appendix_partial.png", SCALE_X, SCALE_Y)

image cg cockpit milfeulle1 = im.Scale("cg/cockpit_milfeulle1.png", SCREENSIZE_X, SCREENSIZE_Y)
image cg cockpit milfeulle2 = im.Scale("cg/cockpit_milfeulle2.png", SCREENSIZE_X, SCREENSIZE_Y)
image cg cockpit ranpha1 = im.Scale("cg/cockpit_ranpha1.png", SCREENSIZE_X, SCREENSIZE_Y)
image cg cockpit ranpha2 = im.Scale("cg/cockpit_ranpha2.png", SCREENSIZE_X, SCREENSIZE_Y)
image cg cockpit mint1 = im.Scale("cg/cockpit_mint1.png", SCREENSIZE_X, SCREENSIZE_Y)
image cg cockpit mint2 = im.Scale("cg/cockpit_mint2.png", SCREENSIZE_X, SCREENSIZE_Y)
image cg cockpit forte1 = im.Scale("cg/cockpit_forte1.png", SCREENSIZE_X, SCREENSIZE_Y)
image cg cockpit forte2 = im.Scale("cg/cockpit_forte2.png", SCREENSIZE_X, SCREENSIZE_Y)
image cg cockpit vanilla1 = im.Scale("cg/cockpit_vanilla1.png", SCREENSIZE_X, SCREENSIZE_Y)
image cg cockpit vanilla2 = im.Scale("cg/cockpit_vanilla2.png", SCREENSIZE_X, SCREENSIZE_Y)
image cg cockpit chitose1 = im.Scale("cg/cockpit_chitose1.png", SCREENSIZE_X, SCREENSIZE_Y)
image cg cockpit chitose2 = im.Scale("cg/cockpit_chitose2.png", SCREENSIZE_X, SCREENSIZE_Y)

# ============================================================
# UI
# ============================================================
image icon ga small = im.Scale("gui/logo_angels.png", SCREENSIZE_Y/24, SCREENSIZE_Y/24)   # 32 * 32
image icon ga small greyscale = im.Scale("gui/logo_angels_grey.png", SCREENSIZE_Y/24, SCREENSIZE_Y/24)
image icon ctcarrow = im.Scale("gui/textarrow.png", SCREENSIZE_Y/32, SCREENSIZE_Y/32)  # 24 * 24 
image ctc = DynamicDisplayable(renderCTC)

image title gameover = "gui/title_gameover.png"
image dialoguebox = im.FactorScale("gui/dialoguebox.png", SCALE_X, SCALE_Y, xanchor=0, xpos=8, yalign=1.0)
image locationbox = im.FactorScale("gui/locationbox.png", SCALE_X, SCALE_Y, xanchor=0, xpos=8)

image tacticaldisplay = "gui/tacdisplay.png"
image unitinfo = "gui/unitinfo.png"
image nvlbg = "gui/nvlbg.png"
image infopanel = "gui/infopanel.png"

image textarrow 1 = "gui/textarrow_1.png"
image textarrow 2 = "gui/textarrow_2.png"
image textauto = "gui/text_auto.png"

image appendixitem = im.FactorScale("gui/appendix_item.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image appendixitem highlight = im.FactorScale("gui/appendix_item_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image appendixitem off = im.FactorScale("gui/appendix_item_off.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image appendixheader = im.FactorScale("gui/appendix_header.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image whalereportheader = im.FactorScale("gui/whalereport/header.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image bgmbar = im.FactorScale("gui/bgmbar.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)

image button system = im.FactorScale("gui/buttons/system_side.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button system highlight = im.FactorScale("gui/buttons/system_side_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)

image button auto = im.FactorScale("gui/buttons/auto.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button auto highlight = im.FactorScale("gui/buttons/auto_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button auto on = im.FactorScale("gui/buttons/auto_on.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)

image button skip = im.FactorScale("gui/buttons/fastforward.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button skip highlight = im.FactorScale("gui/buttons/fastforward_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button skip on = im.FactorScale("gui/buttons/fastforward_on.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)

image button minimize = im.FactorScale("gui/buttons/x.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button minimize highlight = im.FactorScale("gui/buttons/x_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)

image button back = im.FactorScale("gui/buttons/menu/back.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button back highlight = im.FactorScale("gui/buttons/menu/back_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)

image button start mainmenu = im.FactorScale("gui/buttons/menu/start_main.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button start mainmenu highlight = im.FactorScale("gui/buttons/menu/start_main_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button load mainmenu = im.FactorScale("gui/buttons/menu/load_main.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button load mainmenu highlight = im.FactorScale("gui/buttons/menu/load_main_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button config mainmenu = im.FactorScale("gui/buttons/menu/config_main.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button config mainmenu highlight = im.FactorScale("gui/buttons/menu/config_main_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button appendix mainmenu = im.FactorScale("gui/buttons/menu/appendix_main.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button appendix mainmenu highlight = im.FactorScale("gui/buttons/menu/appendix_main_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button quit mainmenu = im.FactorScale("gui/buttons/menu/quit_main.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button quit mainmenu highlight = im.FactorScale("gui/buttons/menu/quit_main_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)

image button appendix milfeulle = im.FactorScale("gui/buttons/appendix/milfeulle.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button appendix milfeulle highlight = im.FactorScale("gui/buttons/appendix/milfeulle_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button appendix ranpha = im.FactorScale("gui/buttons/appendix/ranpha.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button appendix ranpha highlight = im.FactorScale("gui/buttons/appendix/ranpha_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button appendix mint = im.FactorScale("gui/buttons/appendix/mint.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button appendix mint highlight = im.FactorScale("gui/buttons/appendix/mint_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button appendix forte = im.FactorScale("gui/buttons/appendix/forte.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button appendix forte highlight = im.FactorScale("gui/buttons/appendix/forte_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button appendix vanilla = im.FactorScale("gui/buttons/appendix/vanilla.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button appendix vanilla highlight = im.FactorScale("gui/buttons/appendix/vanilla_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button appendix chitose = im.FactorScale("gui/buttons/appendix/chitose.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button appendix chitose highlight = im.FactorScale("gui/buttons/appendix/chitose_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button appendix otherscenes = im.FactorScale("gui/buttons/appendix/otherscenes.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button appendix otherscenes highlight = im.FactorScale("gui/buttons/appendix/otherscenes_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button appendix close = im.FactorScale("gui/buttons/menu/close_appendix.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button appendix close highlight = im.FactorScale("gui/buttons/menu/close_appendix_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)

image button music play = im.FactorScale("gui/buttons/appendix/play.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button music play highlight = im.FactorScale("gui/buttons/appendix/play_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button music play on = im.FactorScale("gui/buttons/appendix/play_on.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button music loop = im.FactorScale("gui/buttons/appendix/loop.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button music loop highlight = im.FactorScale("gui/buttons/appendix/loop_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button music loop on = im.FactorScale("gui/buttons/appendix/loop_on.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button music loop inactive = im.FactorScale("gui/buttons/appendix/loop_inactive.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button music stop = im.FactorScale("gui/buttons/appendix/stop.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button music stop highlight = im.FactorScale("gui/buttons/appendix/stop_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button music stop inactive = im.FactorScale("gui/buttons/appendix/stop_inactive.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button music nexttrack = im.FactorScale("gui/buttons/appendix/nexttrack.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button music nexttrack highlight = im.FactorScale("gui/buttons/appendix/nexttrack_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button music prevtrack = im.FactorScale("gui/buttons/appendix/prevtrack.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image button music prevtrack highlight = im.FactorScale("gui/buttons/appendix/prevtrack_highlight.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)

image bar affection empty = "gui/whalereport/bar_empty.png"
image bar affection full = "gui/whalereport/bar_full.png"

image saveimage milfeulle = "gui/save_milfeulle.png"
image saveimage ranpha = "gui/save_ranpha.png"
image saveimage mint = "gui/save_mint.png"
image saveimage forte = "gui/save_forte.png"
image saveimage vanilla = "gui/save_vanilla.png"
image saveimage chitose = "gui/save_chitose.png"

# ============================================================
# CHARACTER IMAGES
# ============================================================

# Tact
image portrait tact normal = im.FactorScale("portraits/tact_normal.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait tact oh = im.FactorScale("portraits/tact_oh.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait tact amused = im.FactorScale("portraits/tact_amused.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait tact sweating = im.FactorScale("portraits/tact_sweating.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait tact surprised = im.FactorScale("portraits/tact_surprised.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait tact serious = im.FactorScale("portraits/tact_serious.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait tact aggressive = im.FactorScale("portraits/tact_aggressive.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait tact angry = im.FactorScale("portraits/tact_angry.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait tact stressed = im.FactorScale("portraits/tact_stressed.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait tact oneeye = im.FactorScale("portraits/tact_oneeye.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait tact crying = im.FactorScale("portraits/tact_crying.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait tact happy = im.FactorScale("portraits/tact_happy.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)

# Lester
image lester normal = im.FactorScale("sprites/characters/lester_normal.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image lester amused = im.FactorScale("sprites/characters/lester_amused.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image lester annoyed = im.FactorScale("sprites/characters/lester_annoyed.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image lester serious = im.FactorScale("sprites/characters/lester_serious.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image lester aggressive = im.FactorScale("sprites/characters/lester_aggressive.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image lester grim = im.FactorScale("sprites/characters/lester_grim.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image lester relaxed = im.FactorScale("sprites/characters/lester_relaxed.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image lester stressed = im.FactorScale("sprites/characters/lester_stressed.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image portrait lester normal = im.FactorScale("portraits/lester_normal.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait lester aggressive = im.FactorScale("portraits/lester_aggressive.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait lester relaxed = im.FactorScale("portraits/lester_relaxed.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait lester serious = im.FactorScale("portraits/lester_serious.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait lester grim = im.FactorScale("portraits/lester_grim.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait lester stressed = im.FactorScale("portraits/lester_stressed.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)

# Milfeulle
image milfeulle normal = im.FactorScale("sprites/characters/milfeulle_normal.png", SPRITE_SCALE_X, SPRITE_SCALE_Y, xanchor=0.3)
image milfeulle happy = im.FactorScale("sprites/characters/milfeulle_happy.png", SPRITE_SCALE_X, SPRITE_SCALE_Y, xanchor=0.5)
image milfeulle veryhappy = im.FactorScale("sprites/characters/milfeulle_veryhappy.png", SPRITE_SCALE_X, SPRITE_SCALE_Y, xanchor=0.3)
image milfeulle oh = im.FactorScale("sprites/characters/milfeulle_oh.png", SPRITE_SCALE_X, SPRITE_SCALE_Y, xanchor=0.5)
image milfeulle blushing = im.FactorScale("sprites/characters/milfeulle_blushing.png", SPRITE_SCALE_X, SPRITE_SCALE_Y, xanchor=0.3)
image milfeulle sad = im.FactorScale("sprites/characters/milfeulle_sad.png", SPRITE_SCALE_X, SPRITE_SCALE_Y, xanchor=0.5)
image milfeulle serious = im.FactorScale("sprites/characters/milfeulle_serious.png", SPRITE_SCALE_X, SPRITE_SCALE_Y, xanchor=0.5)
image milfeulle concerned = im.FactorScale("sprites/characters/milfeulle_concerned.png", SPRITE_SCALE_X, SPRITE_SCALE_Y, xanchor=0.5)
image milfeulle enthusiastic = im.FactorScale("sprites/characters/milfeulle_enthusiastic.png", SPRITE_SCALE_X, SPRITE_SCALE_Y, xanchor=0.4)
image portrait milfeulle normal = im.FactorScale("portraits/milfeulle_normal.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait milfeulle happy = im.FactorScale("portraits/milfeulle_happy.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait milfeulle concerned = im.FactorScale("portraits/milfeulle_concerned.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait milfeulle sad = im.FactorScale("portraits/milfeulle_sad.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)

# Ranpha
image ranpha normal = im.FactorScale("sprites/characters/ranpha_normal.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image ranpha relaxed = im.FactorScale("sprites/characters/ranpha_relaxed.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image ranpha annoyed = im.FactorScale("sprites/characters/ranpha_annoyed.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image ranpha veryhappy = im.FactorScale("sprites/characters/ranpha_veryhappy.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image ranpha furious = im.FactorScale("sprites/characters/ranpha_furious.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image ranpha starryeyed = im.FactorScale("sprites/characters/ranpha_starryeyed.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image portrait ranpha normal = im.FactorScale("portraits/ranpha_normal.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait ranpha serious = im.FactorScale("portraits/ranpha_serious.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait ranpha aggressive = im.FactorScale("portraits/ranpha_serious.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait ranpha sad = im.FactorScale("portraits/ranpha_sad.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait ranpha stressed = im.FactorScale("portraits/ranpha_stressed.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait ranpha worried = im.FactorScale("portraits/ranpha_worried.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)

# Mint
image mint normal = im.FactorScale("sprites/characters/mint_normal.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image mint happy = im.FactorScale("sprites/characters/mint_happy.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image mint veryhappy = im.FactorScale("sprites/characters/mint_veryhappy.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image mint elegant = im.FactorScale("sprites/characters/mint_elegant.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image portrait mint normal = im.FactorScale("portraits/mint_normal.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait mint angry = im.FactorScale("portraits/mint_angry.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)

# Forte
image forte normal = im.FactorScale("sprites/characters/forte_normal.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image forte calm = im.FactorScale("sprites/characters/forte_calm.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image forte concerned = im.FactorScale("sprites/characters/forte_concerned.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image forte happy = im.FactorScale("sprites/characters/forte_happy.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image forte veryhappy = im.FactorScale("sprites/characters/forte_veryhappy.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image portrait forte normal = im.FactorScale("portraits/forte_normal.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait forte serious = im.FactorScale("portraits/forte_serious.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait forte worried = im.FactorScale("portraits/forte_worried.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait forte sad = im.FactorScale("portraits/forte_worried.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)

# Vanilla
image vanilla normal = im.FactorScale("sprites/characters/vanilla_normal.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image vanilla normal2 = im.FactorScale("sprites/characters/vanilla_normal2.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image vanilla focused = im.FactorScale("sprites/characters/vanilla_focused.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image vanilla happy2 = im.FactorScale("sprites/characters/vanilla_happy2.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image vanilla concerned2 = im.FactorScale("sprites/characters/vanilla_concerned2.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image vanilla sidewaysglance = im.FactorScale("sprites/characters/vanilla_sidewaysglance.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image vanilla shocked = im.FactorScale("sprites/characters/vanilla_shocked.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image vanilla stressed = im.FactorScale("sprites/characters/vanilla_stressed.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image portrait vanilla normal = im.FactorScale("portraits/vanilla_normal.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)

# Chitose
image chitose normal = im.FactorScale("sprites/characters/chitose_normal.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image chitose smallsmile = im.FactorScale("sprites/characters/chitose_smallsmile.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image chitose happy = im.FactorScale("sprites/characters/chitose_happy.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image chitose veryhappy = im.FactorScale("sprites/characters/chitose_veryhappy.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image chitose surprised = im.FactorScale("sprites/characters/chitose_surprised.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image chitose startled = im.FactorScale("sprites/characters/chitose_startled.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image chitose shocked = im.FactorScale("sprites/characters/chitose_shocked.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image portrait chitose normal = im.FactorScale("portraits/chitose_normal.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait chitose annoyed = im.FactorScale("portraits/chitose_annoyed.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)

# Almo
image almo normal = im.FactorScale("sprites/characters/almo_normal.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image almo happy = im.FactorScale("sprites/characters/almo_happy.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image almo surprised = im.FactorScale("sprites/characters/almo_surprised.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image almo sad = im.FactorScale("sprites/characters/almo_sad.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image almo shocked = im.FactorScale("sprites/characters/almo_shocked.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image portrait almo normal = im.FactorScale("portraits/almo_normal.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait almo surprised = im.FactorScale("portraits/almo_surprised.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait almo shocked = im.FactorScale("portraits/almo_shocked.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)

# Coco
image coco normal = im.FactorScale("sprites/characters/coco_normal.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image coco happy = im.FactorScale("sprites/characters/coco_happy.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image coco surprised = im.FactorScale("sprites/characters/coco_surprised.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image coco sad = im.FactorScale("sprites/characters/coco_sad.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image coco shocked = im.FactorScale("sprites/characters/coco_shocked.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image portrait coco normal = im.FactorScale("portraits/coco_normal.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait coco surprised = im.FactorScale("portraits/coco_surprised.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait coco shocked = im.FactorScale("portraits/coco_shocked.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)

# Noah
image noah normal = im.FactorScale("sprites/characters/noah_normal.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image noah serious = im.FactorScale("sprites/characters/noah_serious.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image noah hurm = im.FactorScale("sprites/characters/noah_hurm.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image noah thinking = im.FactorScale("sprites/characters/noah_thinking.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image portrait noah normal = im.FactorScale("portraits/noah_normal.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait noah hurm = im.FactorScale("portraits/noah_hurm.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)
image portrait noah thinking = im.FactorScale("portraits/noah_thinking.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)

# Shiva
image shiva normal = im.FactorScale("sprites/characters/shiva_normal.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image shiva serious = im.FactorScale("sprites/characters/shiva_serious.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image shiva happy = im.FactorScale("sprites/characters/shiva_happy.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image shiva veryhappy = im.FactorScale("sprites/characters/shiva_veryhappy.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image shiva thinking = im.FactorScale("sprites/characters/shiva_thinking.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image shiva surprised = im.FactorScale("sprites/characters/shiva_surprised.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image portrait shiva normal = im.FactorScale("portraits/shiva_normal.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)

# Luft
image luft normal = im.FactorScale("sprites/characters/luft_normal.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image luft thinking = im.FactorScale("sprites/characters/luft_thinking.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image luft serious = im.FactorScale("sprites/characters/luft_serious.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image luft amused = im.FactorScale("sprites/characters/luft_amused.png", SPRITE_SCALE_X, SPRITE_SCALE_Y)
image portrait luft normal = im.FactorScale("portraits/luft_normal.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)

# misc.
image portrait operator normal = im.FactorScale("portraits/operator_normal.png", PORTRAIT_SCALE_X, PORTRAIT_SCALE_Y)

# ============================================================
# MUSIC
# ============================================================

# this is a list of all tracks the music player in appendix has
init -1 python:
    playlist = [
        "Title Theme (GA1)",
        "Milfeulle's Theme",
        "Ranpha's Theme",
        "Mint's Theme",
        "Forte's Theme",
        "Vanilla's Theme",
        "Chitose's Theme",
        "Milfeulle's Theme (Arranged)",
        "Ranpha's Theme (Arranged)",
        "Mint's Theme (Arranged)",
        "Forte's Theme (Arranged)",
        "Vanilla's Theme (Arranged)",
        "Chitose's Theme (Arranged)",
        "Companions",
        "A Peaceful Time",
        "Premonition of Love",
        "The Angel Wing Appears",
        "Reminiscence",
        "An Obscure Unease",
        "Recalcitrant Grief",
        "Shiva",
        "Elsior",
        "Bridge",
        "Briefing",
        "Time To Fight",
        "The Angel Wing Fights",
        "The Threat of the Val-Fasc",
    ]
    
    playlistRelativePaths = []
    for track in playlist:
        playlistRelativePaths.append("music/" + track + ".ogg")
        

# ============================================================
# CHARACTER DEFINITIONS
# ============================================================
define tact = Character('Tact', show_side_image="portrait tact normal", show_two_window=True, ctc="ctc", ctc_position="fixed")
define tact_amused = Character('Tact', show_side_image="portrait tact amused", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define tact_serious = Character('Tact', show_side_image="portrait tact serious", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define tact_aggressive = Character('Tact', show_side_image="portrait tact aggressive", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define tact_sweating = Character('Tact', show_side_image="portrait tact sweating", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define tact_oh = Character('Tact', show_side_image="portrait tact oh", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define tact_surprised = Character('Tact', show_side_image="portrait tact surprised", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define tact_stressed = Character('Tact', show_side_image="portrait tact stressed", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define tact_angry = Character('Tact', show_side_image="portrait tact angry", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define tact_oneeye = Character('Tact', show_side_image="portrait tact oneeye", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define tact_crying = Character('Tact', show_side_image="portrait tact crying", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define tact_happy = Character('Tact', show_side_image="portrait tact happy", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")

define lester = Character('Lester', show_side_image="portrait lester normal", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define lester_aggressive = Character('Lester', show_side_image="portrait lester aggressive", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define lester_serious = Character('Lester', show_side_image="portrait lester serious", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define lester_grim = Character('Lester', show_side_image="portrait lester grim", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define lester_relaxed = Character('Lester', show_side_image="portrait lester relaxed", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define lester_stressed = Character('Lester', show_side_image="portrait lester stressed", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")

define milfeulle = Character('Milfeulle', show_side_image="portrait milfeulle normal", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define milfeulle_serious = Character('Milfeulle', show_side_image="portrait milfeulle serious", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define milfeulle_happy = Character('Milfeulle', show_side_image="portrait milfeulle happy", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define milfeulle_sad = Character('Milfeulle', show_side_image="portrait milfeulle sad", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")

define ranpha = Character('Ranpha', show_side_image="portrait ranpha normal", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define ranpha_serious = Character('Ranpha', show_side_image="portrait ranpha serious", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define ranpha_aggressive = Character('Ranpha', show_side_image="portrait ranpha aggressive", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define ranpha_sad = Character('Ranpha', show_side_image="portrait ranpha sad", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define ranpha_worried = Character('Ranpha', show_side_image="portrait ranpha worried", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")

define mint = Character('Mint', show_side_image="portrait mint normal", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define mint_angry = Character('Mint', show_side_image="portrait mint angry", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")

define forte = Character('Forte', show_side_image="portrait forte normal", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define forte_serious = Character('Forte', show_side_image="portrait forte serious", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define forte_worried = Character('Forte', show_side_image="portrait forte worried", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define forte_sad = Character('Forte', show_side_image="portrait forte sad", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")

define vanilla = Character('Vanilla', show_side_image="portrait vanilla normal", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")

define chitose = Character('Chitose', show_side_image="portrait chitose normal", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define chitose_annoyed = Character('Chitose', show_side_image="portrait chitose annoyed", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")

define almo = Character('Almo', show_side_image="portrait almo normal", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define almo_surprised = Character('Almo', show_side_image="portrait almo surprised", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define almo_shocked = Character('Almo', show_side_image="portrait almo shocked", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")

define coco = Character('Coco', show_side_image="portrait coco normal", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define coco_surprised = Character('Coco', show_side_image="portrait coco surprised", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define coco_shocked = Character('Coco', show_side_image="portrait coco shocked", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")

define noah = Character('Noah', show_side_image="portrait noah normal", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define noah_hurm = Character('Noah', show_side_image="portrait noah hurm", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define noah_thinking = Character('Noah', show_side_image="portrait noah thinking", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")

define shiva = Character('Shiva', show_side_image="portrait shiva normal", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define luft = Character('Luft', show_side_image="portrait luft normal", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")

define operator = Character('Operator', show_side_image="portrait operator normal", show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")

define newscaster = Character('Newscaster', show_two_window=True, ctc=DynamicDisplayable(renderCTC))

define all = Character('All', show_two_window=True, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")
define nvlChar = Character("", kind=nvl, ctc=DynamicDisplayable(renderCTC), ctc_position="fixed")

# ============================================================
# MISSIONS
# ============================================================
init python:
    colors = {
        "red":(1,0.1,0.1),
        "orange":(1,0.5,0.1),
        "green":(0.1,1,0.1),
        "blue":(0.1,0.1,1),
        "skyblue":(0.1,1,1),
        "pink":(1,0.5,0.75),
    }    
    
    def tintImage(img, color):
        r, g, b = color
        return im.MatrixColor(img, im.matrix.tint(r, g, b))
        
    def makeIcon(img, xsize, ysize, color):
        toScale = None
        if color != None:
            toScale = tintImage(img, colors[color])
        else:
            toScale = img
        return im.Scale(toScale, xsize, ysize)

image reticule blue = makeIcon("gui/icons/reticule.png", 32, 32, "skyblue")
image reticule green = makeIcon("gui/icons/reticule.png", 32, 32, "green")
image reticule red = makeIcon("gui/icons/reticule.png", 32, 32, "green")

image icon triangle = makeIcon("gui/icons/triangle.png", 24, 24, None)
image icon triangle skyblue = makeIcon("gui/icons/triangle.png", 24, 24, "skyblue")
image icon triangle big = makeIcon("gui/icons/triangle.png", 32, 32, None)
image icon triangle big skyblue = makeIcon("gui/icons/triangle.png", 32, 32, "skyblue")
image icon triangle big pink = makeIcon("gui/icons/triangle.png", 32, 32, "pink")

image icon arrowhead = makeIcon("gui/icons/arrowhead.png", 24, 24, None)
image icon arrowhead skyblue = makeIcon("gui/icons/arrowhead.png", 24, 24, "skyblue")
image icon arrowhead red = makeIcon("gui/icons/arrowhead.png", 24, 24, "red")
image icon arrowhead orange = makeIcon("gui/icons/arrowhead.png", 24, 24, "orange")
image icon arrowhead big = im.Scale("gui/icons/arrowhead.png", 32, 32)

image icon yngcommando = makeIcon("gui/icons/yngcommando.png", 24, 24, None)
image icon yngtiger = makeIcon("gui/icons/yngtiger.png", 24, 24, None)

image unitpic yngcommando = "gui/unitpics/yngcommando.png"
image unitpic yngtiger = "gui/unitpics/yngtiger.png"
image unitpic enclavestar = "gui/unitpics/enclavestar.png"