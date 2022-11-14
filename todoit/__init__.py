from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

from .models import db
db.init_app(app)
migrate = Migrate(app, db)

from . import routes
