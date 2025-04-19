📰 News Summarizer, Aggregator & Fake News Detection
A web application to:

✂️ Summarize lengthy news articles using advanced NLP.

🌐 Aggregate news from multiple sources for comprehensive coverage.

🧪 Detect and flag potentially fake news content using machine learning.

Built with a Python (Flask) backend and TypeScript (React) frontend, integrating ML models for summarization and fake news detection.

🚀 Features
Text Summarization: Condense articles into concise summaries.

News Aggregation: Fetch and store news from diverse APIs and RSS sources.

Fake News Detection: Flag suspicious or misleading content using ML classifiers.

Modern UI: Responsive, mobile-friendly interface with Tailwind CSS.

🛠️ Tech Stack
Layer	  Technology
Frontend	 TypeScript, React, Tailwind CSS
Backend 	Python (Flask, Flask-SQLAlchemy, Flask-Migrate)
ML/NLP	 Scikit-learn, NLTK, pandas, numpy, sumy
Database	 SQLite
Other	 dotenv, logging, APScheduler, feedparser


📁 Project Structure

.
├── backend/         # Flask backend code
├── frontend/        # React + Tailwind frontend
├── datasets/        # ML training/evaluation datasets
├── models/          # Trained ML models
├── logs/            # Log files
├── migrations/      # DB migrations via Alembic
├── instance/        # Instance configs (e.g., API keys)
├── requirements.txt # Python dependencies
├── .flaskenv        # Flask environment variables
└── README.md        # Project documentation


⚙️ Installation
1. Clone the Repository
git clone https://github.com/KartikAmbupe/Mini-Project-Sem-VI.git
cd Mini-Project-Sem-VI

2. Backend Setup
pip install -r requirements.txt
flask db upgrade
flask run

3. Frontend Setup
cd frontend
npm install
npm run dev

🧪 Usage
Open http://localhost:5173 (frontend) or http://localhost:5000 (backend API).

Summarizer: Condense news articles.

Aggregator: Browse current news from multiple sources.

Detector: Check if an article is potentially fake.

🤖 Machine Learning Approach
Summarization: Extractive, using cosine similarity and sentence ranking (NLP).

Fake News Detection: Classification (Naive Bayes/Logistic Regression on TF-IDF features).

Aggregation: Scheduled background jobs (APScheduler) pull articles via fetcher.py (NewsAPI, RSS), stored via SQLAlchemy in SQLite.


🙏 Acknowledgements
Datasets from open-source fake news and summarization projects.

Libraries: Flask, scikit-learn, pandas, NLTK, sumy, etc.

UI inspiration from open-source Tailwind CSS projects.



Happy coding! 🚀