from app import app, db
from flask import Flask, request, after_this_request, jsonify, request, make_response
from flask_restful import Resource, Api, abort, reqparse
from app.model.author import AuthorModel
from app.model.book import Book

api = Api(app)

books = [
  {
    'id': 1,
    'title': 'Mögest du glücklich sein1',
    'author': 'Laura Malina Seiler', 
    'description': 'In dem Buch "Mögest du glücklich sein" erfährst du, wie du dich mit deinem Higher Self verbindest, Blockaden auflöst, alten emotionalen Schmerz heilst und dich von deinen Ängsten befreist. Das Buch enthält zahlreiche kraftvolle Coaching-Übungen, heilende Meditationen und Geschichten, die inspirieren und dir dabei helfen, dich selbst in einem kraftvollen neuen Licht zu sehen. Laura Malina Seiler nimmt dich mit auf eine wunderschöne Reise zu dir selbst, die dich in Kontakt mit deiner wahren Essenz bringt.',
    'image': '/img/test.png'
  },
  {
    'id': 2,
    'title': 'Mögest du glücklich sein2',
    'author': 'Laura Malina Seiler', 
    'description': 'In dem Buch "Mögest du glücklich sein" erfährst du, wie du dich mit deinem Higher Self verbindest, Blockaden auflöst, alten emotionalen Schmerz heilst und dich von deinen Ängsten befreist. Das Buch enthält zahlreiche kraftvolle Coaching-Übungen, heilende Meditationen und Geschichten, die inspirieren und dir dabei helfen, dich selbst in einem kraftvollen neuen Licht zu sehen. Laura Malina Seiler nimmt dich mit auf eine wunderschöne Reise zu dir selbst, die dich in Kontakt mit deiner wahren Essenz bringt.',
    'image': '/img/test.png'
  },
  {
    'id': 3,
    'title': 'Mögest du glücklich sein3',
    'author': 'Laura Malina Seiler', 
    'description': 'In dem Buch "Mögest du glücklich sein" erfährst du, wie du dich mit deinem Higher Self verbindest, Blockade n auflöst, alten emotionalen Schmerz heilst und dich von deinen Ängsten befreist. Das Buch enthält zahlreiche kraftvolle Coaching-Übungen, heilende Meditationen und Geschichten, die inspirieren und dir dabei helfen, dich selbst in einem kraftvollen neuen Licht zu sehen. Laura Malina Seiler nimmt dich mit auf eine wunderschöne Reise zu dir selbst, die dich in Kontakt mit deiner wahren Essenz bringt.',
    'image': '/img/test.png'
  }
]

@app.route("/")
def index():
  return "REST API for Webshop"

@app.route("/books", methods=['GET'])
def get_all_books():
  @after_this_request
  def add_header(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

  return jsonify({'books': books})
  
@app.route('/book/<int:book_id>', methods=['GET'])
def get_book(book_id):
  for book in books:
    if(book['id'] == book_id):
      return jsonify(book)
    else: abort(404)

@app.route('/book', methods=['POST'])
def create_book():
  book = {
    'id': len(books),
    'title': request.json['title'],
    'description': request.json['description'],
    'author_id': Author.query.filter_by(name=request.json['author']).first()
  }
  books.append(book)

  return jsonify({'book': book}),201

@app.route('/book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
  for book in books:
    if(book['id'] == book_id):
      book['title'] = request.json['title']
      book['description'] = request.json['description']
      book['author'] = request.json['author']
      return jsonify({'book': book}),201
    else: abort(404)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def abort_if_book_doesnt_exist(book_id):
  for book in books:
    if(book['id'] == book_id):
      return book

  abort(404, message="Book {} doesn't exist".format(book_id))

class Books(Resource):
  def get(self):
    return jsonify({'books': books})

api.add_resource(Books, '/api/books')

class Book(Resource):
  def get(self, book_id):
      return jsonify({'book': abort_if_book_doesnt_exist(book_id)})

api.add_resource(Book, '/api/book/<int:book_id>')

Author_parser = reqparse.RequestParser()
Author_parser.add_argument('forename')
Author_parser.add_argument('surname')

class Author(Resource):
    def get(self, author_id):
        #return print(AuthorModel.query.filter_by(id=author_id).first())
        author = AuthorModel.query.filter_by(id=author_id).first()
        return {'author': {
          'forname': author.forename,
          'surname': author.surname
        }}
        
    def post(self):
        data = Author_parser.parse_args()
        new_author =  AuthorModel()
        new_author.surname = data['surname']
        new_author.forename = data['forename']

        new_author.save_to_db()

        try:
            return {
                'message': 'User {} was created'.format(data['surname'])
            }
        except:
            return {'message': 'Something went wrong'}, 500

api.add_resource(Author, '/api/author/<int:author_id>')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)