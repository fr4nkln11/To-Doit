from flask import Flask
from flask_migrate import Migrate

def create_app(env):
    if env == "Development":
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_pyfile('config.py')
    elif env == "Production":
        app = Flask(__name__)
        app.config.from_pyfile('settings.py')
        
    from .models import db
    db.init_app(app)
    migrate = Migrate(app, db)
        
    from .routes import todo_app
    app.register_blueprint(todo_app)
        
    return app
