import csv, os
from datetime import datetime
from flask import Flask, render_template, request


app = Flask(__name__)

# プログラムファイルのディレクトリを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# ファイル名
DATA_FILE = os.path.join(BASE_DIR, "memo.csv")
# 1ページの件数
ROWS_NUM_PER_PAGE = 10

def debug_print(**kwargs:dict):
    '''
    デバッグ情報を表示する関数

    args:
        **kwargs: キーワード引数(名前付きの引数)
    '''
    # 引数がない場合は何もしない
    if not kwargs:
        return
    
    # キーワード引数の処理
    print('==== デバッグ情報 ====')
    for key, value in kwargs.items():
        print(f'{key}: {value}')
    print('======================')

def save_data(created_at:str, memo:str):
    '''
    メモを保存する関数

    Args:
        created_at: 作成日時
        memo: メモ
    '''
    with open(DATA_FILE, 'a', encoding='utf-8') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow([created_at, memo])

def load_data():
    '''記録データを返す関数'''
    with open(DATA_FILE, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=[
            'created_at',
            'memo'
        ])
        # メモデータをリストに格納する
        result = list(csv_reader)
    return result 

@app.route("/", methods=['GET', 'POST'])
def index():
    res = {}

    # デバッグ用に初期化
    memo = None
    writer = None

    # STEP1
    if request.method == 'POST':
        # inputフォームのメモを取得する
        memo = request.form.get('memo', '')
        # メモに値がある時だけ処理する
        if memo:
            # データを記録する
            created_at = f'{datetime.now():%Y-%m-%d}'
            save_data(created_at, memo)
        
    # 記録されているメモを取得する
    data = load_data()
    data = data[::-1] # 逆順にする

    # ページネーションの処理
    # ページ番号を取得
    page = int(request.args.get('page', 1))
    res['page'] = int(page)
    if page > 1:
        res['previous_page'] = page - 1
    if page * ROWS_NUM_PER_PAGE < len(data):
        res['next_page'] = page + 1
    
    # 開始行番号を取得
    start_row_num = (page - 1) * ROWS_NUM_PER_PAGE
    # ページ分のデータ取得
    res['list'] = data[start_row_num: (start_row_num + ROWS_NUM_PER_PAGE)]

    return render_template('index.html', res=res)
