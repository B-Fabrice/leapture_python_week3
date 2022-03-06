from flask import render_template, request
from models import Book
from flask import Blueprint

books = Blueprint('books', __name__, template_folder='templates')

def home_view():
    Book.query.all()
    return render_template('home.html')

def add_view():
    if request.method == 'POST':
        print("data are: ", request.form['title'])
        print("data are: ", request.form['author'])
        print("data are: ", request.form['summary'])
        print("data are: ", request.form['body'])
    return render_template('add.html')

def book_view(id):
    return render_template('book.html')

def update_view(id):
    return render_template('update.html')

def page404_view(error):
    return render_template('page404.html')