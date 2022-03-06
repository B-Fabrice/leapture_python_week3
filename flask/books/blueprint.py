from flask import Blueprint
from views import *

books = Blueprint('books', __name__, template_folder='templates')


@books.route('/')
def home():
    return home_view()

@books.route('/add', methods=['POST', 'GET'])
def add():
    return add_view()

@books.route('/book/<int:id>')
def book(id):
    return book_view(id)

@books.route('/update/<int:id>')
def update(id):
    return update_view(id)

@books.errorhandler(404)
def page404(error):
    return page404_view(error)