#naiveBayes=>handles sparse matrix data like TF-IDF.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib
import re
from sklearn.model_selection import GridSearchCV      #for hyperparameter tuning

# Load datasets
true_df = pd.read_csv('True.csv',dtype=str,low_memory=False)
fake_df = pd.read_csv('Fake.csv',dtype=str,low_memory=False)

# Add label column
true_df['label'] = 1  # Reliable news
fake_df['label'] = 0  # Unreliable news

# Merge datasets
merged_df = pd.concat([true_df, fake_df], ignore_index=True)

# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

merged_df['text'] = merged_df['text'].apply(clean_text)

# Feature Extraction
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
X = tfidf.fit_transform(merged_df['text']).toarray()
y = merged_df['label']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Naive Bayes Model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("Naive Bayes Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save model & vectorizer
joblib.dump(model, 'nb_news_classifier.pkl')
joblib.dump(tfidf, 'nb_tfidf_vectorizer.pkl')




# Hyperparameter tuning for Naive Bayes=>e.g., tweaking the alpha (smoothing) parameter.


param_grid = {
    'alpha': [0.01, 0.1, 0.5, 1.0]  # Smoothing parameter
}

grid_search = GridSearchCV(MultinomialNB(), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

print("Best Parameters:", grid_search.best_params_)

best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
print("Tuned Naive Bayes Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))