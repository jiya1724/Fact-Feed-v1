import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import torch
from torch.utils.data import DataLoader
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset

# Load and combine datasets
true_df = pd.read_csv('datasets/True.csv')
fake_df = pd.read_csv('datasets/Fake.csv')
indian_df = pd.read_csv('datasets/Indian_news.csv')

# Ensure column names match (e.g., "text" and "label")
true_df['label'] = 'REAL'
fake_df['label'] = 'FAKE'

# If Indian dataset already has labels "REAL"/"FAKE", no changes needed
# Combine all datasets
combined_df = pd.concat([true_df, fake_df, indian_df], ignore_index=True)

# Shuffle and reset index
combined_df = combined_df.sample(frac=1).reset_index(drop=True)

# Drop any rows with missing text or label
combined_df.dropna(subset=['text', 'label'], inplace=True)

# Convert text column to string, in case any are float (e.g., nan)
combined_df['text'] = combined_df['text'].astype(str)

# Encode labels to 0 (FAKE) and 1 (REAL)
label_encoder = LabelEncoder()
combined_df['label'] = label_encoder.fit_transform(combined_df['label'])  # FAKE=0, REAL=1

# Rename the text column to "text" if needed
if 'text' not in combined_df.columns:
    # Adjust based on actual column name in Indian_news.csv
    text_column = 'title' if 'title' in combined_df.columns else combined_df.columns[0]
    combined_df.rename(columns={text_column: 'text'}, inplace=True)

# Split data
train_texts, val_texts, train_labels, val_labels = train_test_split(
    combined_df['text'], combined_df['label'], test_size=0.2, random_state=42
)

# Tokenization
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

def tokenize_function(examples):
    return tokenizer(examples['text'], padding='max_length', truncation=True)

# Convert to HuggingFace dataset format
train_dataset = Dataset.from_dict({'text': train_texts.tolist(), 'label': train_labels.tolist()})
val_dataset = Dataset.from_dict({'text': val_texts.tolist(), 'label': val_labels.tolist()})

# Tokenize datasets
train_dataset = train_dataset.map(tokenize_function, batched=True)
val_dataset = val_dataset.map(tokenize_function, batched=True)

# Set format for PyTorch
train_dataset.set_format(type='torch', columns=['input_ids', 'attention_mask', 'label'])
val_dataset.set_format(type='torch', columns=['input_ids', 'attention_mask', 'label'])

# Load BERT model
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# Define training args
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy='epoch',
    save_strategy='epoch',
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=4,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
    load_best_model_at_end=True,
    metric_for_best_model="accuracy"
)

# Define accuracy metric
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = torch.argmax(torch.tensor(logits), dim=1)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, predictions, average='binary')
    acc = accuracy_score(labels, predictions)
    return {'accuracy': acc, 'f1': f1, 'precision': precision, 'recall': recall}

# Train the model
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    compute_metrics=compute_metrics
)

trainer.train()
