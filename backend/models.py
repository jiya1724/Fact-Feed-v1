from backend import db
from datetime import datetime

class Article(db.Model):
    __tablename__ = 'article'  # Explicitly define table name
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    content = db.Column(db.Text, nullable=False)
    published_at = db.Column(db.DateTime, nullable=False)
    source = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)  # Added author column
    
    def __repr__(self):
        return f"<Article {self.title}>"
