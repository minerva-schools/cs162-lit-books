import os
import pytest
import tempfile
from web import app, db

@pytest.fixture
def client():
    client = app.test_client()

    yield client

def test_index(client):
    """Check if index.html renders"""
    rv = client.get('/')
    assert b"Don't have a Book ID?" in rv.data

if __name__ == '__main__':
    unittest.main()
