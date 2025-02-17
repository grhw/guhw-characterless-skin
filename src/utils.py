from PIL import Image, ImageDraw, ImageFont

def resize_by_multiplier(image, multiplier):
    new_width = int(image.width * multiplier)
    new_height = int(image.height * multiplier)
    return image.resize((new_width, new_height), Image.Resampling.BILINEAR)

def resize_to_resolution(image, width, height):
    copy = image.copy()
    copy.thumbnail((width, height), Image.Resampling.BILINEAR)
    return copy

def tint_image(image, tint_color):
    pixels = image.load()
    r_,g_,b_ = tint_color
    r,g,b = int(r_*255),int(g_*255),int(b_*255)
    
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            _,_,_,a = pixels[x, y]
            pixels[x, y] = (r,g,b,a)

def multiply_alpha(image, factor):
    r, g, b, a = image.split()
    a = a.point(lambda p: min(int(p * factor), 255))
    return Image.merge("RGBA", (r, g, b, a))

def text_to_image(text, font_path, font_size, color, shadow):
    font = ImageFont.truetype(font_path, font_size)

    image = Image.new("RGBA", (1, 1))
    draw = ImageDraw.Draw(image)
    text_bbox = draw.textbbox((0, 0), text, font=font)

    x,y = 0,0#text_bbox[0]/2,text_bbox[1]/2
    sx,sy = x+int(text_bbox[2]*0.05),y+int(text_bbox[3]*0.05)
    so = min(sx,sy)
    
    image = image.resize((text_bbox[2]+(text_bbox[0]*2)+so,text_bbox[3]+(text_bbox[1]*2)+so))
    draw = ImageDraw.Draw(image)
    
    
    
    if shadow:
        draw.text((so, so), text, fill="#000000", font=font)
    draw.text((x, y), text, fill=color, font=font)

    return image

def add_before(path,suffix):
    s = path.split(".")
    return f"{'.'.join(s[:-1])}{suffix}.{s[-1]}"

def save_hd_sd(image,path):
    print(path)
    image.save(add_before(path,"@2x"))
    resize_by_multiplier(image,0.5).save(path)

def remove(path):
    Image.open("assets/gameplay/standard/invisible.png").save(path)