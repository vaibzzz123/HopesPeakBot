from flask import Flask, request
from pathlib import Path
import sys, os

root_path = Path(__file__).parent.parent.parent.parent
image_generator_folder = os.path.join(root_path, 'src', 'image_generator')
sys.path.append(image_generator_folder)
from image_generator import generate_image, remove_temporary_image
from character import Character

app = Flask(__name__)

def process_character_json(character_data):
    parsed_data = []
    for array in character_data:
        parsed_array = []
        for character in array:
            parsed_character = Character(character["name"], character["status"], character["character_type"])
            parsed_array.append(parsed_character)
        parsed_data.append(parsed_array)
    return parsed_data

@app.route('/generate_image', methods=['POST'])
def index():
    if request.is_json:
        data = request.get_json()
        character_data = process_character_json(data["characters"])
        generate_image(character_data, data["round"])
        return 'image for current round created at ./current_round.png'
    else:
        return 'error, not json'
  
@app.route('/remove_image', methods=['DELETE'])
def remove_message():
    path = os.path.join(root_path, 'current_round.png')
    if os.path.exists(path):
        remove_temporary_image()
        return 'removed image for current round at ./current_round.png'
    else:
        return 'image not found'