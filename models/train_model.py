import pandas as pd
import re
import string
import nltk
import joblib
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score

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

# Define models with hyperparameter tuning
models = {
    "Logistic Regression": {
        "model": LogisticRegression(),
        "params": {
            "C": [0.01, 0.1, 1, 10],  # Regularization strength
            "max_iter": [100, 200, 300]
        }
    },
    "Random Forest": {
        "model": RandomForestClassifier(),
        "params": {
            "n_estimators": [50, 100, 200],  # Number of trees
            "max_depth": [10, 20, None]      # Max depth
        } 
    },
    "Gradient Boosting": {
        "model": GradientBoostingClassifier(),
        "params": {
            "n_estimators": [50, 100, 200],
            "learning_rate": [0.01, 0.1, 0.2]
        }
    }
}

# Perform hyperparameter tuning and find the best model
best_model = None
best_accuracy = 0

for name, config in models.items():
    print(f"🔍 Tuning hyperparameters for {name}...")
    
    # Perform Grid Search
    grid_search = GridSearchCV(config["model"], config["params"], cv=3, scoring="accuracy", n_jobs=-1)
    grid_search.fit(X_train, y_train)
    
    # Get best model
    best_model_instance = grid_search.best_estimator_
    y_pred = best_model_instance.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    
    print(f"✅ Best {name} Accuracy: {acc:.2f}")
    print(f"🔹 Best Parameters: {grid_search.best_params_}\n")

    # Save the best-performing model
    if acc > best_accuracy:
        best_accuracy = acc
        best_model = best_model_instance

# Save the best model
joblib.dump(best_model, "models/best_fake_news_model.pkl")
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

print(f"🏆 Best model saved: {best_model}")
