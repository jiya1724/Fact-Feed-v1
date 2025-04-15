import requests
import feedparser
from datetime import datetime
from backend.app import create_app
from backend.aggregator.storage import store_articles

def fetch_news():
    articles = []

    # NewsAPI integration
    try:
        newsapi_params = {
            'country': 'in',
            'apiKey': 'ab6877a9ab494ade88a22812b4a84c82'
        }
        newsapi_response = requests.get(
            'https://newsapi.org/v2/top-headlines',
            params=newsapi_params,
            timeout=10
        )
        if newsapi_response.status_code == 200:
            for item in newsapi_response.json().get('articles', []):
                articles.append({
                    'title': item['title'],
                    'content': item['content'] or item['description'],
                    'source': item['source']['name'],
                    'published_at': datetime.strptime(item['publishedAt'], "%Y-%m-%dT%H:%M:%SZ"),
                    'category': 'general',
                    'author': item.get('author', 'Unknown'),
                    'url': item.get('url')  # ✅ ADD THIS
                })
    except Exception as e:
        print(f"NewsAPI Error: {str(e)}")

    # RSS Feed integration
    try:
        feed = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml')
        for entry in feed.entries:
            articles.append({
                'title': entry.title,
                'content': entry.description,
                'source': 'BBC',
                'published_at': datetime.now(),
                'category': 'general',
                'author': entry.get('author', 'Unknown'),
                'url': entry.link  # ✅ ADD THIS
            })
    except Exception as e:
        print(f"RSS Error: {str(e)}")

    return articles


if __name__ == "__main__":
    # Flask app context for database operations
    app = create_app()
    with app.app_context():
        print("Fetching news articles...")
        articles = fetch_news()
        print(f"Fetched {len(articles)} articles")

        print("Storing articles in database...")
        new_count = store_articles(articles)
        print(f"Added {new_count} new articles to database")
