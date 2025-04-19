from backend import db
from datetime import datetime

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    content = db.Column(db.Text, nullable=False)
    published_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    source = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(100), nullable=False, default='Unknown')
    url = db.Column(db.String(500))
    image_url = db.Column(db.String(500))
    
    def __repr__(self):
        return f'<Article {self.title}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'published_at': self.published_at.isoformat() if self.published_at else None,
            'source': self.source,
            'category': self.category,
            'author': self.author,
            'url': self.url,
            'image': self.image_url
        }
