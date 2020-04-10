from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

import web
from web import db, app
from .create_db import User, Book, Letter

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run()
