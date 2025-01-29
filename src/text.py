import utils

text_list = {
    "ranking-accuracy.png": ["Accuracy",90],
    "ranking-maxcombo.png": ["Combo",90],
    "ranking-perfect.png": ["FC",90],
    "spinner-clear.png": ["Clear!",90],
    "spinner-spin.png": ["Spin! Spin! Spin!",90],
    "spinner-rpm.png": ["RPM:",90],
    "play-unranked.png": ["Unranked",90],
    
    "play-warningarrow.png": ["!",90],
    "arrow-pause.png": [">",90],
    "multi-skipped.png": ["Skipped",50],
    
    "section-fail.png": ["Fail..",90],
    "section-pass.png": ["Good job!!",90],
    
    "count3.png": ["3...",90],
    "count2.png": ["2...",90],
    "count1.png": ["1...",90],
    "go.png": ["GO!!!",60],
    "ready.png": ["Ready...",90],
    
    
    "pause-back.png": ["Back       ",90],
    "pause-continue.png": ["Continue",90],
    "pause-replay.png": ["Replay       ",90],
    "pause-retry.png": ["Retry       ",90],
}

def create_texts():
    for fn in text_list.keys():
        text,size = text_list[fn]
        
        utils.save_hd_sd(utils.text_to_image(text,"assets/ComfortaaBold.ttf",size,"#FFFFFF",True),f"build/{fn}")