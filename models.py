from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Person(db.Model, SerializerMixin):
    __tablename__ = "people"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())

    def validate_name(self, name):
        if not name and not isinstance(name, str):
            raise TypeError()
        return True

    def __init__(self, username):
        self.validate_name(username)
        self.username = username

    def set_name(self, username):
        self.validate_name(username)
        self.username = username
