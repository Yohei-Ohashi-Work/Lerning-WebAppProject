import random
from flask import Flask, render_template, request

app = Flask(__name__)

def janken_result(computer, user):
    '''
    ユーザー視点でじゃんけんの勝敗を判定する
    Args:
        computer (int): コンピューターの手
        user (int): ユーザーの手
    Returns:
        str: ユーザー視点での結果を出力
    '''
    
    if computer == user:
        return 'あいこ'
    elif (computer == 0 and user == 1) or (computer == 1 and user == 2) or (computer == 2 and user == 0):
        return '負け'
    else:
        return '勝ち'

@app.route("/")
def index():
    rps_pattern = {'グー': 0, 'チョキ': 1, 'パー': 2}
    res = {'computer': '', 'user': '', 'result': ''}

    # ユーザーが選択した手を取得
    if request.args.get('user', ''):
        res['user'] = rps_pattern[request.args.get('user')]
    
        # コンピューターの手をランダムに選択
        res['computer'] = random.randint(0, 2)

        # 勝敗を判定
        res['result'] = janken_result(res['computer'], res['user'])

    return render_template('index.html', res=res)