import joblib
import pandas as pd
import re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Load trained model & vectorizer
model = joblib.load("models/trained/nb_news_classifier.pkl")
vectorizer = joblib.load("models/trained/nb_tfidf_vectorizer.pkl")

# Preprocessing function
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def clean_text(text):
    if not isinstance(text, str) or pd.isna(text):
        return ""
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = " ".join([lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words])
    return text

def predict_news(news_text):
    text = clean_text(news_text)
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]
    return "Real News" if prediction == 1 else "Fake News"

# Test
sample_text = """
The government has introduced a new healthcare policy aimed at providing affordable medical services to all citizens. The policy includes subsidized health insurance and expanded access to rural areas
"""

"""Real
Israel launched a series of airstrikes across the Gaza Strip, targeting Hamas in what is described as the heaviest assault since a ceasefire was established in January. Gaza's Ministry of Health reported at least 44 fatalities from the strikes. The Israeli government stated that the attacks were a response to Hamas's refusal to release hostages and engage in ceasefire negotiations. Prime Minister Benjamin Netanyahu emphasized that Israel would intensify its military actions against Hamas.
The strikes have caused significant destruction in Gaza, with explosions reported in multiple locations. Ambulances were seen rushing to Al Aqsa Hospital in central Gaza. The ceasefire, which had brought temporary relief, is now at risk of collapsing, potentially worsening the humanitarian crisis in the region.

The government has introduced a new healthcare policy aimed at providing affordable medical services to all citizens. The policy includes subsidized health insurance and expanded access to rural areas


"""

"""Fake

A viral article claims that NASA scientists have confirmed that ancient Indian temple structures have direct connections to extraterrestrial civilizations. The article alleges that NASA has conducted extensive research and found mysterious signals originating from Indian temples.

An unidentified source has reported that an alien spacecraft secretly landed in California last night. Authorities have allegedly covered up the incident to prevent public panic.

"""

print("Prediction:", predict_news(sample_text))
