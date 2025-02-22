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
    with open("assets/" + i + ".json","r") as f:
        loaded[i] = json.loads(f.read())

def get_config(name):
    return loaded[name]