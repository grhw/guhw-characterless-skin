import utils

def char(c):
    utils.save_hd_sd(utils.text_to_image(c,"assets/ComfortaaBold.ttf",90,"#ffffff",False),f"build/score-{c.replace("%","percent").replace(".","dot").replace(",","comma")}.png")

def create_font():
    for n in range(10):
        char(str(n))
    for l in "%.x,":
        char(l)