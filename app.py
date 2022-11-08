import sqlite3
from flask import Flask, render_template, request, redirect, url_for

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret stuff"

@app.route('/', methods =["GET", "POST"])
def index():
    conn = get_db_connection()
    todos = conn.execute('SELECT * FROM todos').fetchall()
    todos = reversed(todos)
    conn.close()
    return render_template('index.html',todos=todos)

@app.route('/create', methods=['POST'])   
def create():
    conn = get_db_connection()
    if request.method == "POST":
       print("incoming POST...")
       new_task = request.get_json()["new_task"]
       
       if new_task:
           conn.execute('INSERT INTO todos (content) VALUES (?)',(new_task,))
           conn.commit()
           task = conn.execute('SELECT * FROM todos WHERE content = ?',(new_task,)).fetchone()
           task_id = str(task['id'])
           conn.close()
       print(f"task #{task_id} created")
       return task_id

@app.route('/delete', methods=['POST'])
def delete():
    conn = get_db_connection()
    if request.method == 'POST':
        id = request.get_json()['task_id']
        conn.execute("DELETE FROM todos WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        print(f"task #{id} deleted")
        return "Task deleted successfully"

if __name__ == "__main__":
    app.run()
