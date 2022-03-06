from app import app, db
import views
from books.blueprint import books

app.register_blueprint(books, url_prefix='/')

if __name__ == '__main__':
    app.run()