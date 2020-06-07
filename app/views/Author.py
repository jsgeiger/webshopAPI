from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, abort
from app.model.Author import AuthorModel


class Authors(Resource):
    def get(self):
        authors = AuthorModel.query.all()

        def to_json(author):
            return {
                'id': author.id,
                'first_name': author.first_name,
                'last_name': author.last_name,
            }

        return jsonify({'Author': list(map(lambda x: to_json(x), authors))})


class Author(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('first_name')
        parser.add_argument('last_name')
        self.parser = parser

    def abort_if_author_doesnt_exists(self, author_id):
        author = AuthorModel.query.filter_by(id=author_id).first()
        if author is not None:
            return author
        else:
            abort(404, message="Author {} does not exist".format(author_id))

    def get(self, author_id):
        author = self.abort_if_author_doesnt_exists(author_id)

        return jsonify({'author': {
            'id': author.id,
            'first_name': author.first_name,
            'last_name': author.last_name
        }})

    def post(self):
        data = self.parser.parse_args()

        new_author = AuthorModel(
            first_name=data['first_name'],
            last_name=data['last_name'],
        )

        try:
            new_author.save_to_db()
            return {
                'message': 'Author {} was created'.format(data['last_name'])
            }
        except:
            return {'message': 'Author could not be saved'}, 500

    def put(self, author_id):
        data = self.parser.parse_args()
        author = self.abort_if_author_doesnt_exists(author_id)
        author.first_name = data['first_name']
        author.last_name = data['last_name']

        try:
            author.save_to_db()
            return {
                'message': 'Author {} {} was updated'.format(data['first_name'], data['last_name'])
            }
        except:
            return {'message': 'Author could not be updated'}, 500




