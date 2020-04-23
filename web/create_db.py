from sqlalchemy import create_engine, Column, Text, Integer, Date, Boolean, ForeignKey, String
from sqlalchemy import case, func, join, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker 
import datetime
from web import db

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    username = Column(Text, index = True)
    salt = Column(String, index = True)
    name = Column(Text, index = True)
    password = Column(Text, index = True)
    email = Column(Text, index = True) 
    
    def __repr__(self):
        return "<User(id={0}, username={1}, name ={2}, password={3}, email={4})".format(self.id, self.username, self.name, self.password, self.email)

class Book(db.Model):
    __tablename__ = 'books'
    id = Column(String, primary_key=True)
    title = Column(String, index = True)
    author_name = Column(String, index = True)
    owner = Column(Integer, ForeignKey('users.id'))
    # current_owner = Column(Integer, ForeignKey('users.id'))
    users = relationship('User')

    def __repr__(self):
        return "<Book(id={0}, title={1}, author_name={2}, language={3}, owner={4}, current_owner={5})".format(self.id, self.title, self.author_name, self.language, self.owner, self.current_owner)

class Letter(db.Model):
    __tablename__ = 'letters'
    id = Column(Integer, primary_key = True)
    book_id = Column(String, ForeignKey('books.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date, index=True)
    message = Column(Text, index = True)
    books = relationship('Book')
    users = relationship('User')

    def __repr__(self):
        return "<Letter(id={0}, book_id={1}, user_id={2}, date={3}, message={4})".format(self.id, self.book_id, self.user_id, self.date, self.message)

class Current_Owner(db.Model):
    __tablename__ = "current_owner"
    book_id = Column(String, ForeignKey('books.id'), primary_key=True)
    current_owner_id = Column(Integer, ForeignKey('users.id'))
    books = relationship('Book')
    users = relationship('User')
# Initialize database
db.create_all()
db.session.commit()

