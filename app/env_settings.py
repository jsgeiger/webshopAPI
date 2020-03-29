import os

# Flask-SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
