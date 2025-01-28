import utils

to_remove = [
    "followpoint.png",
    "lighting.png",
    "sliderendcircle.png",
    "sliderendcircleoverlay.png",
    "comboburst.png",
    "star2.png",
    "masking-border.png",
    "ranking-title.png",
    
    "spinner-glow.png",
    "spinner-middle.png",
    "spinner-middle2.png",
    "spinner-top.png",
    "spinner-metre.png",
    "scorebar-bg.png",
    "scorebar-colour.png",
    "inputoverlay-background.png"
]

def remove_all():
    for i in to_remove:
        utils.remove(f"build/{i}")