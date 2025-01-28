import utils
from PIL import Image

def animate_for(frames, path, new):
    image = Image.open(path)
    utils.remove(utils.add_before(new,f"-{frames}"))
    for i in range(frames):
        utils.save_hd_sd(image,utils.add_before(new,f"-{i}"))

def create_feedback():
    animate_for(15,"assets/gameplay/standard/feedback-miss.png","build/hit0.png")

    animate_for(10,"assets/gameplay/standard/feedback-50.png","build/hit50.png")
    
    animate_for(10,"assets/gameplay/standard/feedback-100.png","build/hit100.png")
    animate_for(10,"assets/gameplay/standard/feedback-100.png","build/hit100k.png")
    
    utils.remove("build/hit300.png")
    utils.remove("build/hit300k.png")
    utils.remove("build/hit300g.png")