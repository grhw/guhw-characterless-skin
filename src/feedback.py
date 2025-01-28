import utils
from PIL import Image

def animate_for(frames, path, new):
    image = Image.open(path)
    utils.remove(utils.add_before(new,f"-{frames}"))
    for i in range(frames):
        utils.save_hd_sd(image,utils.add_before(new,f"-{i}"))

def mania_standard(image,std_name):
    mania_name = std_name.replace("hit","mania-hit")
    utils.save_hd_sd(image,std_name)
    utils.save_hd_sd(image,mania_name)

def create_feedback():
    animate_for(15,"assets/gameplay/standard/feedback-miss.png","build/hit0.png")

    animate_for(10,"assets/gameplay/standard/feedback-50.png","build/hit50.png")
    
    animate_for(10,"assets/gameplay/standard/feedback-100.png","build/hit100.png")
    animate_for(10,"assets/gameplay/standard/feedback-100.png","build/hit100k.png")
    
    utils.remove("build/hit300-0.png")
    utils.remove("build/hit300k-0.png")
    utils.remove("build/hit300g-0.png")
    
    perf = utils.text_to_image("Perfect","assets/ComfortaaBold.ttf",90,"#93beff",True)
    great = utils.text_to_image("Great","assets/ComfortaaBold.ttf",90,"#5fff5f",True)
    good = utils.text_to_image("Okay","assets/ComfortaaBold.ttf",90,"#5ff4ff",True)
    okay = utils.text_to_image("Bad","assets/ComfortaaBold.ttf",90,"#4335ff",True)
    miss = utils.text_to_image("Miss","assets/ComfortaaBold.ttf",90,"#ff3535",True)
    
    mania_standard(perf,"build/hit300.png")
    mania_standard(perf,"build/hit300k.png")
    mania_standard(perf,"build/hit300g.png")
    
    mania_standard(great,"build/hit200.png")
    
    mania_standard(good,"build/hit100.png")
    mania_standard(good,"build/hit100k.png")
    
    mania_standard(okay,"build/hit50.png")
    
    mania_standard(miss,"build/hit0.png")