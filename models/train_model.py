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

# Function to clean text (Fix NaN values)
def clean_text(text):
    if not isinstance(text, str) or pd.isna(text):  # Handle missing values
        return ""
    
    text = text.lower()
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    text = " ".join(word for word in text.split() if word not in stop_words)  # Remove stopwords
    return text


### **📌 1st Dataset: Single CSV with Labeled News**
df1 = pd.read_csv("datasets/Indian_news.csv")  # Replace with actual filename
df1 = df1[['text', 'label']]  # Ensure only relevant columns are used

# Convert labels to numeric (if not already)
# Convert labels in Indian_news.csv
df1["label"] = df1["label"].apply(lambda x: 1 if str(x).lower() in ["real", "1", "true"] else 0)


### **📌 2nd & 3rd Datasets: True.csv & Fake.csv**
true_df = pd.read_csv("datasets/True.csv")
fake_df = pd.read_csv("datasets/Fake.csv")

# Assign labels (1 = Real, 0 = Fake)
true_df["label"] = 1
fake_df["label"] = 0

# Combine into a single DataFrame
df2 = pd.concat([true_df, fake_df])

### **📌 Merge All Datasets Together**
df = pd.concat([df1, df2])

# Shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Remove rows where "text" is NaN
df = df.dropna(subset=["text"])

# Apply text cleaning
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
            "C": [0.01, 0.1, 1, 10],  
            "max_iter": [100, 200, 300]
        }
    },
    "Random Forest": {
        "model": RandomForestClassifier(),
        "params": {
            "n_estimators": [50, 100, 200],  
            "max_depth": [10, 20, None]      
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

# Train the best model
best_model.fit(X_train, y_train)

# Train & Test Accuracy
train_acc = best_model.score(X_train, y_train)
test_acc = best_model.score(X_test, y_test)

print(f"\n🏆 Training Accuracy: {train_acc:.2f}")
print(f"📊 Test Accuracy: {test_acc:.2f}")

if train_acc - test_acc > 0.15:  # If difference is more than 15%, model is overfitting
    print("⚠️ WARNING: Model is overfitting. Try reducing max_depth in Random Forest or n_estimators in Gradient Boosting.")