# backend/aggregator/news_sources.py
SOURCES = [
    {
        'type': 'rss',
        'url': 'http://feeds.bbci.co.uk/news/rss.xml',
        'category': 'general'
    },
    {
        'type': 'api',
        'url': 'https://newsapi.org/v2/top-headlines',
        'params': {
            'country': 'in',
            'apiKey': 'ab6877a9ab494ade88a22812b4a84c82'
        }
    }
]
