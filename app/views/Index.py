from flask import Flask, jsonify
from flask_restful import Resource


class Index(Resource):
    def get(self):
        return jsonify({'message': "Welcome to BookAPI"})
