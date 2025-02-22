from config import get_config
import utils
import json

text_list = get_config("text-image")

def create_texts():
    for fn in text_list.keys():
        text,size = text_list[fn]
        
        utils.save_hd_sd(utils.text_to_image(text,"assets/ComfortaaBold.ttf",size,"#FFFFFF",True),f"build/{fn}")