# ============================================================
# Missions manager
# ============================================================

# TODO: mission performance evaluator

# ============================================================
# data definitions
init python:
    import os
    
    unitLists = {
        "mission1_milfeulle":[
            {"type":"emblemframe", "xpos":0.495, "ypos":0.735, "heading":315, "number":1},
            {"type":"emblemframe", "xpos":0.54, "ypos":0.74, "heading":315, "number":2},
            {"type":"emblemframe", "xpos":0.51, "ypos":0.8, "heading":315, "number":4},
            {"type":"elsior", "xpos":0.57, "ypos":0.83, "heading":315},
            
            {"type":"yngcommando", "xpos":0.37, "ypos":0.32, "heading":135},
            {"type":"yngcommando", "xpos":0.39, "ypos":0.29, "heading":135},
            {"type":"yngcommando", "xpos":0.41, "ypos":0.26, "heading":135},
            {"type":"yngcommando", "xpos":0.22, "ypos":0.60, "heading":135},
            {"type":"yngcommando", "xpos":0.24, "ypos":0.57, "heading":135},
            {"type":"yngcommando", "xpos":0.26, "ypos":0.54, "heading":135},
            
            {"type":"yngtiger", "xpos":0.35, "ypos":0.26, "heading":135},
            {"type":"yngtiger", "xpos":0.37, "ypos":0.23, "heading":135},
            {"type":"yngtiger", "xpos":0.20, "ypos":0.54, "heading":135},
            {"type":"yngtiger", "xpos":0.22, "ypos":0.51, "heading":135},
            
            {"type":"enclavestar", "xpos":0.33, "ypos":0.21, "heading":135},
            {"type":"enclavestar", "xpos":0.18, "ypos":0.49, "heading":135},
        ]
    }
    
    unitTypeLists = {
        "mission1_milfeulle":[
            {"type":"elsior", "text":"Elsior"},
            {"type":"emblemframe", "text":"Angel Wing"},
            {"type":"yngcommando", "text":"UNK-F"},
            {"type":"yngtiger", "text":"UNK-B"},
            {"type":"enclavestar", "text":"UNK-CV"},
        ]
    }
    
    unitIconMap = {
            "emblemframe":"icon triangle skyblue",
            "elsior":"icon triangle big skyblue",
            "yngcommando":"icon arrowhead red",
            "yngtiger":"icon arrowhead orange",
            "enclavestar":"icon triangle big pink",
    }
    
    missionMoraleModifiers = {
        "mission1_milfeulle":[0,5,0,0,0,0,0]
    }
    
    battleLocations = {
            "mission1_milfeulle":"Transbaal",
    }
    
    #combatResults = {}
    lifetimeStats = {}
    
    for i in range(0,7):
        lifetimeStats[i] = {"kills":0, "killCost":0, "damage":0, "damageCost":0, "repair":0, "deaths":0}
    

# ============================================================
# functions
init python:
    import subprocess
    import sys
    import traceback

    SPRING_DIR = sys.path[0] + "/spring"           
    #SPRING_DIR = renpy.loader.transfn("../spring")
    EXECUTABLE_PATH = SPRING_DIR + "/spring.exe"
    SCRIPT_DIR = SPRING_DIR + "/scripts/"
    SCRIPT_FILENAME_TEMP = "_script.txt"
    SCRIPT_PATH_TEMP = SPRING_DIR + "/" + SCRIPT_FILENAME_TEMP
    RESULTS_PATH = SPRING_DIR + "/" + "results.py"
    RESULTS_PATH_COMPILED = SPRING_DIR + "/" + "results.pyo" # dunno if necessary to delete this as well

    sys.path.append(SPRING_DIR)

    MORALE_PER_TRUST_POINT = 1
    MORALE_PER_MOOD_POINT = 5
    
    def getMoraleModifier(missionName, index):
        return moods[index] * MORALE_PER_MOOD_POINT + trust[index] * MORALE_PER_TRUST_POINT + missionMoraleModifiers[missionName][index]
    
    # TODO: write modules, special flags
    def getStartscriptSubstDict(missionName):
        dict = {}
        for i in range(1,7):    # end of interval is open
            dict["morale"+str(i)] = 50 + getMoraleModifier(missionName, i)
            dict["partner"] = partner
        return dict
        
    def writeStartscript(missionName):
        scriptRaw = open(SCRIPT_DIR + missionName + ".txt", 'r')
        s = ""
        for line in scriptRaw:
            s += line
        s = s % getStartscriptSubstDict(missionName)
        scriptRaw.close()
        script = open(SCRIPT_PATH_TEMP, 'w')
        script.write(s)
        script.close()
    
    def removeResultFiles():
        try:
            os.remove(RESULTS_PATH)
            os.remove(RESULTS_PATH_COMPILED)
        except:
            print("Warning: failed to delete results file(s)")
            print("File may already not exist, or may be in use")
            
    def writeEnvVars():
        s = ""
        d = dict(os.environ)
        for key, value in sorted(d.items()):
            s += key + "=" + value + "\n"
        testFile = open(SPRING_DIR + "/envVars.txt", 'w');
        testFile.write(s)
        testFile.close()

label run_spring(missionName):
    $ location = None
    stop music fadeout 1
    scene bg blank with fadeSlow
    
    $ writeEnvVars()
    
    while True:
        python:
            removeResultFiles()
            writeStartscript(missionName)
            #envVars = dict(os.environ.copy())
            if "SDL_VIDEODRIVER" in os.environ:
                del os.environ["SDL_VIDEODRIVER"]
            subprocess.call([EXECUTABLE_PATH, SCRIPT_PATH_TEMP])
    
        # parse results
        # for some reason this breaks when moved to its own function >:|
        python:
            loadSuccess = False
            gameOver = False
            try:
                execfile(RESULTS_PATH)
                loadSuccess = True
            except:
                print("Failed to load data from Spring")
                traceback.print_stack()
            
            if loadSuccess:
                if combatResults["gameOver"] == True:
                    gameOver = True
                else:
                    for i in range(0,7):
                        if combatResults[i]["deaths"] == 1:
                            lifetimeStats[i]["deaths"] = lifetimeStats[i]["deaths"] + combatResults[i]["deaths"]
                            lifetimeStats[i]["kills"] = lifetimeStats[i]["kills"] + combatResults[i]["kills"]
                            lifetimeStats[i]["damage"] = lifetimeStats[i]["damage"] + combatResults[i]["damage"]
                            lifetimeStats[i]["repair"] = lifetimeStats[i]["repair"] + combatResults[i]["repair"]
                        else:
                            lifetimeStats[i]["kills"] = lifetimeStats[i]["kills"] + combatResults[i]["kills"]
                            lifetimeStats[i]["killCost"] = lifetimeStats[i]["killCost"] + combatResults[i]["killCost"]
                            lifetimeStats[i]["damage"] = lifetimeStats[i]["damage"] + combatResults[i]["damage"]
                            lifetimeStats[i]["damageCost"] = lifetimeStats[i]["damageCost"] + combatResults[i]["damageCost"]
                            lifetimeStats[i]["repair"] = lifetimeStats[i]["repair"] + combatResults[i]["repair"]
                        
                        print("{0}: {1} kills, {2} damage".format(getAngelName(i), combatResults[i]["kills"], combatResults[i]["damage"]))
                        
        if gameOver:
            return 0
        elif loadSuccess:
            return 1
        
        menu:
            "Error loading combat results."
            "Abort":
                return -1
            "Retry":
                $ print("Retrying mission")
            "Ignore":
                return 1
    
        