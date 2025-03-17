import joblib

# Load trained model & vectorizer
model = joblib.load("models/fake_news_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

def predict_news(news_text):
    text_vector = vectorizer.transform([news_text])
    prediction = model.predict(text_vector)[0]
    return "Real News" if prediction == 1 else "Fake News"

# Test with a sample news article
sample_text = "An unidentified source has reported that an alien spacecraft secretly landed in California last night. Authorities have allegedly covered up the incident to prevent public panic."
print("Prediction:", predict_news(sample_text))
