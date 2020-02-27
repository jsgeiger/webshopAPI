from app import db

class Book:
     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
     name = db.Column(db.String(255),  nullable=False)
     description = db.Column(db.String(255),  nullable=False)
     image = db.Column(db.String(255))
     author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

     def __repr__(self):
             return '<Book %r>' % self.name