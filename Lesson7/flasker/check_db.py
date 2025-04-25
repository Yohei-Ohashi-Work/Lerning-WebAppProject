import sqlite3
import os
from textwrap import dedent

# データベースファイルのパス
DB_PATH = os.path.join(os.path.dirname(__file__), 'db/todo.db')

def check_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # テーブル一覧を表示
    table_query = dedent('''
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
    ''')
    c.execute(table_query)
    tables = c.fetchall()
    print('テーブル一覧：')
    print('-' * 40)
    for table in tables:
        print(f'- {table}')
    print('-' * 40)
    print()
    
    # todoテーブルの内容を表示
    todo_query = dedent('''
        SELECT *
        FROM todo
    ''')
    c.execute(todo_query)
    rows = c.fetchall()
    print('todoテーブルの内容：')
    print('-' * 40)
    for row in rows:
        print(f'ID: {row[0]}')
        print(f'タイトル: {row[1]}')
        print(f'期限: {row[2]}')
        print(f'ステータス: {row[3]}')
        print(f'メモ: {row[4]}')
        print('-' * 40)
    
    # 接続を閉じる
    conn.close()
    
if __name__ == '__main__':
    check_db()