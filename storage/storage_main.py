import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

def create_summary(image_path, text, output_dir="saved_entries", font_path="helvetica-light.ttf", text_color=(0, 0, 0), img_fraction=0.50):
    img = Image.open(image_path)

    fontsize = 40

    canvas_width = img.width + 300 + 400 
    canvas_height = max(img.height + 20, 100)

    new_img = Image.new('RGB', (canvas_width, canvas_height), color='white')

    new_img.paste(img, (100, (canvas_height - img.height) // 2))

    draw = ImageDraw.Draw(new_img)
    
    font = ImageFont.truetype(font_path, fontsize, encoding="unic")

    text_x = img.width + 200 
    text_y = 50


    lines = []
    line = ""
    max_text_width = canvas_width - text_x - 5 
    for word in text.split():
        if len(line) + len(word) < max_text_width // (fontsize // 2):
            line += word + " "
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)

    current_y = text_y
    for line in lines:
        draw.text((text_x, current_y), line, font=font, fill=text_color)
        current_y += fontsize 

    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, f'{current_time}.jpg')
    new_img.save(output_path)

    return output_path

