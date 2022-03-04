import http
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/book/<str:id>')
def book(id):
    return render_template('book.html')

@app.route('/update/<str:id>')
def update(id):
    return render_template('book.html')

@app.errorhandler(404)
def page404(error):
    return render_template('page404.html')