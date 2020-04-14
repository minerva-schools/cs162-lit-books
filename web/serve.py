from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
#from create_db import User, Book, Letter

# Initiate Flask app
app = Flask(__name__)

# Create local SQL Lite database.db file in directory
# db_path = os.path.join(os.path.dirname(__file__), 'database.db')
# URI = 'sqlite:///{}'.format(db_path)
URI = 'sqlite:///:memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = URI
# To use environment variable as URI - for final submission
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instantiate SQLAlchemy
db = SQLAlchemy(app)

db.create_all() #create all tables

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
