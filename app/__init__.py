from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
import os
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

from app.rescources import routes
from app.model import book, author

db.create_all()

app.run(host='0.0.0.0', port=4300, debug=True)