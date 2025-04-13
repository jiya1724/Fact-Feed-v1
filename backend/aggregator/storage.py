from backend import db
from backend.models import Article

def store_articles(articles):
    new_count = 0
    for article in articles:
        exists = Article.query.filter_by(title=article['title']).first()
        if not exists:
            new_article = Article(
                title=article['title'],
                content=article['content'],
                source=article['source'],
                published_at=article['published_at'],
                category=article['category'],
                author=article.get('author', 'Unknown')  # Add default author value
            )
            db.session.add(new_article)
            new_count += 1
    db.session.commit()
    return new_count

def get_articles():
    """Retrieve all articles from the database."""
    return Article.query.order_by(Article.published_at.desc()).all()
