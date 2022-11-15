from flask import Flask, render_template, request, redirect, url_for, Blueprint
from .models import db, tasks
import os

todo_app = Blueprint("todo_app", __name__)

basedir = os.path.abspath(os.path.dirname(__file__))

@todo_app.route("/", methods=["GET", "POST"])
def index():
    todos = tasks.query.all()
    todos = reversed(todos)
    return render_template("index.html", todos=todos)


@todo_app.route("/create", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        new_task = request.get_json()["new_task"]

        if new_task:
            task = tasks(new_task)
            db.session.add(task)
            db.session.commit()
            db.session.refresh(task)
            task_id = str(task.id)
            print(f"task #{task_id} created: {new_task}")
            return task_id
        else:
            return "empty string"

    elif request.method == "GET":
        with open(os.path.join(basedir, "templates/card_content.html")) as html:
            text = html.read()
            return text


@todo_app.route("/delete", methods=["POST"])
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