from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse, abort
from app.model.User import UserModel


class Users(Resource):
    def get(self):
        users = UserModel.query.all()

        def to_json(user):
            return {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }

        return jsonify({'Users': list(map(lambda x: to_json(x), users))})


class User(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username')
        parser.add_argument('first_name')
        parser.add_argument('last_name')
        parser.add_argument('password')
        self.parser = parser

    def abort_if_user_doesnt_exists(self, user_id):
        user = UserModel.query.filter_by(id=user_id).first()
        if user is not None:
            return user
        else:
            abort(404, message="User {} does not exist".format(user_id))

    def get(self, user_id):
        user = self.abort_if_user_doesnt_exists(user_id)

        return jsonify({'User': {
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }})

    def post(self):
        data = self.parser.parse_args()
        new_user = UserModel(
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
        )

        new_user.set_password(data['password'])

        try:
            new_user.save_to_db()
            return {
                'message': 'User {} was created'.format(data['username'])
            }
        except:
            return {'message': 'User could not be saved'}, 500

    def put(self, user_id):
        data = self.parser.parse_args()
        user = self.abort_if_user_doesnt_exists(user_id)
        user.set_password(data['password'])
        user.username = data['username']
        user.first_name = data['first_name']
        user.last_name = data['last_name']

        try:
            user.save_to_db()
            return {
                'message': 'User {} was updated'.format(data['username'])
            }
        except:
            return {'message': 'User could not be updated'}, 500

