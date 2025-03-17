import re
import string
from flask import Flask, request, jsonify
import joblib

# Load the correct trained model & vectorizer
model = joblib.load("models/fake_news_model.pkl")  # Ensure correct model is used
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

app = Flask(__name__)

# Function to clean text (SAME as in train_model.py & predict.py)
def clean_text(text):
    text = text.lower()  
    text = re.sub(r'\d+', '', text)  
    text = text.translate(str.maketrans('', '', string.punctuation))  
    text = " ".join(text.split())  # Remove extra spaces
    return text

@app.route('/')
def home():
    return "Fake News Detection API is Running! Use POST /predict to check news."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        text = clean_text(data['text'])  # Apply proper text preprocessing

        # Ensure input is in list format for vectorizer
        text_vector = vectorizer.transform([text])  

        # Predict using trained model
        prediction = model.predict(text_vector)[0]
        result = "Real News" if prediction == 1 else "Fake News"

        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
