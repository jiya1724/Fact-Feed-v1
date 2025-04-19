from backend.models import Article, db
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def store_articles(articles):
    """
    Store articles in database
    
    Args:
        articles: List of article dictionaries
        
    Returns:
        int: Number of new articles added
    """
    new_count = 0
    
    for article in articles:
        try:
            # Skip articles without title
            if not article.get('title'):
                continue
                
            # Check if article already exists to avoid duplicates
            exists = Article.query.filter_by(title=article['title']).first()
            
            if not exists:
                # Ensure author isn't None
                author = article.get('author')
                if not author:
                    author = 'Unknown'
                    
                # Create new article
                new_article = Article(
                    title=article['title'],
                    content=article.get('content', 'No content'),
                    source=article.get('source', 'Unknown Source'),
                    published_at=article.get('published_at'),
                    category=article.get('category', 'general'),
                    author=author,
                    url=article.get('url', '#'),
                    image_url=article.get('image')
                )
                
                # Add to database session
                db.session.add(new_article)
                new_count += 1
                
        except Exception as e:
            logger.error(f"Error storing article: {str(e)}")
            logger.error(f"Problematic article: {article.get('title')}")
            # Continue with next article instead of failing entire batch
            continue
    
    # Commit all changes at once
    try:
        db.session.commit()
        logger.info(f"Successfully added {new_count} new articles")
    except Exception as e:
        db.session.rollback()
        logger.error(f"Database commit error: {str(e)}")
        raise
        
    return new_count
