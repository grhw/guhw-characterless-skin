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
]

def remove_all():
    for i in to_remove:
        utils.remove(f"build/{i}")