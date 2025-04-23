import sqlite3
import os
from textwrap import dedent

# データベースファイルのパス
DB_PATH = os.path.join(os.path.dirname(__file__), 'db/todo.db')

def check_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # テーブル一覧を表示
    table_query = dedent("""
        SELECT name 
        FROM sqlite_master 
        WHERE type='table'
    """).strip()
    c.execute(table_query)
    tables = c.fetchall()
    print("テーブル一覧:")
    for table in tables:
        print(f"- {table[0]}")
    print()

    # todoテーブルの内容を表示
    print("todoテーブルの内容:")
    todo_query = dedent("""
        SELECT * 
        FROM todo
    """).strip()
    c.execute(todo_query)
    rows = c.fetchall()
    for row in rows:
        print(f"ID: {row[0]}")
        print(f"名前: {row[1]}")
        print(f"期限: {row[2]}")
        print(f"状態: {row[3]}")
        print(f"メモ: {row[4]}")
        print("-" * 30)

    conn.close()

if __name__ == '__main__':
    check_db() 