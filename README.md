# Welcome to Paper Trail - CS162 Final Project

### About
Paper trail is a book sharing and tracking service. We challenge you to explore the degrees of connection through a book.

### What is the challenge like?
Share a book with your friend through Paper Trail.
Challenge your friend to read and share the book to one of their connections. Repeat the process and Paper Trail will help you to track your book and collect thoughts along the way! Check out our sample book page 👇

## Run Virtual Environment

##### Installation
To install virtualenv via pip run:
```bash
$ pip3 install virtualenv
```

##### Requirements
* Python 3
* Pip 3

```bash
$ brew install python3
```

Pip3 is installed with Python3


To deactivate the virtualenv (after you finished working):

    $ deactivate

Install dependencies:

    $ pip3 install -r requirements.txt

## Environment Variables

All environment variables are stored within the `.env` file.



## Running the application
Once you installed everything necessary, go to the root directory of the project and start the server by running:

Start the server by running:

    $ export FLASK_ENV=development
    $ export FLASK_APP=web
    $ python3 -m flask run


## Testing
To run the unit tests, be sure to run the following command and the project directory:
```bash
$ cd unit_test
$ python3 -m unittest discover tests
```
