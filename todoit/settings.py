import os

FLASK_APP = os.environ["FLASK_APP"]
FLASK_DEBUG = os.environ["FLASK_DEBUG"]
SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URI"]
SECRET_KEY = os.environ["SECRET_KEY"]
SQLALCHEMY_ECHO = False
