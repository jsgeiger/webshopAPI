from app.views.Book import Book, Books
from app.views.Author import Author, Authors
from app.views.User import User, Users
from app.views.Roles import UserRole, Roles


def create_routes(api):
    api.add_resource(Books, '/api/books')
    api.add_resource(Book, '/api/book/<int:book_id>', '/api/book')
    api.add_resource(Authors, '/api/authors')
    api.add_resource(Author, '/api/author/<int:author_id>', '/api/author')
    api.add_resource(UserRole, '/api/role')
    api.add_resource(Roles, '/api/roles')
    api.add_resource(Users, '/api/users')
    api.add_resource(User, '/api/user', '/api/user/<int:user_id>')


