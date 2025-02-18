# 🤖 AI-Powered Meme Generator

## 📌 Overview
An AI-powered meme generator that takes text prompts and creates memes using deep learning and natural language processing.

## 🎯 Features
- **Text-to-Meme Generation** – AI generates a meme from text prompts.
- **Predefined Meme Templates** – Choose from classic meme formats.
- **AI-Generated Captions** – NLP-based meme caption generation using NLTK/TextBlob.
- **Custom Image Uploads** – Users can upload their own image.
- **Download & Share Option** – Download or share memes.

## 🏗️ Tech Stack
### Backend:
- Python (Flask)
- NLTK/TextBlob (for meme text generation without API keys)
- PIL/OpenCV (for image processing)

### Frontend:
- React.js (for web app)
- Tailwind CSS (for styling)
- HTML Canvas or Fabric.js (for image manipulation)

### Deployment:
- **Backend**: Local execution / Docker
- **Frontend**: Local execution

## 🚀 Getting Started
### Prerequisites
- Python 3.8+
- Node.js & npm

### Installation
#### Backend:
```bash
# Clone the repository
git clone https://github.com/Swyampatel/ai-meme-generator.git
cd ai-meme-generator/backend

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the API
python app.py
```

#### Frontend:
```bash
cd ../frontend
npm install
npm start
```

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## 🏆 License
MIT License
