import re
import string
import joblib

# Load trained model & vectorizer
model = joblib.load("models/best_fake_news_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Function to clean text (same as in train_model.py)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = " ".join(text.split())  # Remove extra spaces
    return text

def predict_news(news_text):
    text = clean_text(news_text)  # Preprocess text
    text_vector = vectorizer.transform([text])  # Convert to numerical form
    prediction = model.predict(text_vector)[0]  # Get prediction
    return "Real News" if prediction == 1 else "Fake News"
