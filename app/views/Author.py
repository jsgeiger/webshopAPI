from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from app.model.Author import AuthorModel


class Authors(Resource):
    def get(self):
        authors = AuthorModel.query.all()

        def to_json(x):
            return {
                'id': x.id,
                'forename': x.forename,
                'surname': x.surname,
            }

        return {'Authors': list(map(lambda x: to_json(x), authors))}


class Author(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('forename')
        parser.add_argument('surname')
        self.parser = parser

    def get(self, author_id):
        author = AuthorModel.query.filter_by(id=author_id).first()
        return {'author': {
            'forename': author.forename,
            'surname': author.surname
        }}

    def post(self):
        data = self.parser.parse_args()
        new_author = AuthorModel()
        new_author.surname = data['surname']
        new_author.forename = data['forename']

        try:
            new_author.save_to_db()
            return {
                'message': 'Author {} was created'.format(data['surname'])
            }
        except:
            return {'message': 'Something went wrong'}, 500
