from sqlalchemy import create_engine, Column, Text, Integer, Date, Boolean, ForeignKey, String
from sqlalchemy import case, func, join, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import datetime
from web import db

class User(db.Model):
    """Table of users"""
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
    """Table of books"""
    __tablename__ = 'books'
    id = Column(String, primary_key=True)
    title = Column(String)
    author_name = Column(String)
    owner = Column(Integer, ForeignKey('users.id'), index = True) #indexed for quick lookup of books a specific user owns
    users = relationship('User')

    def __repr__(self):
        return "<Book(id={0}, title={1}, author_name={2}, language={3}, owner={4}, current_owner={5})".format(self.id, self.title, self.author_name, self.language, self.owner, self.current_owner)

class Letter(db.Model):
    """Table of letters"""
    __tablename__ = 'letters'
    id = Column(Integer, primary_key = True)
    book_id = Column(String, ForeignKey('books.id'), index = True) #indexed for quick lookup of letters for a specific book
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date)
    message = Column(Text)
    books = relationship('Book')
    users = relationship('User')

    def __repr__(self):
        return "<Letter(id={0}, book_id={1}, user_id={2}, date={3}, message={4})".format(self.id, self.book_id, self.user_id, self.date, self.message)

class BookTransactions(db.Model):
    """Table containing all book transactions (transfer of ownership between
    users)"""
    __tablename__="book_transactions"
    id = Column(Integer, primary_key = True)
    date = Column(Date)
    month = Column(Integer)
    book_id = Column(String, ForeignKey('books.id'))
    from_user_id = Column(Integer, ForeignKey('users.id'))
    to_user_id = Column(Integer, ForeignKey('users.id'), index=True) #indexed for quick lookup of all books an owner holds
    books = relationship('Book')
    users = relationship('Users')

# Initialize database
db.create_all()
db.session.commit()
