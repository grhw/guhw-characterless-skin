import utils
from PIL import Image

def create_mania():
    inner = Image.open("assets/gameplay/mania/inner.png")
    outer = Image.open("assets/gameplay/mania/outer.png")
    special = Image.open("assets/gameplay/mania/special.png")
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
        utils.save_hd_sd(rec_held,f"build/mania-key{i}d.png")
        
        utils.save_hd_sd(hold,f"build/mania-note{i}L.png")
        utils.save_hd_sd(hold_end,f"build/mania-note{i}T.png")