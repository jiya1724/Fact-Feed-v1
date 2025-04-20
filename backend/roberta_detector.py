from transformers import RobertaTokenizer, RobertaForSequenceClassification
import torch

# Load model and tokenizer once at the start
model_path = "models/trained/roberta_model"  # adjust if needed
tokenizer = RobertaTokenizer.from_pretrained(model_path)
model = RobertaForSequenceClassification.from_pretrained(model_path)

label_map = {0: "Fake News", 1: "Real News"}

def predict_news(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        predicted_class = torch.argmax(outputs.logits, dim=1).item()
        return label_map[predicted_class]
