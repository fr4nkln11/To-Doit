from flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    
    from .models import db
    db.init_app(app)
    migrate = Migrate(app, db)
    
    from .routes import todo_app
    app.register_blueprint(todo_app)
    
    return app
