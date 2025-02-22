import json
from coloraide import Color
from PIL import Image
from config import get_config
import utils


def note(main_color):
    converted = main_color.convert("srgb").coords()
    contrast = (
        main_color
        .filter("brightness", 0.45)
        .filter("saturate", 1.2)
        .convert("srgb")
        .coords()
    )
    inner = Image.open("assets/gameplay/mania/inner.png")
    outer = Image.open("assets/gameplay/mania/outer.png")

    utils.tint_image(inner, converted)
    utils.tint_image(outer, contrast)

    outer.paste(inner, (0, 0), inner)

    return outer

def both(main_color):
    return note(Color.new(main_color)), note(Color.new(main_color).filter("hue-rotate",-90))

colors = get_config("mania")


def create_mania():
    inner,inner_hold = both(colors["2"])
    outer,outer_hold = both(colors["1"])
    special,special_hold = both(colors["S"])
    rec = Image.open("assets/gameplay/mania/rec.png")
    rec_held_overlay = Image.open("assets/gameplay/mania/rec_held.png")

    hold = Image.open("assets/gameplay/mania/hold.png")
    hold_end = Image.open("assets/gameplay/mania/hold_end.png")

    utils.save_hd_sd(outer, "build/mania-note1.png")
    utils.save_hd_sd(outer_hold, "build/mania-note1H.png")

    utils.save_hd_sd(inner, "build/mania-note2.png")
    utils.save_hd_sd(inner_hold, "build/mania-note2H.png")

    utils.save_hd_sd(special, "build/mania-noteS.png")
    utils.save_hd_sd(special_hold, "build/mania-noteSH.png")

    utils.save_hd_sd(special, "build/mania-noteS.png")
    utils.save_hd_sd(special_hold, "build/mania-noteSH.png")

    for i in "12S":
        utils.save_hd_sd(rec, f"build/mania-key{i}.png")
        this_rec_held_overlay = rec_held_overlay.copy()
        this_rec = rec.copy()
        utils.tint_image(
            this_rec_held_overlay, Color(colors[i]).convert("srgb").coords()
        )
        this_rec.paste(this_rec_held_overlay, (0, 0), this_rec_held_overlay)
        utils.save_hd_sd(this_rec, f"build/mania-key{i}D.png")

        utils.save_hd_sd(hold, f"build/mania-note{i}L.png")
        utils.save_hd_sd(hold_end, f"build/mania-note{i}T.png")
