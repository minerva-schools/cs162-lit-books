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
        self.db_fd, web.app.config['DATABASE'] = tempfile.mkstemp()
        app.testing = True
        self.app = web.app.test_client()
        db.drop_all()
        db.create_all()



    # executed after each test
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(web.app.config['DATABASE'])

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




if __name__ == '__main__':
    unittest.main()
