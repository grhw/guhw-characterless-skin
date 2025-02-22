import utils
import json

with open("assets/text-image.json","r") as f:
    text_list = json.loads(f.read())

def create_texts():
    for fn in text_list.keys():
        text,size = text_list[fn]
        
        utils.save_hd_sd(utils.text_to_image(text,"assets/ComfortaaBold.ttf",size,"#FFFFFF",True),f"build/{fn}")