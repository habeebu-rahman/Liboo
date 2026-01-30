from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import date


class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    data =  db.Column(db.String(1000))
    date =  db.Column(db.DateTime(timezone = True),default=func.now())
    user_id =  db.Column(db.Integer,db.ForeignKey('user.id'))
    donated_id =  db.Column(db.Integer,db.ForeignKey('donated_book.id'))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(100),unique=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(50))
    notes = db.relationship('Note')
    donations = db.relationship('Donated_book',backref="donor")
    
    
class Donated_book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    book_name = db.Column(db.String(200))
    author_name = db.Column(db.String(150))
    category = db.Column(db.String(10))
    published_year = db.Column(db.Integer)
    cover_image = db.Column(db.String(250))
    description = db.Column(db.Text)
    location = db.Column(db.String(200))
    # date =  db.Column(db.Date, default=func.current_date())
    user_id =  db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship('User')
    notes = db.relationship('Note')