import random
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    rps_pattern = {'グー': 0, 'チョキ': 1, 'パー': 2}
    res = {'computer': '', 'user': '', 'result': ''}


    return render_template('index.html', res=res)