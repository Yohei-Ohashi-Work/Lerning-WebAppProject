# 1: 大吉、2: 吉、3: 中吉、4: 小吉、5: 凶、6:大凶
import os
import random
from flask import Flask, render_template, request

app = Flask(__name__)

# プログラムファイルのディレクトリを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

GOOD_FILE = os.path.join(BASE_DIR, 'input/fortune_good.txt')
BAD_FILE = os.path.join(BASE_DIR, 'input/fortune_bad.txt')

@app.route("/")
def index():
    fortune = {}
    if request.args.get('fortune', ''):
        fortune['no'] = random.randint(1, 6)
        
        if fortune['no'] <= 4:
            # 1~4の場合はGood
            fortune_file = GOOD_FILE
        else:
            # 5~6の場合はBad
            fortune_file = BAD_FILE
        with open(fortune_file, 'r', encoding='utf-8') as f:
            messages = f.readlines()
        fortune['message'] = random.choice(messages).rstrip()
    return render_template('index.html', fortune=fortune)