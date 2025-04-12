import random
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    dice = 0
    if request.args.get('dice', ''):
        dice = random.randint(1, 6)
    return render_template('index.html', dice=dice)