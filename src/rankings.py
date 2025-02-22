from config import get_config
import utils
from PIL import Image

raw = get_config("rankings")
colors = raw["colors"]
rankings = list(raw["displays"].keys())
displays = raw["displays"]
colors["H"] = colors["Silver"]
fonts = get_config("fonts")


def create_ranks():
    for rank in rankings:
        image = utils.text_to_image(
            displays[rank], fonts["rankings"], 780, colors[rank[-1]], True
        )
        small_image = utils.text_to_image(
            displays[rank], fonts["rankings"], 130, colors[rank[-1]], False
        )

        w, h = image.size
        moved = Image.new("RGBA", (w + 360, h + 11))
        moved.paste(image, (0, 11), mask=image)

        utils.save_hd_sd(
            utils.resize_to_resolution(small_image, 85, 85),
            f"build/ranking-{rank}-small.png",
        )
        utils.save_hd_sd(moved, f"build/ranking-{rank}.png")
