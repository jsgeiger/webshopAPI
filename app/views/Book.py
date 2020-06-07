from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, abort
from app.model.Book import BookModel
from app.model.Author import AuthorModel


class Books(Resource):
    def get(self):
        books = BookModel.query.all()

        def to_json(book):
            author = AuthorModel.query.filter_by(id=book.author_id).first()
            return {
                'id': book.id,
                'title': book.title,
                'author': '%s %s' % (author.forename, author.surname),
                'description': book.description,
                'image': book.image,
            }

        return jsonify({'Books': list(map(lambda x: to_json(x), books))})


class Book(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title')
        parser.add_argument('author_id')
        parser.add_argument('description')
        parser.add_argument('image')
        self.parser = parser

    def abort_if_book_doesnt_exists(self, book_id):
        book = BookModel.query.filter_by(id=book_id).first()
        if book is not None:
            return book
        else:
            abort(404, message="Book {} does not exist".format(book_id))

    def get(self, book_id):
        book = self.abort_if_book_doesnt_exists(book_id)
        author = AuthorModel.query.filter_by(id=book.author_id).first()

        return jsonify({'book': {
            'id': book.id,
            'title': book.title,
            'author': '%s %s' % (author.forename, author.surname),
            'description': book.description,
            'image': book.image
        }})

    def post(self):
        data = self.parser.parse_args()

        new_book = BookModel(
            title=data['title'],
            description=data['title'],
            author_id=data['author_id'],
            image=data['image'],
        )

        try:
            new_book.save_to_db()
            return {
                'message': 'Book {} was created'.format(data['title'])
            }
        except:
            return {'message': 'Book could not be saved'}, 500

    def put(self, book_id):
        data = self.parser.parse_args()
        book = self.abort_if_book_doesnt_exists(book_id)
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
            return {'message': 'Book could not be updated'}, 500
