import sqlite3
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# データベースファイルのパス
sqlite_path = os.path.join(os.path.dirname(__file__), 'db/todo.db')

def debug_print(**kwargs):
    print(f'---------- 【デバッグ】 ----------')
    for k, v in kwargs.items():
        print(f'{k}: {v}')
    print(f'----------------------------------')


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

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'GET':
        todo = {}
        
        return render_template('edit.html', todo=todo)
    else:
        # バリデーション
        error = []
        if not request.form['name']:
            error.append('タスク名を入力して下さい')
        if not request.form['duedate']:
            error.append('期日を入力して下さい')
        
        if error:
            # ユーザーが入力したデータを保持するため
            todo = request.form.to_dict()
            return render_template('edit.html', todo=todo, error_list=error)
        
        # データベースに接続
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO todo (name, duedate, memo) VALUES (?, ?, ?)',(
                request.form['name'],
                request.form['duedate'],
                request.form['memo']
            ))
            conn.commit()
            
        finally:
            conn.close()
        
        return redirect(url_for('index'))
