from sqlalchemy import Column, Integer, String
from flask_appbuilder import Model

class Book(Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), unique=True, nullable=True)
    author = Column(String(50))
    summary = Column(String(255))
    body = Column(String(2000))