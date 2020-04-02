from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
from flask_user import UserManager

app = Flask(__name__)
CORS(app)
db = SQLAlchemy(app)
api = Api(app)

app.config.from_object('app.settings')
app.config.from_object('app.env_settings')

from app.rescources import routes
from app.model import Book, Author, User

db.create_all()

user_manager = UserManager(app, db, User)


@app.context_processor
def context_processor():
    return dict(user_manager=user_manager)


app.run(host='0.0.0.0', port=4300, debug=True)
