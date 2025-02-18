import utils
from PIL import Image

rankings = [
    "D",
    "C",
    "B",
    "A",
    "S",
    "SH",
    "X",
    "XH",
]
colors = {
    "D": "#8f0000",
    "C": "#9600c4",
    "B": "#0080ca",
    "A": "#00ff80",
    "S": "#ffd900",
    "X": "#dcb0ff",
    
    "H": "#aec0c9",
}

def create_ranks():
    for rank in rankings:
        image = utils.text_to_image(rank[0],"assets/Jua-Regular.ttf",780,colors[rank[-1]],True)
        small_image = utils.text_to_image(rank[0],"assets/Jua-Regular.ttf",130,colors[rank[-1]],False)
        
        w,h = image.size
        moved = Image.new("RGBA",(w+360,h+11))
        moved.paste(image,(0,11),mask=image)
        
        utils.save_hd_sd(utils.resize_to_resolution(small_image,85,85),f"build/ranking-{rank}-small.png")
        utils.save_hd_sd(moved,f"build/ranking-{rank}.png")