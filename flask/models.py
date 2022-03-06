from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), unique=True, nullable=True)
    author = db.Column(db.String(50))
    summary = db.Column(db.String(255))
    body = db.Column(db.Text)