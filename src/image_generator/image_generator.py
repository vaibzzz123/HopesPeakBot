from PIL import Image, ImageDraw, ImageFont
import os

def create_character_list():
    generator = os.walk("./assets/characters/formatted sprites")
    unformatted = [x[0] for x in generator]
    unformatted.pop(0) # this is the directory itself, not the subdirectories
    formatted = [path.replace("\\", "/") for path in unformatted]
    return formatted

def paste_portrait(bg, im, coords):
    bg.paste(im, coords, mask=im)

def paste_arrow(bg, coords):
    im = Image.open("./assets/red arrow flipped.png")
    bg.paste(im, coords, mask=im)

def paste_portraits(bg):
    character_list = create_character_list()
    initial_coords = (30, 413)
    coords = initial_coords

    characters_length = len(character_list)
    i = 0

    while i < characters_length:
        im = Image.open(character_list[i]+'/alive.png')
        paste_portrait(bg, im, coords)
        if(i == 7):
            coords = (initial_coords[0], initial_coords[1]+326)
        else:
            coords = (coords[0]+238, coords[1])
        i += 1

def create_title(bg):
    draw = ImageDraw.Draw(bg)
    fancy_font = ImageFont.truetype("./assets/fonts/MrGrieves-Regular.otf", size=120)
    bg_width = 1920
    msg = "Killing Game Simulator"
    pink_color = (255, 0, 240, 0)
    text_width = draw.textsize(msg, font=fancy_font)[0]
    coords = ((bg_width - text_width)/2, 28)
    draw.text(coords, msg, fill=pink_color, font=fancy_font, align="center")

def create_chapter_number(bg):
    draw = ImageDraw.Draw(bg)
    fancy_font = ImageFont.truetype("./assets/fonts/MrGrieves-Regular.otf", size=60)
    msg = "Prologue"
    pink_color = (255, 0, 240, 0)
    coords = (27, 200)   
    draw.text(coords, msg, fill=pink_color, font=fancy_font, align="left")

def generate_image():
    im = Image.open("./assets/background.png").convert("RGBA")
    create_title(im)
    create_chapter_number(im)
    paste_portraits(im)
    im.show()

generate_image()