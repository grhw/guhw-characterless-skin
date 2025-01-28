import utils

text_list = {
    "ranking-accuracy.png": ["Accuracy",90],
    "ranking-maxcombo.png": ["Combo",90],
    "ranking-perfect.png": ["FC",90],
}

def create_texts():
    for fn in text_list.keys():
        text,size = text_list[fn]
        
        utils.save_hd_sd(utils.text_to_image(text,"assets/ComfortaaBold.ttf",size,"#FFFFFF",True),f"build/{fn}")