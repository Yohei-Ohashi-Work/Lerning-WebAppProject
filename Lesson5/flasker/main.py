from flask import Flask, render_template, request

app = Flask(__name__)

# ファイル名
DATA_FILE = "memo.csv"
# 1ページの件数
ROWS_NUM_PER_PAGE = 10


@app.route("/", methods=['GET', 'POST'])
def index():
    res = {}

    return render_template('index.html', res=res)