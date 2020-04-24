# Welcome to Paper Trail - CS162 Final Project

### About
Paper trail is a book sharing and tracking service. We challenge you to explore the degrees of connection through a book.

### What is the challenge like?
Share a book with your friend through Paper Trail.
Challenge your friend to read and share the book to one of their connections. Repeat the process and Paper Trail will help you to track your book and collect thoughts along the way! Check out our sample book page 👇

##Instructions to follow:

## Run Virtual Environment

Virtual environment is a key component in ensuring that the application is configured in the right environment

##### Requirements
* Python 3
* Pip 3

```bash
$ brew install python3
```

Pip3 is installed with Python3

##### Installation
To install virtualenv via pip run:
```bash
$ pip3 install virtualenv
```

##### Usage
Creation of virtualenv:

    $ virtualenv -p python3 venv

If the above code does not work, you could also do

    $ python3 -m venv venv

To activate the virtualenv:

    $ source venv/bin/activate

Or, if you are **using Windows** - [reference source:](https://stackoverflow.com/questions/8921188/issue-with-virtualenv-cannot-activate)

    $ venv\Scripts\activate

To deactivate the virtualenv (after you finished working):

    $ deactivate

Install dependencies in virtual environment:

    $ pip3 install -r requirements.txt

## Environment Variables

All environment variables are stored within the `.env` file and loaded with dotenv package.

**Never** commit your local settings to the Github repository!

## Run Application

Start the server by running:

    $ export FLASK_ENV=development
    $ export FLASK_APP=web
    $ python3 -m flask run

For windows, use:
    $ set FLASK_ENV=development
    $ set FLASK_APP=web
    $ python3 -m flask run


## Unit Tests
To run the unit tests use the following commands:

    $ python3 -m venv venv_unit
    $ source venv_unit/bin/activate
    $ pip install -r requirements-unit.txt
    $ export DATABASE_URL='sqlite:///web.db'
    $ pytest unit_test

For windows, use:

    $ python3 -m venv venv_unit
    $ venv_unit\Scripts\activate
    $ pip install -r requirements-unit.txt
    $ set DATABASE_URL='sqlite:///web.db'
    $ pytest unit_test


## Integration Tests
Start by running the web server in a separate terminal.

Now run the integration tests using the following commands:

    $ python3 -m venv venv_integration
    $ source venv_integration/bin/actvate
    $ pip3 install -r requirements-integration.txt
    $ pytest integration_test

For windows, use:

    $ python3 -m venv venv_integration
    $ venv_integration\Scripts\activate
    $ pip3 install -r requirements-integration.txt
    $ pytest integration_test
