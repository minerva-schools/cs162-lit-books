from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, desc
from datetime import datetime
import os
import random
import json, itsdangerous
from functools import wraps

from web import db,app
from .create_db import User, Book, Letter, Current_Owner, BookTransactions
import hashlib


#####################################################
# Initiate Flask app
# app = Flask(__name__)

# Create local SQL Lite database.db file in directory
# db_path = os.path.join(os.path.dirname(__file__), 'database.db')
# URI = 'sqlite:///{}'.format(db_path)
# URI = 'sqlite:///:memory:'
# app.config['SQLALCHEMY_DATABASE_URI'] = URI
# To use environment variable as URI - for final submission
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instantiate SQLAlchemy
# db = SQLAlchemy(app)

# db.create_all() #create all tables
#####################################################

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = session.get('username')
        try:
            _session = request.cookies["session"].partition('.')[0]
        except KeyError:
            session_username = None
        else:
            session_username = json.loads(itsdangerous.base64_decode(_session).decode('utf-8')).get('username')

        print(username, session_username)
        if username is None or session_username is None or username != session_username: #is checks for identity, since None is a singleton
            flash ('Please log in to use')
            return redirect(url_for('login'))

        return func(*args, **kwargs)
    return wrapper


# Page to look up book by ID
@app.route('/booksearch')
def booksearch():
    return render_template('index.html')

# Index page
@app.route('/')
def index():
    # Redirect to booksearch if logged-in
    return redirect(url_for('booksearch'))

# sample page (book page with sample letters)
@app.route('/sample')
def sample():
    return render_template('sample.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

#logout
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    session.clear()
    flash('You were logged out')
    return redirect(url_for('login'))

# Log-in page
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        user = db.session.query(User).filter(User.username == username).first()
        if user:
            salt = user.salt
            if user.password == hash_password(str(password+salt)):
                session['username'] = user.username
                flash('Login sucessfully')
                return redirect(url_for('user_byusername', username=username))
            else:
                flash('Wrong password')
                return redirect(url_for('login'))
        else:
            flash('Username does not exist')
            return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template('login.html')

#create random salt
def create_salt():
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars = []
    for i in range (16):
        chars.append(random.choice(ALPHABET))
    return "".join(chars)

#hash password
def hash_password(users_password):
    # input: user password
    # then encode to convert into bytes
    return hashlib.sha256(users_password.encode('utf-8')).hexdigest()

# Register page
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        name = request.form['name']

        user = db.session.query(User).filter(User.username == username).first()

        if user != None:
            flash('Taken username!')
            return render_template('register.html')
        else:
            salt = create_salt()
            new_user = User(username = username, name=name, password = hash_password(str(password+salt)), email = email, salt=salt)

            db.session.add(new_user)
            db.session.commit()
            flash('Registered sucessfully. Log in to use')
            return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template('register.html')

#################
#book ID generator
def create_one_bookID():
    number = "0123456789"
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars = []
    for i in range (2):
        chars.append(random.choice(ALPHABET))
    for i in range (3):
        chars.append(random.choice(number))
    return "".join(chars)
def valid_book_id():
    while True:
        book_id = create_one_bookID()
        book = db.session.query(Book).filter(Book.id == book_id).first()
        if book != None:
            continue
        else:
            return book_id
###############
# Add a new book

@app.route('/add', methods=["POST","GET"])
@login_required
def add_book():
    username = session.get('username')
    user = db.session.query(User).filter(User.username == username).first()
    title = request.form['title']
    author = request.form['author']
    book_id = valid_book_id()

    new_book = Book(title=title, author_name=author, id=book_id, owner=user.id)
    db.session.add(new_book)
    db.session.add(Current_Owner(book_id=book_id,current_owner_id=user.id,orig_owner=1))
    db.session.commit()
    return redirect(url_for('book', bookid = book_id))

#add existed book
@app.route('/add_existed_book/<bookid>', methods=['POST',"GET"])
def add_existed_book(bookid):
    username = session.get('username')

    if username == None:
        flash ('Please log in to use')
        return redirect(url_for('login'))

    user = db.session.query(User).filter(User.username == username).first()
    date = datetime.utcnow()
    month = datetime.utcnow().month

    db.session.add(Current_Owner(book_id=bookid,current_owner_id=user.id,orig_owner=0))
    db.session.add(BookTransactions(date=date, month=month, book_id=bookid,to_user_id=user.id))
    db.session.commit()
    return redirect(url_for('book', bookid=bookid))

#add a new letter
@app.route('/add_letter/<bookid>', methods=['POST'])
def add_letter(bookid):
    username = session.get('username')

    if username == None:
        flash ('Please log in to use')
        return redirect(url_for('login'))

    user = db.session.query(User).filter(User.username == username).first()
    message = request.form['msg']
    date = datetime.utcnow()

    new_letter = Letter(user_id = user.id, book_id=bookid, date=date, message=message)
    db.session.add(new_letter)
    db.session.commit()
    return redirect(url_for('book', bookid=bookid))

#show letter form
@app.route('/letter/<bookid>')
def letter(bookid): 
    return render_template('letter.html', bookid=bookid)

# Book listing
@app.route('/book/id/<bookid>')
@login_required
def book(bookid):
    book = db.session.query(Book).filter(Book.id==bookid).first()
    book_owner = db.session.query(User).filter(User.id==Book.owner).first()
    letters = db.session.query(Letter,User.name).join(Letter.users
                                ).filter(Letter.book_id==bookid
                                ).order_by(desc(Letter.date)
                                ).all()
    return render_template('book_page.html', book = book, book_owner=book_owner,letters=letters, bookid=bookid)

# User profile by username
@app.route('/user/<username>')
@login_required
def user_byusername(username):
    if username == None:
        return render_template('login.html')
    user = db.session.query(User).filter(User.username == username).first()
    user_id = user.id
    nowned = db.session.query(Book
                        ).filter(Book.owner == user.id
                        ).count()
    nreceived = db.session.query(Current_Owner
                        ).filter(Current_Owner.current_owner_id == user.id
                        ).filter(Current_Owner.orig_owner == 0
                        ).count()
    owned_books = db.session.query(Book
                        ).filter(Book.owner == user.id
                        ).all()
    received_books = db.session.query(Book.id, Book.title, Book.author_name
                        ).join(Current_Owner.books
                        ).filter(Current_Owner.current_owner_id == user.id
                        ).filter(Current_Owner.orig_owner == 0
                        ).all()
    return render_template('users.html', user=user, nowned=nowned, nreceived=nreceived, owned_books=owned_books, received_books=received_books)

# User profile by id
@app.route('/user/id/<int:userid>')
def user_byid(userid):
    return render_template('users.html')


if __name__ == '__main__':
    app.run()
