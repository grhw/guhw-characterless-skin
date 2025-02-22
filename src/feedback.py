from config import get_config
import utils
from PIL import Image
import math

feedback = get_config("feedback")
fonts = get_config("fonts")


def easeInQuad(t):
    return t * t
def easeOutExpo(t):
    return -math.pow(2, -10 * t) + 1

def animate_for(frames, source, new):
    utils.remove(utils.add_before(new, f"-{frames}"))
    w,h = source.size
    for i in range(frames):
        rev = ((1 - easeOutExpo(i / frames)) * 2) + 1
        rot = easeInQuad(i / frames) * 45
        image = source.resize((round(w*rev),round(h*rev)),Image.Resampling.BILINEAR).rotate(rot)
        utils.save_hd_sd(
            utils.multiply_alpha(image, (1 - easeInQuad(i / frames))),
            utils.add_before(new, f"-{i}"),
        )


def all_modes(image, std_name):
    mania_name = std_name.replace("hit", "mania-hit")
    taiko_name = std_name.replace("hit", "taiko-hit")
    utils.save_hd_sd(image, std_name)
    utils.save_hd_sd(image, mania_name)
    utils.save_hd_sd(image, taiko_name)


def create_feedback():
    animate_for(
        30, Image.open("assets/gameplay/standard/feedback-miss.png"), "build/hit0.png"
    )

    animate_for(
        20, Image.open("assets/gameplay/standard/feedback-50.png"), "build/hit50.png"
    )

    animate_for(
        20, Image.open("assets/gameplay/standard/feedback-100.png"), "build/hit100.png"
    )
    animate_for(
        20, Image.open("assets/gameplay/standard/feedback-100.png"), "build/hit100k.png"
    )

    utils.remove("build/hit300-0.png")
    utils.remove("build/hit300k-0.png")
    utils.remove("build/hit300g-0.png")

    perf2 = utils.text_to_image(
        feedback["300plus"], fonts["feedback"], 90, "#d6e6ff", True
    )
    perf = utils.text_to_image(feedback["300"], fonts["feedback"], 90, "#93beff", True)
    great = utils.text_to_image(feedback["200"], fonts["feedback"], 90, "#5fff5f", True)
    good2 = utils.text_to_image(feedback["100plus"], fonts["feedback"], 90, "#a6f9ff", True)
    good = utils.text_to_image(feedback["100"], fonts["feedback"], 90, "#5ff4ff", True)
    okay = utils.text_to_image(feedback["50"], fonts["feedback"], 90, "#4335ff", True)
    miss = utils.text_to_image(feedback["0"], fonts["feedback"], 90, "#ff3535", True)

    all_modes(perf, "build/hit300.png")
    all_modes(perf2, "build/hit300k.png")
    all_modes(perf2, "build/hit300g.png")

    all_modes(great, "build/hit200.png")

    all_modes(good, "build/hit100.png")
    all_modes(good2, "build/hit100k.png")

    all_modes(okay, "build/hit50.png")

    all_modes(miss, "build/hit0.png")
