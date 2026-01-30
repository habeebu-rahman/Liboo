from flask import Blueprint,render_template
from flask_login import login_required,current_user
from .models import Donated_book;

views = Blueprint('views',__name__)

@views.route('/')
def home():
    books = Donated_book.query.order_by(Donated_book.id.desc()).limit(4).all()
    return render_template('home1.html',user=current_user,books=books)