import os

FLASK_APP = os.environ["FLASK_APP"]
FLASK_ENV = os.environ["FLASK_ENV"]
SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URI"]
SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = False
SQLALCHEMY_ECHO = False