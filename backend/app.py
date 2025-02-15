from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # Import CORS
from PIL import Image, ImageDraw, ImageFont
import os
import random
import nltk
from textblob import TextBlob

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Ensure nltk resources are available
nltk.download('punkt')

# Meme template folder
TEMPLATES_DIR = "templates"
GENERATED_DIR = "generated_memes"

# Ensure directories exist
os.makedirs(TEMPLATES_DIR, exist_ok=True)
os.makedirs(GENERATED_DIR, exist_ok=True)

def generate_caption(text):
    blob = TextBlob(text)
    return blob.correct().string

def create_meme(image_path, text):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    
    width, height = img.size
    text_x = width // 4
    text_y = height - 50
    
    draw.text((text_x, text_y), text, font=font, fill="white")

    meme_filename = f"meme_{random.randint(1000,9999)}.jpg"
    meme_path = os.path.join(GENERATED_DIR, meme_filename)
    img.save(meme_path)
    return meme_filename

@app.route('/generate_meme', methods=['POST'])
def generate_meme():
    data = request.json
    text = generate_caption(data.get("text", "Default Meme"))
    
    # Select a random template
    templates = [os.path.join(TEMPLATES_DIR, f) for f in os.listdir(TEMPLATES_DIR) if f.endswith(".jpg")]
    if not templates:
        return jsonify({"error": "No meme templates found!"}), 500

    template = random.choice(templates)
    
    meme_filename = create_meme(template, text)
    return jsonify({"meme": f"/memes/{meme_filename}"})

@app.route('/memes/<filename>')
def serve_meme(filename):
    return send_from_directory(GENERATED_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
