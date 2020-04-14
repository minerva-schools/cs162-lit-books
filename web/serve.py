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

# Page to look up book by ID
@app.route('/booksearch')
def booksearch():
    return render_template('index.html')

# Index page
@app.route('/')
def index():
    # Redirect to booksearch if logged-in
    return redirect(url_for('booksearch'))

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Log-in page
@app.route('/login')
def login():
    return render_template('login.html')

# Register page
@app.route('/register')
def register():
    return render_template('register.html')

# Book listing
@app.route('/book/id/<int:bookid>')
def book(bookid):
    return render_template('book_page.html')

# User profile
@app.route('/user/<username>')
def user_byusername(username):
    return render_template('users.html')

if __name__ == '__main__':
    app.run()
