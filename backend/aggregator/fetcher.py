import requests
import feedparser
from datetime import datetime

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
                    'author': item.get('author', 'Unknown')  # Default author value if missing
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
                'published_at': datetime.now(),  # Use current time for RSS feeds
                'category': 'general',
                'author': entry.get('author', 'Unknown')  # Default author value if missing
            })
    except Exception as e:
        print(f"RSS Error: {str(e)}")

    return articles
