from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)

from app.rescources import routes

#db.create_all()

app.run(host='0.0.0.0', debug=True)