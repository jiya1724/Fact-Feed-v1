import pandas as pd
import re
import string
import nltk
import joblib
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Download stopwords
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Function to clean text
def clean_text(text):
    text = text.lower()  
    text = re.sub(r'\d+', '', text)  
    text = text.translate(str.maketrans('', '', string.punctuation))  
    text = " ".join(word for word in text.split() if word not in stop_words)
    return text

# Load datasets
true_df = pd.read_csv("datasets/True.csv")
fake_df = pd.read_csv("datasets/Fake.csv")

# Assign labels
true_df["label"] = 1  
fake_df["label"] = 0  

# Merge and shuffle
df = pd.concat([true_df, fake_df]).sample(frac=1, random_state=42).reset_index(drop=True)

# Preprocess text
df["text"] = df["title"] + " " + df["text"]
df["text"] = df["text"].apply(clean_text)

# Convert text to numerical format
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model and vectorizer
joblib.dump(model, "fake_news_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

# Save test data for evaluation
joblib.dump(X_test, "X_test.pkl")
joblib.dump(y_test, "y_test.pkl")

print("Model training complete. Model saved in 'models' folder.")
