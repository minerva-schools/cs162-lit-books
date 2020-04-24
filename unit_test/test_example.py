import os
import tempfile
import unittest
import pytest
from flask_sqlalchemy import SQLAlchemy

from web import app, db
from web.create_db import User, Book, Letter, Current_Owner, BookTransactions

app.config['TESTING'] = True #DB mounted on memory for specific app instance
app.config['SECRET_KEY'] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'

@pytest.fixture
def client():
    db.drop_all()
    db.create_all()
    client = app.test_client()

    yield client

def test_simple(client):
    """Test empty db"""
    assert db.session.query(User).count() == 0
    assert db.session.query(Book).count() == 0
    assert db.session.query(Letter).count() == 0
    assert db.session.query(Current_Owner).count() == 0
    assert db.session.query(BookTransactions).count() == 0

def test_signup(client):
    # Create an account with username="CS162" password = "ProfStern"
    client.post('/register',
        data = dict(username = "CS162",
                    password = "ProfSterne",
                    email = "a@b.com",
                    name = "testname"),
        follow_redirects = True)
    user = db.session.query(User).filter(User.username == "CS162").first()
    print(user)
    assert("testname" == user.name)

if __name__ == '__main__':
    unittest.main()
