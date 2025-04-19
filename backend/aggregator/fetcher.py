import requests
import feedparser
from datetime import datetime
import logging
from backend.aggregator.news_sources import SOURCES
import time
import random

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_news():
    """Fetch news articles from multiple sources"""
    articles = []
    
    for source in SOURCES:
        # Add delay between requests to avoid rate limiting
        time.sleep(random.uniform(0.5, 1.5))
        
        if source['type'] == 'api':
            try:
                logger.info(f"Fetching from API: {source['url']}")
                response = requests.get(source['url'], params=source.get('params', {}), timeout=15)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    # Handle different API response structures
                    if 'articles' in data:
                        items = data['articles']
                    elif 'results' in data:
                        items = data['results']
                    else:
                        items = []
                        
                    for item in items:
                        try:
                            # Extract published date with fallbacks
                            if 'publishedAt' in item:
                                date_str = item['publishedAt']
                                date_format = "%Y-%m-%dT%H:%M:%SZ"
                            elif 'pubDate' in item:
                                date_str = item['pubDate']
                                date_format = "%Y-%m-%d %H:%M:%S"
                            else:
                                date_str = None
                                
                            published_at = datetime.strptime(date_str, date_format) if date_str else datetime.now()
                            
                            # Extract author with fallbacks
                            if 'author' in item and item['author']:
                                author = item['author']
                            elif 'creator' in item:
                                if isinstance(item['creator'], list):
                                    author = item['creator'][0] if item['creator'] else 'Unknown'
                                else:
                                    author = item['creator'] or 'Unknown'
                            else:
                                author = 'Unknown'
                                
                            # Create article object
                            articles.append({
                                'title': item.get('title', 'No Title'),
                                'content': item.get('description') or item.get('content') or 'No content available',
                                'source': item.get('source', {}).get('name') or source.get('name', 'API Source'),
                                'published_at': published_at,
                                'category': item.get('category') or source.get('category', 'general'),
                                'author': author,
                                'url': item.get('url') or item.get('link', '#'),
                                'image': item.get('urlToImage') or item.get('image_url') or item.get('image')
                            })
                        except Exception as e:
                            logger.error(f"Error processing API item: {str(e)}")
                else:
                    logger.error(f"API request failed with status code: {response.status_code}")
                    
            except Exception as e:
                logger.error(f"API Error: {str(e)}")

        elif source['type'] == 'rss':
            try:
                logger.info(f"Fetching from RSS: {source['url']}")
                feed = feedparser.parse(source['url'])
                
                for entry in feed.entries:
                    try:
                        # Extract content with fallbacks
                        content = getattr(entry, 'description', None) or getattr(entry, 'summary', '') or ''
                        
                        # Extract publish date with fallbacks
                        if hasattr(entry, 'published_parsed') and entry.published_parsed:
                            published_at = datetime(*entry.published_parsed[:6])
                        elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                            published_at = datetime(*entry.updated_parsed[:6])
                        else:
                            published_at = datetime.now()
                            
                        # Extract author with fallbacks
                        author = entry.get('author', 'Unknown')
                        if hasattr(entry, 'authors') and entry.authors:
                            author = entry.authors[0].get('name', author)
                        
                        # Extract image with multiple formats
                        image_url = None
                        if hasattr(entry, 'media_thumbnail') and entry.media_thumbnail:
                            image_url = entry.media_thumbnail[0].get('url')
                        elif hasattr(entry, 'media_content') and entry.media_content:
                            media_content = [m for m in entry.media_content if 'image' in m.get('type', '')]
                            if media_content:
                                image_url = media_content[0].get('url')
                        elif hasattr(entry, 'enclosures') and entry.enclosures:
                            for enc in entry.enclosures:
                                if enc.get('type', '').startswith('image/'):
                                    image_url = enc.get('href')
                                    break
                        
                        # Try to extract image from content if still not found
                        if not image_url and content:
                            import re
                            img_match = re.search(r'<img.*?src=["\'](.*?)["\']', content)
                            if img_match:
                                image_url = img_match.group(1)
                        
                        articles.append({
                            'title': entry.title,
                            'content': content,
                            'source': feed.feed.get('title', source.get('name', 'RSS Source')),
                            'published_at': published_at,
                            'category': source['category'],
                            'author': author,
                            'url': entry.link,
                            'image': image_url
                        })
                    except Exception as e:
                        logger.error(f"Error processing RSS entry: {str(e)}")
                        
            except Exception as e:
                logger.error(f"RSS Error: {str(e)}")

    logger.info(f"Fetched {len(articles)} articles total")
    return articles

if __name__ == "__main__":
    from backend.app import create_app
    app = create_app()
    with app.app_context():
        print("Fetching news articles...")
        articles = fetch_news()
        print(f"Fetched {len(articles)} articles")
        
        from backend.aggregator.storage import store_articles
        new_count = store_articles(articles)
        print(f"Added {new_count} new articles to database")
