import sqlite3
import os

from flask import Flask, render_template
app = Flask(__name__)

# データベースファイルのパス
sqlite_path = os.path.join(os.path.dirname(__file__), 'db/todo.db')


def get_db_connection():
    connection = sqlite3.connect(sqlite_path)
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def index():
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        res = cursor.execute('SELECT * FROM todo')
        return render_template('index.html', todo_list=res.fetchall())
    finally:
        conn.close()
    
@app.route('/show/<int:id>')
def show(id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        res = cursor.execute('SELECT * FROM todo WHERE id = ?', (id,))
        return render_template('detail.html', todo=res.fetchone())
    finally:
        conn.close()