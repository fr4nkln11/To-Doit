import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

class tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"[Task #{self.id}]"

    def __init__(self, content):
        self.content = content


@app.route("/", methods=["GET", "POST"])
def index():
    todos = tasks.query.all()
    todos = reversed(todos)
    return render_template("index.html", todos=todos)


@app.route("/create", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        new_task = request.get_json()["new_task"]

        if new_task:
            task = tasks(new_task)
            db.session.add(task)
            db.session.commit()
            db.session.refresh(task)
            task_id = str(task.id)
            print(f"task #{task_id} created")
            return task_id
        else:
            return "empty string"

    elif request.method == "GET":
        with open("templates/card_content.html") as html:
            text = html.read()
            return text


@app.route("/delete", methods=["POST"])
def delete():
    if request.method == "POST":
        task_id = request.get_json()["task_id"]
        if task_id:
            task = tasks.query.get(task_id)
            db.session.delete(task)
            db.session.commit()
            print(f"task #{task_id} deleted")
            return "Task deleted successfully"
        else:
            return "Error"


if __name__ == "__main__":
    app.run()
