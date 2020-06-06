from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from app.model.User import UserModel


class Users(Resource):
    def get(self):
        users = UserModel.query.all()

        def to_json(x):
            return {
                'id': x.id,
                'username': x.username,
                'forename': x.foranme,
                'surname': x.surname,
                'roles': x.roles,
            }

        return {'Users': list(map(lambda x: to_json(x), users))}


class User(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username')
        parser.add_argument('forename')
        parser.add_argument('surname')
        parser.add_argument('password')
        parser.add_argument('roles')
        self.parser = parser

    def get(self, user_id):
        user = UserModel.query.filter_by(id=user_id).first()

        return jsonify({'User': {
            'id': user.id,
            'username': user.username,
            'forename': user.forename,
            'surname': user.surname,
            'roles': user.roles
        }})

    def post(self):
        data = self.parser.parse_args()
        new_user = UserModel()
        new_user.username = data['username']
        new_user.forename = data['forename']
        new_user.surname = data['surname']
        new_user.password = data['password']
        new_user.roles = [data['roles']]

        try:
            new_user.save_to_db()
            return {
                'message': 'User {} was created'.format(data['username'])
            }
        except:
            return {'message': 'Something went wrong'}, 500
