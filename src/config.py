import json

loaded = {}

config_files = [
    "clutterless",
    "feedback",
    "mania",
    "other",
    "rankings",
    "skin",
    "text-image",
]

for i in config_files:
    with open("assets/" + i + ".json", "r") as f:
        loaded[i] = json.loads(f.read())

with open("assets/fonts.json", "r") as f:
    font = json.loads(f.read())
    for k in font.keys():
        font[k] = "assets/fonts/" + font[k]

    loaded["fonts"] = font


def get_config(name):
    return loaded[name]
