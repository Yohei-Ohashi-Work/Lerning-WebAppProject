# 1: 大吉、2: 吉、3: 中吉、4: 小吉、5: 凶、6:大凶
import random
from flask import Flask, render_template, request

app = Flask(__name__)

GOOD_FILE = 'input/fortune_good.txt'
BAD_FILE = 'input/fortune_bad.txt'


@app.route("/")
def index():
    fortune = {}
    return render_template('index.html', fortune=fortune)