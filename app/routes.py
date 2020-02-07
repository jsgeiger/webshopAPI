from app import app
from flask import Flask, request, after_this_request, jsonify, abort, request, make_response
from flask_restful import Resource, Api

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
    'author': request.json['author']
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

if __name__ == '__main__':
    app.run(host='localhost', port=5000)