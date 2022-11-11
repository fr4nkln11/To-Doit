import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = "secret stuff"

db = SQLAlchemy(app)

class tasks(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"[Task #{self.id}]"
    def __init__(self, content):
        self.content = content

@app.route('/', methods =["GET", "POST"])
def index():
    todos = tasks.query.all()
    todos = reversed(todos)
    return render_template('index.html',todos=todos)

@app.route('/create', methods=['POST'])   
def create():
    if request.method == "POST":
       print("incoming POST...")
       new_task = request.get_json()["new_task"]
       
       if new_task:
           db.session.add(tasks(new_task))
           db.session.commit()
           task = tasks.query.filter_by(content=new_task).first()
           task_id = str(task.id)
       print(f"task #{task_id} created")
       return task_id

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        _id = request.get_json()['task_id']
        task = tasks.query.filter_by(id=_id).first()
        db.session.delete(task)
        db.session.commit()
        print(f"task #{_id} deleted")
        return "Task deleted successfully"

if __name__ == "__main__":
    app.run()
