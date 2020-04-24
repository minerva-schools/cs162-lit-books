import os
import tempfile
import unittest
import pytest
from flask_sqlalchemy import SQLAlchemy

from web import app, db
from web.create_db import User, Book, Letter, Current_Owner

app.config['TESTING'] = True #DB mounted on memory for specific app instance

@pytest.fixture
def client():
    db.drop_all()
    db.create_all()
    client = app.test_client()

    yield client

def test_simple(client):
    """Test empty db"""
    assert db.session.query(Book).count() == 0

if __name__ == '__main__':
    unittest.main()
