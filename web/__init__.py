# Configuration and initialization
# from .serve import app, db

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initiate Flask app
app = Flask(__name__)

#can change to postgresql here
# URI = 'sqlite:///:memory:'

#for locally testing
# db_path = os.path.join(os.path.dirname(__file__), 'database.db')
# URI = 'sqlite:///{}'.format(db_path)
if app.config['TESTING'] == True:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
PHOTO = os.path.join('static/')
app.config['UPLOAD_FOLDER'] = PHOTO

# Instantiate SQLAlchemy
db = SQLAlchemy(app)

from web import serve
