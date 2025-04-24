import sqlite3
import os

# データベースファイルのパス
DB_PATH = os.path.join(os.path.dirname(__file__), 'db/todo.db')

# データベース接続
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # テーブル作成
    c.execute('''
        CREATE TABLE IF NOT EXISTS todo (
            id INTEGER PRIMARY KEY,
            name TEXT,
            duedate TEXT,
            status TEXT,
            memo TEXT            
        )
    ''')
    
    # 初期データの挿入
    initial_data = [
        (1, 'メールを書く', '2017-10-10', '未完了', '佐藤様に次回の打ち合わせの件を連絡'),
        (2, '資料作成', '2017-10-20', '未完了', ''),
        (3, 'バグを修正', '2017-10-30', '未完了', '仕様の解釈ミスでした')
    ]

    c.executemany('INSERT OR IGNORE INTO todo VALUES(?, ?, ?, ?, ?)', initial_data)
    
    # 変更を保存
    conn.commit()
    
    # 接続を閉じる
    conn.close()

if __name__ == '__main__':
    init_db()
    print(f"データベースを作成しました: {DB_PATH}")