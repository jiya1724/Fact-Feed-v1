import pandas as pd

# Load datasets
true_df = pd.read_csv("datasets/True.csv")
fake_df = pd.read_csv("datasets/Fake.csv")
indian_df = pd.read_csv("datasets/Indian_news.csv")

# Check label distribution
print("True.csv Real News Count:", len(true_df))
print("Fake.csv Fake News Count:", len(fake_df))
print("Indian_news.csv Label Counts:\n", indian_df["label"].value_counts())
