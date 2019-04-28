from PIL import Image, ImageDraw, ImageFont
from character import Character, dr1_test

def paste_portrait(bg, im, coords):
    bg.paste(im, coords, mask=im)

def paste_arrow(bg, coords):
    im = Image.open("./assets/red arrow flipped.png")
    width, height = im.size
    im.thumbnail((64, 64))
    bg.paste(im, coords, mask=im)

def paste_portraits(bg):
    characters = dr1_test
    initial_coords = (30, 413)
    coords = initial_coords

    characters_length = len(characters)
    i = 0
    portrait_number = 0

    while i < characters_length:

        j = 0
        tuple_length = len(characters[i])
        while j < tuple_length:

            character = characters[i][j]
            im = Image.open(character.get_character_path())
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
    fancy_font = ImageFont.truetype("./assets/fonts/MrGrieves-Regular.otf", size=120)
    bg_width = 1920
    msg = "Killing Game Simulator"
    pink_color = (255, 0, 240, 255)
    text_width = draw.textsize(msg, font=fancy_font)[0]
    coords = ((bg_width - text_width)/2, 28)
    draw.text(coords, msg, fill=pink_color, font=fancy_font, align="center")

def create_chapter_number(bg):
    draw = ImageDraw.Draw(bg)
    fancy_font = ImageFont.truetype("./assets/fonts/MrGrieves-Regular.otf", size=60)
    msg = "Prologue"
    pink_color = (255, 0, 240, 255)
    coords = (27, 200)   
    draw.text(coords, msg, fill=pink_color, font=fancy_font, align="left")

def generate_image():
    im = Image.open("./assets/background.png").convert("RGBA")
    create_title(im)
    create_chapter_number(im)
    paste_portraits(im)
    im.show()

generate_image()