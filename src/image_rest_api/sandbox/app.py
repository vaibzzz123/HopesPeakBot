from flask import Flask, request
from pathlib import Path
import sys, os

src_path = Path(__file__).parent.parent.parent
image_generator_folder = os.path.join(src_path, 'image_generator')
sys.path.append(image_generator_folder)
from image_generator import generate_image, remove_temporary_image

app = Flask(__name__)

@app.route('/generate_image', methods=['POST'])
def index():
    if request.is_json:
        data = request.get_json()
        print(data)
        generate_image()
        return 'cool json!'
    else:
        return 'error, not json'
  
@app.route('/remove_image', methods=['DELETE'])
def remove_message():
    remove_temporary_image()
    return 'removed image'