from app import app, db
from books.blueprint import books

app.register_blueprint(books, url_prefix='/')

if __name__ == '__main__':
    app.run()