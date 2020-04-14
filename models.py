from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flasql'
db = SQLAlchemy(app)

class Videogame(db.Model):
    __tablename__ = 'videogames'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    company = db.Column(db.String, unique=True, nullable=False)
    esrb = db.Column(db.String, nullable=False)

    def __repr(self):
        return f("Videogame(id='{self.id}', name='{self.name}', company='{self.company}', esrb='{self.esrb}')")