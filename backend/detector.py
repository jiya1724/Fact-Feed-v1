import os
import re
import string
import joblib
import logging

# Get the absolute path to the models directory
base_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(base_dir)
model_path = os.path.join(parent_dir, "models", "trained", "nb_news_classifier.pkl")
vectorizer_path = os.path.join(parent_dir, "models", "trained", "nb_tfidf_vectorizer.pkl")

try:
    # Load trained model & vectorizer
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    print(f"Successfully loaded model from {model_path}")
except Exception as e:
    print(f"Error loading model: {str(e)}")
    # Fallback to relative path as last resort
    try:
        model = joblib.load("./models/trained/nb_news_classifier.pkl")
        vectorizer = joblib.load("./models/trained/nb_tfidf_vectorizer.pkl")
    except Exception as e2:
        print(f"Critical error loading model: {str(e2)}")
        # Define dummy model/vectorizer for non-critical operation
        model = None
        vectorizer = None

# Function to clean text (same as in train_model.py)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = " ".join(text.split())  # Remove extra spaces
    return text

def predict_news(news_text):
    if model is None or vectorizer is None:
        return "Model not loaded - Unable to predict"
    
    text = clean_text(news_text)  # Preprocess text
    text_vector = vectorizer.transform([text])  # Convert to numerical form
    prediction = model.predict(text_vector)[0]  # Get prediction
    return "Real News" if prediction == 1 else "Fake News"
