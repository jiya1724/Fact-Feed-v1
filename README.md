# News Summarizer, Aggregator and Fake News Detection


📝 Project Overview
This project is a web-based application that enables users to:​

Summarize lengthy news articles using advanced Natural Language Processing (NLP) techniques.

Aggregate news from multiple sources for comprehensive coverage.

Detect and flag potentially fake news content to ensure information reliability.​

The application leverages Python for backend processing, TypeScript for frontend development, and integrates various machine learning models for NLP tasks.​

🚀 Features
Text Summarization: Condenses articles to their essential points.

News Aggregation: Collects news from diverse sources for a unified view.

Fake News Detection: Analyzes content to identify misinformation.​

🛠️ Technologies Used
Backend: Python, Flask

Frontend: TypeScript, HTML, CSS

Machine Learning: Scikit-learn, TensorFlow

Database: SQLite​

📁 Project Structure
├── backend/               # Backend API and server logic
├── frontend/              # Frontend application
├── datasets/              # Datasets for training and evaluation
├── models/                # Pre-trained and custom ML models
├── logs/                  # Log files for monitoring
├── migrations/            # Database migration files
├── instance/              # Instance-specific configurations
├── .flaskenv              # Flask environment variables
├── cosine_summarizer.py   # Script for cosine similarity summarization
├── summarize.py           # Main summarization script
└── README.md              # Project documentation


⚙️ Installation
1.Clone the repository:git clone https://github.com/KartikAmbupe/Mini-Project-Sem-VI.git
cd Mini-Project-Sem-VI


2.Install dependencies:
pip install -r requirements.txt


3.Run database migrations (if applicable):
flask db upgrade

4.Run the application:
flask run

🧪 Usage
Access the application via http://localhost:5000.

Navigate through the interface to summarize articles, view aggregated news, and check for fake news detection.​

🛠️ Tech Stack
Layer	Technology
Frontend	TypeScript, JavaScript, HTML, CSS, Mako templates
Backend	Python (Flask)
ML/NLP	Python (scikit-learn, pandas, numpy, nltk)
Data	Custom datasets for fake news detection and summarization
Other	Shell scripts, logging, migrations, Flask environment


🤖 Machine Learning Approach
Summarization: Uses cosine similarity and NLP techniques to extract key sentences and generate summaries.

Fake News Detection: Trained on labeled datasets using algorithms such as Naive Bayes or Logistic Regression. Text is preprocessed, vectorized (e.g., TF-IDF), and classified as real or fake.



🙏 Acknowledgements
Datasets and inspiration from open-source fake news detection and summarization projects.

Flask, scikit-learn, and other open-source libraries.
Happy coding! 🚀
