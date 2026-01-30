from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from os import path, makedirs
from flask_login import LoginManager

db = SQLAlchemy()    #database object
DB_NAME = 'database.db'   #database name
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'akkopikko123'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'    #database located
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    
    # 🖼️ Upload folder setup
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/uploads')
    makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    db.init_app(app)     #initialization
    migrate = Migrate(app, db)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    
    from .models import User,Note,Donated_book
    
    create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app

def create_database(app):
    if not path.exists('library/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('created database !')