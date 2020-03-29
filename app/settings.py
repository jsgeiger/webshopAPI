# Application settings
APP_NAME = "WebshopAPI"
APP_SYSTEM_ERROR_SUBJECT_LINE = APP_NAME + " system error"

# Flask settings
SECRET_KEY = 'This is an INSECURE secret!! DO NOT use this in production!!'

# Flask-SQLAlchemy settings
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask-User settings
USER_APP_NAME = "Webshop"  # Shown in and email templates and page footers
USER_ENABLE_EMAIL = False  # Disable email authentication
USER_ENABLE_USERNAME = True  # Enable username authentication
USER_REQUIRE_RETYPE_PASSWORD = False  # Simplify register form
