import os
import pytest
import tempfile
from web import app, db

@pytest.fixture
def client():
    """Create client for testing
    Statements before 'yield client' set-up client
    Statements after 'yield client' tear-down client"""
    client = app.test_client()

    yield client

def test_booksearch(client):
    """Check if booksearch endpoint renders"""
    rv = client.get('/booksearch')
    assert b"Don't have a Book ID?" in rv.data

def test_about(client):
    """Check if about.html renders"""
    rv = client.get('/about')
    assert b"About Paper Trail" in rv.data
    assert b"What's Paper Trail" in rv.data

def test_login(client):
    """Check login.html renders"""
    rv = client.get('/login')
    assert b"Login" in rv.data

def test_register(client):
    """Check /register endpoint"""
    rv = client.get('/register')
    assert b"Create an account" in rv.data

def test_bookpage(client):
    """Check book endpoint"""
    rv = client.get('/book/')
    assert b"I'm a new book receiver" in rv.data
    assert b"I've finished reading the book" in rv.data

if __name__ == '__main__':
    unittest.main()
