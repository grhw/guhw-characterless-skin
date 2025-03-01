from PIL import Image
from coloraide import Color
from config import get_config
import utils

circle_scale_size_mult = get_config("other")["circleVisualSizeMultiplier"]
fonts = get_config("fonts")


def create_circles():
    hit_circle = Image.open("assets/gameplay/standard/hit-circle.png")
    hit_circle_alt = Image.open("assets/gameplay/standard/hit-circle-alt.png")
    approach = Image.open("assets/gameplay/standard/approach.png")

    insta_fading_circle = utils.resize_by_multiplier(
        hit_circle, (1 / 0.8) * circle_scale_size_mult
    )
    insta_fading_circle_alt_c = utils.resize_by_multiplier(
        hit_circle_alt, (1 / 0.8) * circle_scale_size_mult
    )
    insta_fading_approach = utils.resize_by_multiplier(approach, circle_scale_size_mult)

    # colors = list(Color("").range_to(Color(""),10))
    colors = Color.steps(["#51ff00", "#a200ff"], steps=10, space="hsl")

    for i in range(0, 10):
        color = colors[i].convert("srgb").coords()
        print(color)
        insta_fading_circle_alt = insta_fading_circle_alt_c.copy()
        utils.tint_image(insta_fading_circle_alt, color)
        insta_fading_circle_alt.paste(insta_fading_circle, (0, 0), insta_fading_circle)

        number = utils.text_to_image(str(i), fonts["hit-circle"], 90, "#ffffff", True)

        w, h = number.size
        nw, nh = insta_fading_circle_alt.size
        insta_fading_circle_alt.paste(
            number, ((nw // 2) - (w // 2), ((nh // 2) - (h // 2)) + 5), number
        )

        utils.save_hd_sd(insta_fading_circle_alt, f"build/default-{i}.png")

    utils.save_hd_sd(insta_fading_approach, "build/approachcircle.png")
    utils.remove("build/hitcircle.png")
    utils.remove("build/hitcircleoverlay.png")
