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

shutil.rmtree("build", ignore_errors=True)
os.mkdir("build")

for icon in os.listdir("assets/icons/"):
    icons.create(f"assets/icons/{icon}", f"build/mode-{icon}")

rankings.create_ranks()
instafade.create_circles()
clutterless.remove_all()
feedback.create_feedback()
font.create_font()
text.create_texts()
mods.create_mods()
mania.create_mania()

menu_back = Image.open("assets/icons/back.png")
template = Image.new("RGBA",menu_back.size)

def easeInCubic(t):
    return t * t * t
def easeOutCubic(t):
    t -= 1
    return t * t * t + 1

frames = 120
for i in range(frames):
    if i < frames/2:
        x = (1 - easeInCubic(i/(frames/2)))
    else:
        x = easeOutCubic((i-(frames/2))/(frames/2))
    use = template.copy()
    use.paste(menu_back,(int(x*100),0))
    utils.save_hd_sd(
        use,
        utils.add_before("build/menu-back.png", f"-{i}"),
    )

for to_copy in os.walk("assets/copy/"):
    for i in to_copy[2]:
        if i.endswith(".png"):
            utils.save_hd_sd(Image.open(f"{to_copy[0]}/{i}"), f"build/{i}")
        else:
            shutil.copy(f"{to_copy[0]}/{i}", "build/")

ver = "1.12.0"  # input("x.x.x\n")

skin_ini.generate(ver)
print("\n")
os.makedirs("dist", exist_ok=True)
os.system(f'zip -r "dist/{ver}_guhw_insta-fading_read.osk" build/')
