from app import db

class AuthorModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    forename = db.Column(db.String(255),  nullable=False)
    surname = db.Column(db.String(255),  nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def toString():
        print("jaödfkjöa")


    def __repr__(self):
        return '<Author %r>' % self.name