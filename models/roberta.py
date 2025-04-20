import torch
from transformers import RobertaTokenizer, RobertaForSequenceClassification

# Path to the saved RoBERTa model directory
model_path = "models/trained/roberta_model"

# Load tokenizer and model
tokenizer = RobertaTokenizer.from_pretrained(model_path)
model = RobertaForSequenceClassification.from_pretrained(model_path)

# Set to evaluation mode
model.eval()

# Prediction function
def classify_news(news_text):
    inputs = tokenizer(news_text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()

    label = "Real" if predicted_class == 1 else "Fake"
    return label

# 🔍 Example usage
news = """The government has introduced a new healthcare policy aimed at providing affordable medical services to all citizens. The policy includes subsidized health insurance and expanded access to rural areas
"""
result = classify_news(news)
print("Prediction:", result)
