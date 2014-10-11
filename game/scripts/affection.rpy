# ============================================================
# Affection manager
# ============================================================

init python:
    # note Tact is considered an Angel just to fill the 0 index; don't expect him to be supported for any Angel-specific functions
    
    # variables
    partner = None;
    
    angelsByIndex = ["Tact", "Milfeulle", "Ranpha", "Mint", "Forte", "Vanilla", "Chitose"]
    angelNameToIndex = {"Milfeulle":1, "Ranpha":2, "Mint":3, "Forte":4, "Vanilla":5, "Chitose":6}
    
    moods = [0, 0, 0, 0, 0, 0, 0]       # 0 = normal, -1 = sad, 1 = happy, 2 = very happy
    trust = [0, 0, 0, 0, 0, 0, 0]       # runs from 0 to 20
    angelAbsent = [False, False, False, False, False, False, False]
    
    affectionSounds = {
        -2:"sfx/relationship_down_super.wav",
        -1:"sfx/relationship_down.wav",
        #0:
        1:"sfx/relationship_up.wav",
        2:"sfx/relationship_up_super.wav",
    }
    
    moodStringsByInt = {-1:"sad", 0:"normal", 1:"happy", 2:"veryhappy"}
    
    whaleReportImages = {}
    whaleReportImagesFrame = {}
    whaleReportImagesAbsent = {}
    for i in range(0,7):
        whaleReportImages[i] = {}
        whaleReportImagesFrame[i] = im.FactorScale("gui/whalereport/" + angelsByIndex[i].lower() + "_frame.png", SCALE_X, SCALE_Y)
        whaleReportImagesAbsent[i] = im.FactorScale("gui/whalereport/" + angelsByIndex[i].lower() + "_absent.png", SCALE_X, SCALE_Y)
        for j in range(-1,2):
            whaleReportImages[i][j] = im.FactorScale("gui/whalereport/" + angelsByIndex[i].lower() + "_mood_" + moodStringsByInt[j] + ".png", SCALE_X, SCALE_Y)
    
    # functions
    def getAngelIndexByName(name):
        return angelNameToIndex[name]
    
    def getAngelName(index):
        return angelsByIndex[index]
    
    def setAngelMood(index, val):
        if val > 2:
            val = 2
        elif val < -1:
            val = -1
        moods[index] = val
    
    def setAngelTrust(index, val):
        if val > 20:
            val = 20
        elif val < 0:
            val = 0
        trust[index] = val
        
    def modifyAngelAffection(index, val):
        if val == 0:
            return
        elif val > 2:
            val = 2
        elif val < -1:
            val = -1
        moods[index] = moods[index] + val
        trust[index] = trust[index] + val
        
label angelMoodEvent(index, delta):
    $ modifyAngelAffection(index, delta)
    play sound affectionSounds[delta]