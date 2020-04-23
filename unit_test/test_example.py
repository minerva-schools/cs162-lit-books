<<<<<<< HEAD
import os
import tempfile
import unittest
import pytest

from web import app, db
import app


class BasicTests(unittest.TestCase):

    # executed prior to each test
    #creates a new test client and initializes a new databade
    def setUp(self):
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + TEST_DB
        self.app = app.test_client()
        db.drop_all()
        db.create_all()




    # executed after each test
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # user authentication methods
=======
# Example taken from:
# http://flask.pocoo.org/docs/1.0/testing/
# and suitably modified.
# import os
# import tempfile

# import pytest

# from web import app, db
>>>>>>> 6d8ab052334af0c9fe41743d6196eb1be2609130

    def signup(self, username, password, email, confirm):
        return self.app.post(
            '/signup',
            data=dict(username=username, password=password, email=email, confirm=confirm),
            follow_redirects=True
        )

<<<<<<< HEAD
    def login(self, username, password):
        return self.app.post(
            '/login',
            data=dict(username=username, password=password),
            follow_redirects=True
        )

    def logout(self):
        return self.app.get(
            '/logout',
            follow_redirects=True
        )

    #basic tests
    # Standard Route tests
    def test_valid_user_signup(self):
        response = self.signup('test', 'test1', 'test@test.com')
        self.assertEqual(response.status_code, 200)
=======
# @pytest.fixture
# def client():
#     db_fd, app.config['DATABASE'] = tempfile.mkstemp()
#     app.config['TESTING'] = True
#     client = app.test_client()

#     yield client

#     os.close(db_fd)
#     os.unlink(app.config['DATABASE'])
>>>>>>> 6d8ab052334af0c9fe41743d6196eb1be2609130

    def test_valid_user_login(self):
        response = self.login('test@test.com', 'test1')
        self.assertEqual(response.status_code, 200)

<<<<<<< HEAD
    def test_valid_user_logout(self):
        response = self.logout()
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
=======
# def test_empty_db(client):
#     """Start with a blank database."""

#     rv = client.get('/')
#     assert b'Hello World!' in rv.data

# def login(client, username, password):
#     return client.post('/login', data=dict(
#     username="sho",
#     password="password"
#     ), follow_redirects=True)

# def logout(client):
#     return client.get('/logout', follow_redirects=True)
        
# if __name__ == '__main__':
#     unittest.main()
>>>>>>> 6d8ab052334af0c9fe41743d6196eb1be2609130
