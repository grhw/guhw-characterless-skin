from coloraide import Color
from PIL import Image
import utils

def note(main_color):
    converted = Color.new(main_color).convert("srgb").coords()
    contrast = Color.new(main_color).filter("brightness",0.45).filter("saturate",1.2).convert("srgb").coords()
    inner = Image.open("assets/gameplay/mania/inner.png")
    outer = Image.open("assets/gameplay/mania/outer.png")
        
    utils.tint_image(inner,converted)
    utils.tint_image(outer,contrast)
    
    outer.paste(inner,(0,0),inner)
    
    return outer

def create_mania():
    inner = note("#ACC9FF")
    outer = note("#FFE1AB")
    special = note("#FFABF7")
    rec = Image.open("assets/gameplay/mania/rec.png")
    rec_held = Image.open("assets/gameplay/mania/rec_held.png")
    
    hold = Image.open("assets/gameplay/mania/hold.png")
    hold_end = Image.open("assets/gameplay/mania/hold_end.png")
    
    utils.save_hd_sd(outer,"build/mania-note1.png")
    utils.save_hd_sd(outer,"build/mania-note1H.png")
    
    utils.save_hd_sd(inner,"build/mania-note2.png")
    utils.save_hd_sd(inner,"build/mania-note2H.png")
    
    utils.save_hd_sd(special,"build/mania-noteS.png")
    utils.save_hd_sd(special,"build/mania-noteSH.png")
    
    utils.save_hd_sd(special,"build/mania-noteS.png")
    utils.save_hd_sd(special,"build/mania-noteSH.png")
    
    for i in "12S":
        utils.save_hd_sd(rec,f"build/mania-key{i}.png")
        utils.save_hd_sd(rec_held,f"build/mania-key{i}D.png")
        
        utils.save_hd_sd(hold,f"build/mania-note{i}L.png")
        utils.save_hd_sd(hold_end,f"build/mania-note{i}T.png")