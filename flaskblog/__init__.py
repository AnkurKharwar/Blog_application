import os
from email_validator import validate_email
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = '788be05d80e7f0fed58c823b5e575c00'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['Mail_SERVER'] = 'smtp.googlemail.com'
app.config['Mail_PORT'] = 587
app.config['Mail_USE_TLS'] = True
app.config['Mail_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['Mail_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from flaskblog import routes

