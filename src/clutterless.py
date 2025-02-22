import json
import utils

with open("assets/clutterless.json","r") as f:
    to_remove = json.loads(f.read())

def remove_all():
    for i in to_remove:
        utils.remove(f"build/{i}")