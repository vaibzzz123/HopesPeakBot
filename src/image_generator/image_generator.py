import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from character import Character

root_path_raw = Path(__file__).parent.parent.parent
root_path = str(root_path_raw)

def paste_portrait(bg, im, coords):
    bg.paste(im, coords, mask=im)

def paste_arrow(bg, coords):
    path = str(os.path.join(root_path, 'assets', 'red arrow flipped.png'))
    im = Image.open(path)
    new_size = (64, 64)
    im.thumbnail(new_size)
    bg.paste(im, coords, mask=im)

def paste_portraits(bg, characters):
    initial_coords = (30, 413)
    coords = initial_coords

    characters_length = len(characters)
    i = 0
    portrait_number = 0

    while i < characters_length:

        j = 0
        list_length = len(characters[i])
        while j < list_length:

            character = characters[i][j]
            path = os.path.join(root_path, 'assets', 'characters', 'formatted sprites', character.get_first_name(), character.get_status() + ".png")
            im = Image.open(path)
            paste_portrait(bg, im, coords)

            if character.get_character_type() == "killer":
                arrow_coords = (coords[0]+186, coords[1]+52)
                paste_arrow(bg, arrow_coords)
                
            if(portrait_number == 7):
                coords = (initial_coords[0], initial_coords[1]+326) 
            else:
                coords = (coords[0]+238, coords[1])
            j += 1
            portrait_number += 1
        
        i += 1

def create_title(bg):
    draw = ImageDraw.Draw(bg)
    path = str(os.path.join(root_path, 'assets', 'fonts', 'MrGrieves-Regular.otf'))
    fancy_font = ImageFont.truetype(path, size=120)
    bg_width = 1920
    msg = "Killing Game Simulator"
    pink_color = (255, 0, 240, 255)
    text_width = draw.textsize(msg, font=fancy_font)[0]
    coords = ((bg_width - text_width)/2, 28)
    draw.text(coords, msg, fill=pink_color, font=fancy_font, align="center")

def create_chapter_number(bg, msg):
    draw = ImageDraw.Draw(bg)
    path = str(os.path.join(root_path, 'assets', 'fonts', 'MrGrieves-Regular.otf'))
    fancy_font = ImageFont.truetype(path, size=60)
    pink_color = (255, 0, 240, 255)
    coords = (27, 200)
    draw.text(coords, msg, fill=pink_color, font=fancy_font, align="left")

def create_temporary_image(im):
    path = os.path.join(root_path, 'current_round.png')
    im.save(path)

def remove_temporary_image():
    path = os.path.join(root_path, 'current_round.png')
    if os.path.exists(path):
        os.remove(path)

def generate_image(character_data, chapter):
    path = str(os.path.join(root_path, 'assets', 'background.png'))
    im = Image.open(path).convert("RGBA")
    create_title(im)
    create_chapter_number(im, chapter)
    paste_portraits(im, character_data)
    create_temporary_image(im)
    im.show()