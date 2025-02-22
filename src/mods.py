import os

from coloraide import Color
from config import get_config
import utils
from PIL import Image

mods = {
    "autoplay": "AT",
    "cinema": "CN",
    "doubletime": "DT",
    "easy": "EZ",
    "fadein": "FI",
    "flashlight": "FL",
    "halftime": "HT",
    "hardrock": "HR",
    "hidden": "HD",
    "keycoop": "CO",
    "mirror": "MR",
    "nightcore": "NC",
    "nofail": "NF",
    "perfect": "PF",
    "random": "RD",
    "relax": "RX",
    "relax2": "AP",
    "scorev2": "V2",
    "spunout": "SO",
    "suddendeath": "SD",
    "targetpractice": "TP",
}

colors = {
    "#5eff00": "eznfhtco",
    "#ff0000": "hr",
    "#ff8800": "sd",
    "#ffe600": "pf",
    "#9900ff": "nchdcnrd",
    "#0084ff": "dtrxapmr",
    "#888888": "flfi",
    "#888888": "atv2so",
}

for i in range(10):
    mods[f"key{i}"] = f"{i}K"
fonts = get_config("fonts")

def create_mods():
    icons = os.listdir("assets/mods/icons")
    for name in mods.keys():
        short = mods[name]
        background = Image.open("assets/mods/background.png")
        text = utils.text_to_image(short,fonts["mods"],60,"#FFFFFF",True)
        text.thumbnail((170,85))
        background.paste(text,(0,85),text)
        
        icon = False
        if short.lower() + ".png" in icons:
            icon = Image.open(f"assets/mods/icons/{short.lower()}.png")
        elif short.lower().endswith("k"):
            icon = Image.open(f"assets/mods/icons/key.png")
        
        icon_color = "#ffffff"
        for col in colors.keys():
            col_mods = colors[col]
            if short.lower() in col_mods:
                icon_color = col
        
        if icon:
            icon.thumbnail((170,45))
            utils.tint_image(icon,Color.new(icon_color).convert("srgb").coords())
            background.paste(icon,(0,20),icon)

        
        utils.save_hd_sd(background,f"build/selection-mod-{name}.png")