from config import get_config
import utils

text_list = get_config("text-image")
fonts = get_config("fonts")


def create_texts():
    for fn in text_list.keys():
        text, size = text_list[fn]

        utils.save_hd_sd(
            utils.text_to_image(text, fonts["text-image"], size, "#FFFFFF", True),
            f"build/{fn}",
        )
