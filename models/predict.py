import joblib
import pandas as pd
import re 
import string
import nltk
from nltk.corpus import stopwords

# Load trained model & vectorizer
model = joblib.load("models/best_fake_news_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Download stopwords (only needed once)
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Function to clean text (same as `train_model.py`)
def clean_text(text):
    if not isinstance(text, str) or pd.isna(text):  # Handle missing values
        return ""
    
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    text = " ".join(word for word in text.split() if word not in stop_words)  # Remove stopwords
    return text

def predict_news(news_text):
    text = clean_text(news_text)  # Apply same preprocessing
    text_vector = vectorizer.transform([text])  # Transform with correct vectorizer
    prediction = model.predict(text_vector)[0]
    return "Real News" if prediction == 1 else "Fake News"

# Test with a sample news article
sample_text = "In Texas, buses reserved a front seat in honor of Rosa Parks, celebrating her legacyMonsanto announced the closure of three facilities, marking a step towards environmental change"
print("Prediction:", predict_news(sample_text))
