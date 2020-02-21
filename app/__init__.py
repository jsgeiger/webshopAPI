from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootroot@localhost:3306/WebshopAPI'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app.route import routes
db = SQLAlchemy()
db.init_app(app)

app.run(debug=True)