from flask import Blueprint
from books.views import *
from models import Book

books = Blueprint('books', __name__, template_folder='templates')


@books.route('/')
def home():
    b = Book.query.all()
    return render_template('home.html')

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