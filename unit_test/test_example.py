<<<<<<< Updated upstream
<<<<<<< HEAD
<<<<<<< HEAD
=======
# Example taken from:
# http://flask.pocoo.org/docs/1.0/testing/
# and suitably modified.

>>>>>>> Stashed changes
import os
import tempfile
import unittest
import pytest
<<<<<<< Updated upstream

from web import app, db
=======
import web
from web import app, db
from web import serve

>>>>>>> Stashed changes
import app


class BasicTests(unittest.TestCase):

    # executed prior to each test
    #creates a new test client and initializes a new databade
    def setUp(self):
<<<<<<< Updated upstream
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + TEST_DB
        self.app = app.test_client()
=======
        # Creates a new test client and initializes a new database
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.testing = True
        self.app = app.app.test_client()
>>>>>>> Stashed changes
        db.drop_all()
        db.create_all()




    # executed after each test
    def tearDown(self):
<<<<<<< Updated upstream
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
=======
        # Closes the test database
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])

    # user authentication methods

    # sign up testing
    def test_signup(self):
        # Create an account with username="CS162" password = "ProfStern"
        self.app.post('/signup',
                      data = dict(username = "CS162",
                                  password = "ProfSterne"),
                      follow_redirects = True)

        User = db.session.query(Users).filter(Users.username == "CS162").first()
        self.assertTrue("ProfSterne" == User.password)

    # log in testing
    def test_login(self):
        # Create an account with username="CS162" password = "ProfStern"
        self.app.post('/signup',
                      data = dict(username = "CS162",
                                  password = "ProfSterne"),
                                  follow_redirects = True)

        # Get User's data through the username
        User = db.session.query(Users).filter(Users.username=='CS162').first()

        # Log in
        result = self.app.post('/login', data=dict(
            username="CS162",
            password= "ProfSterne"), follow_redirects=True)

        # Check the flash response
        assert b"Login sucessfully" in result.data

    # log out test
    def test_logout(self):
        # Create an account with username="CS162" password = "ProfStern"
        self.app.post('/signup',
                      data = dict(username = "CS162",
                                  password = "ProfSterne"),
                      follow_redirects = True)

        # Get User's data through the username
        User = db.session.query(Users).filter(Users.username=='CS162').first()

        # Log in
        self.app.post('/login', data=dict(username="CS162",
                                    password= "ProfSterne"),
                                  follow_redirects=True)

        # Try logging out
        result = self.app.get('/logout',
                      follow_redirects=True)
        assert b"You were logged out" in result.data

>>>>>>> Stashed changes



if __name__ == '__main__':
    unittest.main()
<<<<<<< Updated upstream
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
=======
>>>>>>> 9eb28bd5eb3c9a127dc4016dafa8d5f1bebe175e
=======
>>>>>>> Stashed changes
