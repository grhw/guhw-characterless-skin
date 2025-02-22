import json
from config import get_config
import utils

to_remove = get_config("clutterless")

def remove_all():
    for i in to_remove:
        utils.remove(f"build/{i}")