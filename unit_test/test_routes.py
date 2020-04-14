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

def test_index(client):
    """Check if index.html renders"""
    rv = client.get('/')
    assert b"Don't have a Book ID?" in rv.data

def test_about(client):
    """Check if about.html renders"""
    rv = client.get('/about')
    assert b"About Paper Trail" in rv.data
    assert b"What's Paper Trail" in rv.data

def test_login(client):
    """Check login.html renders"""
    rv = client.get('/login')
    assert b."Login" in rv.data

if __name__ == '__main__':
    unittest.main()
