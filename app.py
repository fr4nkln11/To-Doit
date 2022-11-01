import sqlite3
from datetime import datetime
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
    return render_template('index.html',todos=todos, datetime=datetime)

@app.route('/create', methods=['POST'])   
def create():
    conn = get_db_connection()
    if request.method == "POST":
       new_entry = request.form["new_entry"]
       
       if new_entry:
           conn.execute('INSERT INTO todos (content) VALUES (?)',(new_entry,))
           conn.commit()
           conn.close()
           return redirect(url_for('index'))
       return redirect(url_for('index'))

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    if request.method == 'POST':
        conn.execute("DELETE FROM todos WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return "Task deleted successfully"

if __name__ == "__main__":
    app.run(debug=True)
