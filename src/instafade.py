from PIL import Image,ImageChops
from coloraide import Color
import utils

def tint_image(image, tint_color):
    pixels = image.load()
    r_,g_,b_ = tint_color
    r,g,b = int(r_*255),int(g_*255),int(b_*255)
    
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            _,_,_,a = pixels[x, y]
            pixels[x, y] = (r,g,b,a)

def create_circles():
    hit_circle = Image.open("assets/gameplay/standard/hit-circle.png")
    hit_circle_alt = Image.open("assets/gameplay/standard/hit-circle-alt.png")
    approach = Image.open("assets/gameplay/standard/approach.png")
    
    insta_fading_circle = utils.resize_by_multiplier(hit_circle,1/0.8)
    insta_fading_circle_alt = utils.resize_by_multiplier(hit_circle_alt,1/0.8)
    
    #colors = list(Color("").range_to(Color(""),10))
    colors = Color.steps(['#0091FF', '#ffffff', '#a200ff'], steps=10, space='hsl')

    
    for i in range(0,10):
        color = colors[i].convert("srgb").coords()
        print(color)
        tint_image(insta_fading_circle_alt,color)
        insta_fading_circle.paste(insta_fading_circle_alt,(0,0),insta_fading_circle_alt)
        utils.save_hd_sd(insta_fading_circle,f"build/default-{i}.png")
    
    utils.save_hd_sd(approach,"build/approachcircle.png")
    utils.remove("build/hitcircle.png")
    utils.remove("build/hitcircleoverlay.png")

create_circles()