import utils
from PIL import Image

def create_circles():
    hit_circle = Image.open("assets/gameplay/standard/hit-circle.png")
    approach = Image.open("assets/gameplay/standard/approach.png")
    
    insta_fading_circle = utils.resize_by_multiplier(hit_circle,1/0.8)
    
    for i in range(10):
        utils.save_hd_sd(insta_fading_circle,f"build/default-{i}.png")
    
    utils.save_hd_sd(approach,"build/approachcircle.png")
    utils.remove("build/hitcircle.png")
    utils.remove("build/hitcircleoverlay.png")