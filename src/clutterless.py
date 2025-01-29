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
    "inputoverlay-background.png",
    
    "mania-stage-hint.png",
    "mania-stage-bottom.png",
    "mania-stage-light.png",
    "mania-warningarrow.png",
    "lightingL.png",
    "lightingN.png",
    
    "taiko-glow.png",
    "taiko-bar-right-glow.png",
    "taiko-slider.png",
    "taiko-slider-fail.png",
    "pippidonkiai.png"
    "pippidonidle.png"
    "pippidonfail.png"
    "pippidonclear.png"
]

def remove_all():
    for i in to_remove:
        utils.remove(f"build/{i}")