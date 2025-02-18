import utils

def char(c):
    img = utils.text_to_image(c,"assets/Modak-Regular.ttf",90,"#ffffff",False)
    w,h = img.size
    
    img = img.crop((0,h/8,w,h-(h/3)))
    
    utils.save_hd_sd(img,f"build/score-{c.replace("%","percent").replace(".","dot").replace(",","comma")}.png")

def create_font():
    for n in range(10):
        char(str(n))
    for l in "%.x,":
        char(l)