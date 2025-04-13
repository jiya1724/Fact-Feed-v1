from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

# Create a single SQLAlchemy instance for the entire application
db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
