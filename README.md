# 📰 News Summarizer, Aggregator, and Fake News Detection

## 📝 Project Overview

This is a web-based application that allows users to:

- ✂️ Summarize lengthy news articles using advanced Natural Language Processing (NLP) techniques.
- 🌐 Aggregate news from multiple sources for comprehensive coverage.
- 🧪 Detect and flag potentially fake news content to ensure information reliability.

The application uses **Python (Flask)** for backend processing and **TypeScript (React)** for the frontend. It integrates machine learning models to power NLP tasks like summarization and fake news detection.

---

## 🚀 Features

- **Text Summarization**: Condenses articles into their key points.
- **News Aggregation**: Fetches and stores news from diverse APIs/sources.
- **Fake News Detection**: Flags suspicious or misleading content using ML classifiers.

---

## 🛠️ Technologies Used

| Layer     | Technology                                    |
|-----------|-----------------------------------------------|
| Frontend  | TypeScript, React, Tailwind CSS, Mako         |
| Backend   | Python (Flask, Flask-SQLAlchemy, Flask-Migrate) |
| ML/NLP    | Scikit-learn, NLTK, pandas, numpy             |
| Database  | SQLite                                        |
| Other     | dotenv, logging, cron jobs (APScheduler)      |

---

## 📁 Project Structure
. ├── backend/ # Flask backend code ├── frontend/ # React + Tailwind frontend ├── datasets/ # ML training/evaluation datasets ├── models/ # Trained ML models ├── logs/ # Log files ├── migrations/ # DB migrations via Alembic ├── instance/ # Instance configs (e.g., API keys) ├── cosine_summarizer.py # Cosine similarity-based summarizer ├── summarize.py # Main summarizer script ├── requirements.txt # Python dependencies ├── .flaskenv # Flask environment variables └── README.md # Project documentation


---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/KartikAmbupe/Mini-Project-Sem-VI.git
cd Mini-Project-Sem-VI

2. Install dependencies

pip install -r requirements.txt

3. Run database migrations

flask db upgrade

4. Start the application

flask run

🧪 Usage

Open the app in your browser: http://localhost:5000

Navigate through:

Summarizer to condense articles.

Aggregator to browse current news.

Detector to check for fake news.

🤖 Machine Learning Approach
Summarization: Extractive method using cosine similarity and sentence ranking via NLP.

Fake News Detection: Classification using algorithms like Naive Bayes or Logistic Regression on TF-IDF features.

Aggregation: Scheduled background jobs (via APScheduler) pull articles using fetcher.py (e.g., NewsAPI, RSS), stored via SQLAlchemy in SQLite.

🙏 Acknowledgements
Datasets from open-source fake news and summarization projects.

Libraries: Flask, scikit-learn, pandas, NLTK, etc.

Tailwind CSS and open-source UI inspiration.


Happy coding! 🚀




