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
db_path = os.path.join(os.path.dirname(__file__), 'database.db')
URI = 'sqlite:///{}'.format(db_path)

app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

# Instantiate SQLAlchemy
db = SQLAlchemy(app)

from web import serve