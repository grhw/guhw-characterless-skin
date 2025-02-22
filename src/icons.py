import utils
from PIL import Image


def create(path, new):
    image = Image.open(path)
    utils.save_hd_sd(image, new)
    utils.save_hd_sd(
        utils.resize_to_resolution(image, 256, 256), utils.add_before(new, "-med")
    )
    utils.save_hd_sd(
        utils.resize_to_resolution(image, 64, 64), utils.add_before(new, "-small")
    )
