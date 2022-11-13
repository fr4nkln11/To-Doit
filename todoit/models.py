from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"[Task #{self.id}]"

    def __init__(self, content):
        self.content = content