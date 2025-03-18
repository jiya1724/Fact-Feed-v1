from flask import Flask, request, jsonify
from flask_cors import CORS
from detector import predict_news
from summerizer import summarize_text

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

@app.route('/')
def home():
    return "Fake News Detection & Summarization API is Running! Use /predict and /summarize."

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    try:
        data = request.json
        text = data.get("text", "")
        if not text:
            return jsonify({"error": "No text provided"}), 400

        result = predict_news(text)
        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
    try:
        data = request.json
        text = data.get("text", "")
        num_sentences = data.get("num_sentences", 2)

        if not text:
            return jsonify({"error": "No text provided"}), 400

        summary = summarize_text(text, num_sentences)
        return jsonify({"summary": summary})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
