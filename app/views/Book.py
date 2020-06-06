from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from app.model.Book import BookModel
from app.model.Author import AuthorModel


class Books(Resource):
    def get(self):
        books = BookModel.query.all()

        def to_json(x):
            author = AuthorModel.query.filter_by(id=x.author_id).first()
            return {
                'id': x.id,
                'title': x.title,
                'description': x.description,
                'author': author.forename + " " + author.surname,
                'image': x.image,
            }

        return {'Books': list(map(lambda x: to_json(x), books))}


class Book(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title')
        parser.add_argument('author_id')
        parser.add_argument('description')
        parser.add_argument('image')
        self.parser = parser

    def get(self, book_id):
        book = BookModel.query.filter_by(id=book_id).first()
        author = AuthorModel.query.filter_by(id=book.author_id).first().forename + AuthorModel.query.filter_by(
            id=book.author_id).first().surname
        return jsonify({'book': {
            'title': book.title,
            'author': author,
            'description': book.description,
            'image': book.image
        }})

    def post(self):
        data = self.parser.parse_args()
        new_Book = BookModel()
        new_Book.title = data['title']
        new_Book.description = data['description']
        new_Book.author_id = data['author_id']
        new_Book.image = data['image']
        try:
            new_Book.save_to_db()
            return {
                'message': 'Book {} was created'.format(data['title'])
            }
        except:
            return {'message': 'Something went wrong'}, 500

    def put(self, book_id):
        data = Book_parser.parse_args()
        book = BookModel.query.filter_by(id=book_id).first()
        book.title = data['title']
        book.description = data['description']
        book.author_id = data['author_id']
        book.image = data['image']
        try:
            book.save_to_db()
            return {
                'message': 'Book {} was updated'.format(data['title'])
            }
        except:
            return {'message': 'Something went wrong'}, 500
