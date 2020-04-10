from app import api
from flask import Flask, request, after_this_request, jsonify, request, make_response
from flask_restful import Resource, Api, abort, reqparse
from app.model.Author import AuthorModel
from app.model.Book import BookModel
from app.model.User import UserModel
from app.model import Role


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


api.add_resource(Books, '/api/books')

Book_parser = reqparse.RequestParser()
Book_parser.add_argument('title')
Book_parser.add_argument('author_id')
Book_parser.add_argument('description')
Book_parser.add_argument('image')


class Book(Resource):
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
        data = Book_parser.parse_args()
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


api.add_resource(Book, '/api/book/<int:book_id>', '/api/book')


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


api.add_resource(Authors, '/api/authors')

Author_parser = reqparse.RequestParser()
Author_parser.add_argument('forename')
Author_parser.add_argument('surname')


class Author(Resource):
    def get(self, author_id):
        author = AuthorModel.query.filter_by(id=author_id).first()
        return {'author': {
            'forename': author.forename,
            'surname': author.surname
        }}

    def post(self):
        data = Author_parser.parse_args()
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


api.add_resource(Author, '/api/author/<int:author_id>', '/api/author')

Role_parser = reqparse.RequestParser()
Role_parser.add_argument('name')


class UserRole(Resource):
    def post(self):
        data = Role_parser.parse_args()
        new_role = Role(name=data['name'])

        try:
            new_role.save_to_db()
            return {
                'message': 'Role {} was created'.format(data['name'])
            }
        except:
            return {'message': 'Something went wrong'}, 500


api.add_resource(UserRole, '/api/role')


class Roles(Resource):
    def get(self):
        roles = Role.query.all()

        def to_json(x):
            return {
                'id': x.id,
                'surname': x.name,
            }

        return {'Roles': list(map(lambda x: to_json(x), roles))}


api.add_resource(Roles, '/api/roles')


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


api.add_resource(Users, '/api/users')

User_parser = reqparse.RequestParser()
User_parser.add_argument('username')
User_parser.add_argument('forename')
User_parser.add_argument('surname')
User_parser.add_argument('password')
User_parser.add_argument('roles')


class User(Resource):
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
        data = User_parser.parse_args()
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


api.add_resource(User, '/api/user', '/api/user/<int:user_id>')
