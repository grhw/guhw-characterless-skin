import utils

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
for i in range(10):
    mods[f"key{i}"] = f"{i}K"

def create_mods():
    for name in mods.keys():
        short = mods[name]
        utils.save_hd_sd(utils.text_to_image(short,"assets/ComfortaaBold.ttf",100,"#FFFFFF",True),f"build/selection-mod-{name}.png")