from flask import Blueprint,render_template,request,flash,redirect,url_for,current_app
from .models import User,Donated_book
from werkzeug.security import generate_password_hash,check_password_hash
from werkzeug.utils import secure_filename
from . import db
import os
from flask_login import login_user,login_required,logout_user,current_user

auth = Blueprint('auth',__name__)


# sign_in page
@auth.route('/signin',methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        
        full_name = request.form.get('full-name')
        email = request.form.get('email')
        password1 = request.form.get('password')
        password2 = request.form.get('confirm-password')
        location = request.form.get('location')
        
        user = User.query.filter_by(email=email).first()
        
        if user:
            flash('the email is already exist you can loge-in', category='error')
        elif len(email)<=4:
            flash(message='hey,the email must be greater than 4 character ',category = 'error')
        elif len(full_name)<3:
            flash(message='hey,the name must be greater than 2 character ',category = 'error')
        elif len(password1)<8:
            flash(message='hey,the password must be greater than 8 character ',category = 'error')
        elif password1 != password2:
            flash(message='hey, those passwords must be same ',category = 'error')
        elif len(location)<4:
            flash(message='hey,the location must be greater than 4 character ',category = 'error')
        else:
            new_user = User(email=email,name = full_name,password=generate_password_hash(password1,method='pbkdf2:sha256'))
            db.session.add(new_user)             #adding datas to the data base
            db.session.commit()                #creating new data base
            # login_user(user,remember=True)
            flash(message='logged in successfully',category = 'success')
            
            return redirect(url_for('auth.login'))
    return render_template('signin.html', user=current_user)


# log_in page
@auth.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user:
            if check_password_hash(user.password,password):
                flash('Logged in successfully', category = 'success')
                login_user(user,remember=True)
                return redirect(url_for('auth.user_dash'))
            else:
                flash('logged in failed, check your password is correct', category='error')
        else:
            flash('email does not exist, create your account ', category='error')
            
    return render_template('login.html',user=current_user)


# user dashboard
@auth.route('/user_dash', methods = ['GET','POST'])
@login_required
def user_dash():
    name = (current_user.name).title()
    email = current_user.email
    
        
    if request.method == 'POST':
        action = request.form.get("action")
        # user = User.query.filter_by(email=email).first()
        
        if action=='book_remove':
            book_id = request.form.get('book_id')
            book = Donated_book.query.get_or_404(book_id)
            db.session.delete(book)
            db.session.commit()
            flash("Book removed successfully!", "success")
            return redirect(url_for('auth.user_dash'))
        
        if action=='logout':
            logout_user()
            flash(message='hey, your logout from Liboo library. ',category = 'info')
            return redirect(url_for('auth.login'))
            
            
    donated_books = Donated_book.query.filter_by(user_id=current_user.id).all()
    donated_count = Donated_book.query.filter_by(user_id=current_user.id).count()
    return render_template('/user_dash.html',user=current_user,name=name,email=email,donated_books=donated_books,donated_count=donated_count)


# book_listing page
# @auth.route('/user_dash/book_listing', methods = ['GET','POST'])
# @login_required
# def book_listing():
#     return render_template('book_listing.html',user=current_user)


# book_searching page
@auth.route('/user_dash/search_book', methods = ['GET','POST'])
@login_required
def search_book():
    books = Donated_book.query.all()
    return render_template('search_book.html',user=current_user,books=books)


# book_details page
@auth.route('/user_dash/search_book/book_details/<int:book_id>', methods = ['GET','POST'])
@login_required
def book_details(book_id):
    book = Donated_book.query.get_or_404(book_id)
    donor = book.donor
    return render_template('book_details.html',user=current_user,book=book,donor=donor)


# request_status
@auth.route('/user_dash/request_status', methods = ['GET','POST'])
@login_required
def request_status():
    return render_template('request_status.html',user=current_user)


# book_donation
@auth.route('/user_dash/book_donation', methods = ['GET','POST'])
@login_required
def book_donation():
    
    if request.method == "POST":
        book_name = request.form.get('title')
        author_name = request.form.get('author')
        category = request.form.get('category')
        published_year = request.form.get('publishedYear')
        publisher = request.form.get('publisher')
        file = request.files.get('coverImage')
        description = request.form.get('description')
        location = request.form.get('location')
        
        #return render_template('book_donation.html')
        
        if file and file.filename !='':
            filename = secure_filename(file.filename)
            upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(upload_path)
            cover_image = filename
        else:
            cover_image = 'no_image.png'
            
        if not description:
            description = 'Description is not mentioned'
        if not publisher:
            publisher = 'Publisher name is not mentioned'
        
        
        new_donation = Donated_book(
        book_name=book_name,
        author_name=author_name,
        category=category,
        published_year=published_year,
        cover_image=cover_image,
        description=description,
        location=location,
        user_id=current_user.id
        )
            
        db.session.add(new_donation)
        db.session.commit()
        flash('Thank you for donating! Your book is now listed in the library.', category='success')
        return redirect(url_for('auth.user_dash'))
        
        
    return render_template('book_donate.html',user=current_user)


# about_us page
@auth.route('/aboutus', methods = ['GET','POST'])
def aboutus():
    return render_template('aboutus.html',user=current_user)