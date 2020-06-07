from app.model import db


class AuthorModel(db.Model):
    __tablename__ = 'author_model'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    forename = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Author %r>' % self.surname
