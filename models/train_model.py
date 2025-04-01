import pandas as pd
import re
import string
import nltk
import joblib
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score

nltk.download("stopwords")
nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def clean_text(text):
    if not isinstance(text, str) or pd.isna(text):
        return ""
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    text = " ".join([lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words])  # Lemmatization
    return text


true_df = pd.read_csv("datasets/True.csv")
fake_df = pd.read_csv("datasets/Fake.csv")
indian_news_df = pd.read_csv("datasets/Indian_news.csv")


true_df["label"] = 1  
fake_df["label"] = 0  
indian_news_df["label"] = indian_news_df["label"].apply(lambda x: 1 if str(x).lower() == 'real' else 0)


df = pd.concat([true_df, fake_df, indian_news_df])


df = df.sample(frac=1, random_state=42).reset_index(drop=True)


df["text"] = df["text"].apply(clean_text)


vectorizer = TfidfVectorizer(ngram_range=(1, 3), max_features=10000)
X = vectorizer.fit_transform(df["text"])
y = df["label"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Logistic Regression": {
        "model": LogisticRegression(max_iter=300),
        "params": {"C": [0.01, 0.1, 1, 10]}
    },
    "Random Forest": {
        "model": RandomForestClassifier(),
        "params": {"n_estimators": [100, 200], "max_depth": [10, 20, None]}
    },
    "Gradient Boosting": {
        "model": GradientBoostingClassifier(),
        "params": {"n_estimators": [100, 200], "learning_rate": [0.01, 0.1]}
    }
}

best_model = None
best_accuracy = 0

for name, config in models.items():
    print(f"Tuning hyperparameters for {name}...")
    grid_search = GridSearchCV(config["model"], config["params"], cv=3, scoring="accuracy", n_jobs=-1)
    grid_search.fit(X_train, y_train)
    
    best_model_instance = grid_search.best_estimator_
    y_pred = best_model_instance.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    
    print(f"{name} Accuracy: {acc:.2f}")
    print(f"Best Parameters: {grid_search.best_params_}\n")

    if acc > best_accuracy:
        best_accuracy = acc
        best_model = best_model_instance


joblib.dump(best_model, "models/best_fake_news_model.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

print(f"Best model saved: {best_model}")
