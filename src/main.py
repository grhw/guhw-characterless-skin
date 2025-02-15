import clutterless
import instafade
import rankings
import feedback
import skin_ini
import icons
import utils
import mania
import font
import text
import mods

import os
import shutil
from PIL import Image

shutil.rmtree("build",ignore_errors=True)
os.mkdir("build")

for icon in os.listdir("assets/icons/"):
    icons.create(f"assets/icons/{icon}",f"build/mode-{icon}")

skin_ini.generate()
rankings.create_ranks()
instafade.create_circles()
clutterless.remove_all()
feedback.create_feedback()
font.create_font()
text.create_texts()
mods.create_mods()
mania.create_mania()

for to_copy in os.walk("assets/copy/"):
    for i in to_copy[2]:
        if i.endswith(".png"):
            utils.save_hd_sd(Image.open(f"{to_copy[0]}/{i}"),f"build/{i}")
        else:
            shutil.copy(f"{to_copy[0]}/{i}","build/")

print("\n")
os.system(f"zip -r \"dist/zzz__guhw_no-char_skin_V{input("v")}__zzz.osk\" build/")