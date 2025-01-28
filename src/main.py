import os
import shutil
import clutterless
import feedback
import icons
import instafade
import rankings
import utils
from PIL import Image

for icon in os.listdir("assets/icons/"):
    icons.create(f"assets/icons/{icon}",f"build/mode-{icon}")

rankings.create_ranks()
instafade.create_circles()
clutterless.remove_all()
feedback.create_feedback()

for to_copy in os.walk("assets/copy/"):
    for i in to_copy[2]:
        if i.endswith(".png"):
            utils.save_hd_sd(Image.open(f"{to_copy[0]}/{i}"),f"build/{i}")
        else:
            shutil.copy(f"{to_copy[0]}/{i}","build/")