from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_user import UserManager
from app.model import User
from app.views import create_routes
import app.config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    from app.model import db
    db.init_app(app)

    from app.model.User import UserModel
    from app.model.Author import AuthorModel
    from app.model.Book import BookModel
    with app.app_context():
        db.create_all()

    CORS(app)
    api = Api(app)
    create_routes(api)

    return app
