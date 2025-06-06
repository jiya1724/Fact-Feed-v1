import os
from flask import Flask, jsonify, request, send_from_directory
from backend import db, migrate, cors
from apscheduler.schedulers.background import BackgroundScheduler
import logging
from datetime import datetime

def create_app():
    app = Flask(__name__, static_folder="../frontend/dist")
    
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    # Configuration settings
    basedir = os.path.abspath(os.path.dirname(__file__))
    parent_dir = os.path.dirname(basedir)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(parent_dir, 'instance', 'news.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app, resources={r"/*": {"origins": "http://localhost:5173"}})


    # Import models and services
    from backend.models import Article
    from backend.roberta_detector import predict_news
    from backend.summerizer import summarize_text
    
    @app.route('/')
    def home():
        return "Fake News Detection & Summarization API is Running!"

    @app.route('/predict', methods=['POST'])
    def predict():
        data = request.json
        text = data.get("text", "")
        if not text:
            return jsonify({"error": "No text provided"}), 400

        result = predict_news(text)
        app.logger.info(f"Prediction made: {result} for text: {text[:100]}...")
        return jsonify({"prediction": result})

    @app.route('/summarize', methods=['POST'])
    def summarize():
        data = request.json
        text = data.get("text", "")
        num_sentences = data.get("num_sentences", 2)
        
        if not text:
            return jsonify({"error": "No text provided"}), 400
        
        summary = summarize_text(text, num_sentences)
        return jsonify({"summary": summary})
    
    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def serve(path):
        if path and os.path.exists(os.path.join(app.static_folder, path)):
            return send_from_directory(app.static_folder, path)
        return send_from_directory(app.static_folder, "index.html")

    @app.route('/api/news')
    def get_news():
        try:
            articles = Article.query.order_by(Article.published_at.desc()).limit(100).all()
            return jsonify([{
                'title': a.title,
                'content': a.content,
                'source': a.source,
                'published_at': a.published_at.isoformat() if a.published_at else None,
                'category': a.category,
                'author': a.author,
                'url': a.url,
                'image': a.image_url
            } for a in articles])
        except Exception as e:
            app.logger.error(f"News fetch error: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    @app.route('/api/news/filter')
    def filter_news():
        try:
            category = request.args.get('category')
            if not category or category == 'all':
                return get_news()
                
            articles = Article.query.filter_by(category=category).order_by(Article.published_at.desc()).limit(100).all()
            return jsonify([{
                'title': a.title,
                'content': a.content,
                'source': a.source,
                'published_at': a.published_at.isoformat() if a.published_at else None,
                'category': a.category,
                'author': a.author,
                'url': a.url,
                'image': a.image_url
            } for a in articles])
        except Exception as e:
            app.logger.error(f"Filter news error: {str(e)}")
            return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    @app.route('/api/categories')
    def get_categories():
        try:
            # Return all available categories from database
            categories = db.session.query(Article.category).distinct().all()
            category_list = ['general', 'technology', 'politics', 'environment']
            
            # Add any additional categories from database
            for category in categories:
                if category[0] and category[0] not in category_list:
                    category_list.append(category[0])
                    
            return jsonify(category_list)
        except Exception as e:
            app.logger.error(f"Categories fetch error: {str(e)}")
            return jsonify(["general", "technology", "politics", "environment"]), 500

    # Background news fetching using cron instead of interval for better reliability
    def scheduled_fetch():
        with app.app_context():
            try:
                from backend.aggregator.fetcher import fetch_news
                from backend.aggregator.storage import store_articles
                logger.info(f"Running scheduled fetch at {datetime.now()}")
                articles = fetch_news()
                new_count = store_articles(articles)
                logger.info(f"Added {new_count} new articles")
            except Exception as e:
                logger.error(f"Scheduled fetch error: {str(e)}")

    # Set up scheduler with cron schedule instead of interval
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_fetch, 'cron', minute='*/5')  # Run every 5 minutes
    scheduler.start()

    # Ensure database connections are properly closed
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    return app

# App instance creation
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
