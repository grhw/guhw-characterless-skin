import utils

to_remove = [
    "followpoint.png",
    "lighting.png",
    "sliderendcircle.png",
    "sliderendcircleoverlay.png",
    "comboburst.png",
]

def remove_all():
    for i in to_remove:
        utils.remove(f"build/{i}")