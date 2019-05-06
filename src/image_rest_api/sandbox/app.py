from flask import Flask, request, jsonify
from pathlib import Path
import sys, os

root_path = Path(__file__).parent.parent.parent.parent
image_generator_folder = os.path.join(root_path, 'src', 'image_generator')
sys.path.append(image_generator_folder)
from image_generator import generate_image, remove_temporary_image
from character import Character

app = Flask(__name__)

def process_json(data):
    parsed_rounds = []
    round_name = ''
    rounds = data["all_rounds"]
    players_remaining = data["players_remaining"]
    if rounds is not None:
        length = len(rounds)
        for i in range(length):
            round = rounds[i]
            parsed_round = []
        
            character = round["murderer"]
            if character["name"] != '':
                parsed_character = Character(character["name"], character["status"], character["character_type"])
                parsed_round.append(parsed_character)

            character = round["victim_one"]
            if character["name"] != '':
                parsed_character = Character(character["name"], character["status"], character["character_type"])
                parsed_round.append(parsed_character)

            character = round["victim_two"]
            if character["name"] != '':
                parsed_character = Character(character["name"], character["status"], character["character_type"])
                parsed_round.append(parsed_character)

            parsed_rounds.append(parsed_round)

            if i == length - 1:
                round_name == round["round_name"]
    
    parsed_player_array = []
    for player in players_remaining:
        parsed_player = Character(player["name"], player["status"], player["character_type"])
        parsed_player_array.append(parsed_player)
    
    parsed_rounds.append(parsed_player_array)

    return parsed_rounds, round_name

@app.route('/', methods=['GET', 'POST'])
def basic_response():
    if request.method == 'POST':
        return jsonify(request.get_json())
    return 'hooray!'

@app.route('/generate_image', methods=['POST'])
def index():
    if request.is_json:
        data = request.get_json()
        characters, round_name = process_json(data)
        generate_image(characters, round_name)
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