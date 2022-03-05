from multiprocessing import Manager
from flask import Flask
import sqlalchemy
from views import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lksnlskndlknvlskndlvknew2382y983hwfo0923u'
app.debug = True

# manager = Manager(app)
# db = sqlalchemy(app)

@app.route('/')
def home():
    return home_view()

@app.route('/add', methods=['POST', 'GET'])
def add():
    return add_view()

@app.route('/book/<int:id>')
def book(id):
    return book_view(id)

@app.route('/update/<int:id>')
def update(id):
    return update_view(id)

@app.errorhandler(404)
def page404(error):
    return page404_view(error)

if __name__ == '__main__':
    app.run()