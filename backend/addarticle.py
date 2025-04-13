import sys
import os
from datetime import datetime

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.app import create_app
from backend.models import Article, db

app = create_app()

with app.app_context():
    new_article = Article(
        title="Sample News",
        content="This is a sample news article content.",
        source="Sample Source",
        category="general",
        author="Admin",
        published_at=datetime.now()
    )
    db.session.add(new_article)
    db.session.commit()
    print("Test article added!")
