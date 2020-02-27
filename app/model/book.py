from app import db

class BookModel(db.Model):
     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
     title = db.Column(db.String(255),  nullable=False)
     description = db.Column(db.String(255),  nullable=False)
     image = db.Column(db.String(255))
     author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

     def save_to_db(self):
        db.session.add(self)
        db.session.commit()

     def __repr__(self):
             return '<Book %r>' % self.title