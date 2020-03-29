from app import db

from flask_user import UserMixin


class UserModel(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')
    forename = db.Column(db.String(100), nullable=False, server_default='')
    surname = db.Column(db.String(100), nullable=False, server_default='')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<User %r>' % self.username
