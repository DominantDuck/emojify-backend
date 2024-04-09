import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

def create_summary(image_path, text, output_dir = "saved_entries", text_font=None, text_color=(0, 0, 0)):
    img = Image.open(image_path)

    
    text_font = text_font or ImageFont.load_default()
    text_width, text_height = ImageDraw.Draw(Image.new('RGB', (1, 1))).textsize(text, font=text_font)
    new_width = img.width + text_width + 20  
    new_height = max(img.height, text_height) + 20  
    new_img = Image.new('RGB', (new_width, new_height), color='white')

    new_img.paste(img, (0, (new_height - img.height) // 2))

    draw = ImageDraw.Draw(new_img)
    draw.text((img.width + 20, (new_height - text_height) // 2), text, font=text_font, fill=text_color)

    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, f'{current_time}.jpg')
    new_img.save(output_path)
    return output_path

