# ============================================================
# Appendix stuff
# ============================================================
# N.B. Actual screens are in screens.rpy, as usual

# TBD
init python:
    galleries = {}
    tracks = [
        None,
    ]
    
    for i in range(0,6):
        galleries[i] = Gallery()
        galleries[i].locked_button = "appendixitem off"
        galleries[i].idle_border = "appendixitem"
        galleries[i].hover_border = "appendixitem highlight"