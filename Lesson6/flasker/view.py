import sqlite3

from flask import Flask, render_template
app = Flask(__name__)

sqlite_path = 'db/todo.db'


def get_db_connection():
    connection = sqlite3.connect(sqlite_path)
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def index():
    return render_template('index.html')