from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from app.model.Role import Role


class UserRole(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        self.parser = parser

    def get(self, role_id):
        role = Role.query.filter_by(id=role_id).first()

        return jsonify({'User': {
            'id': role.id,
            'name': role.name
        }})

    def post(self):
        data = self.parser.parse_args()
        new_role = Role(name=data['name'])

        try:
            new_role.save_to_db()
            return {
                'message': 'Role {} was created'.format(data['name'])
            }
        except:
            return {'message': 'Something went wrong'}, 500


class Roles(Resource):
    def get(self):
        roles = Role.query.all()

        def to_json(x):
            return {
                'id': x.id,
                'surname': x.name,
            }

        return {'Roles': list(map(lambda x: to_json(x), roles))}
