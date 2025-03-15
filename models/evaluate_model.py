import joblib
from sklearn.metrics import accuracy_score, classification_report

# Load model & vectorizer
model = joblib.load("../models/fake_news_model.pkl")
X_test = joblib.load("../models/X_test.pkl")
y_test = joblib.load("../models/y_test.pkl")

# Predict on test data
y_pred = model.predict(X_test)

# Evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print(classification_report(y_test, y_pred))
