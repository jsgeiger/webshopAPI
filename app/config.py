import os


class Config(object):
    DEBUG = False
    TESTING = False
    APP_NAME = "WebshopAPI"
    SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@mysql:%s/%s" % (
        os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWORD'], os.environ['DATABASE_PORT'],
        os.environ['DATABASE_NAME'],)
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    JSON_SORT_KEYS = False

    # Flask-SQLAlchemy settings
    SQLALCHEMY_ENGINE_OPTIONS = {'pool_size': 100, 'pool_recycle': 280}

    # Flask-User settings
    # USER_ENABLE_EMAIL = False  # Disable email authentication
    # USER_ENABLE_USERNAME = True  # Enable username authentication
    # USER_REQUIRE_RETYPE_PASSWORD = False  # Simplify register form
