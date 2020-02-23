class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    forename = db.Column(db.String(255),  nullable=False)
    surname = db.Column(db.String(255),  nullable=False)

    def __repr__(self):
        return '<Author %r>' % self.name