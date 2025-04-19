# List of news sources to fetch from
# Includes both RSS feeds and API sources

SOURCES = [
    # RSS Sources
    {
        'type': 'rss',
        'url': 'http://feeds.bbci.co.uk/news/rss.xml',
        'category': 'general',
        'name': 'BBC News'
    },
    {
        'type': 'rss',
        'url': 'http://rss.cnn.com/rss/edition.rss',
        'category': 'general',
        'name': 'CNN'
    },
    {
        'type': 'rss',
        'url': 'https://techcrunch.com/feed/',
        'category': 'technology',
        'name': 'TechCrunch'
    },
    {
        'type': 'rss',
        'url': 'https://www.wired.com/feed/rss',
        'category': 'technology',
        'name': 'Wired'
    },
    {
        'type': 'rss',
        'url': 'https://feeds.npr.org/1001/rss.xml',
        'category': 'general',
        'name': 'NPR'
    },
    {
        'type': 'rss',
        'url': 'https://www.theguardian.com/environment/rss',
        'category': 'environment',
        'name': 'The Guardian - Environment'
    },
    {
        'type': 'rss',
        'url': 'https://feeds.nbcnews.com/nbcnews/public/politics',
        'category': 'politics',
        'name': 'NBC Politics'
    },
    
    # API Sources - Use your own API key
    {
        'type': 'api',
        'url': 'https://newsapi.org/v2/top-headlines',
        'params': {
            'apiKey': 'ab6877a9ab494ade88a22812b4a84c82',  # Replace with your actual API key
            'country': 'us',
            'category': 'technology'
        },
        'category': 'technology',
        'name': 'NewsAPI Tech'
    },
    {
        'type': 'api',
        'url': 'https://newsapi.org/v2/top-headlines',
        'params': {
            'apiKey': 'ab6877a9ab494ade88a22812b4a84c82',  # Replace with your actual API key
            'country': 'us',
            'category': 'politics'
        },
        'category': 'politics',
        'name': 'NewsAPI Politics'
    }
]
