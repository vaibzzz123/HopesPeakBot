from PIL import Image
import os

def create_character_list():
    generator = os.walk("./assets/characters/formatted sprites")
    unformatted = [x[0] for x in generator]
    unformatted.pop(0)
    formatted = [path.replace("\\", "/") for path in unformatted]
    return formatted

def paste_onto(bg):
    character_list = create_character_list()
    im = Image.open(character_list[0]+'/alive.png')
    bg.paste(im, (900, 100), mask=im)

def generate_image():
    im = Image.open("./assets/background.png")
    paste_onto(im)
    im.show()

generate_image()