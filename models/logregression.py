import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV
import joblib
import re

# Load datasets (set dtype to prevent mixed types warning)
true_df = pd.read_csv('True.csv', dtype=str, low_memory=False)
fake_df = pd.read_csv('Fake.csv', dtype=str, low_memory=False)

# Add labels
true_df['label'] = 1  # Reliable news
fake_df['label'] = 0  # Unreliable news

# Merge datasets
merged_df = pd.concat([true_df, fake_df], ignore_index=True)

# Text Cleaning Function
def clean_text(text):
    if isinstance(text, str):
        text = text.lower()
        text = re.sub(r'\d+', '', text)  # Remove numbers
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    return text

# Apply cleaning
merged_df['text'] = merged_df['text'].apply(clean_text)

# Feature Extraction (TF-IDF)
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
X = tfidf.fit_transform(merged_df['text']).toarray()
y = merged_df['label'].astype(int)  # Ensure labels are integers

# Ensure X and y have the same length
assert len(X) == len(y), f"Inconsistent data: X has {len(X)} rows, y has {len(y)} labels"

# Split Data (use merged_df, not df)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save Model
joblib.dump(model, 'news_classifier.pkl')
joblib.dump(tfidf, 'tfidf_vectorizer.pkl')



# Hyperparameter Tuning
param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],  # Regularization strength
    'penalty': ['l1', 'l2'],        # Regularization type
    'solver': ['liblinear']         # Solver for optimization
}

grid_search = GridSearchCV(LogisticRegression(), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Best Parameters
print("Best Parameters:", grid_search.best_params_)

# Evaluate Best Model
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
