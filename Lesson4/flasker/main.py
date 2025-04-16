from flask import Flask, render_template, request

app = Flask(__name__)

def validate_input(name, val):
    error_msg = ''
    if not val:
        error_msg = f"{name}を入力してください。"
    elif not val.isdigit():
        error_msg = f"{name}は整数を入力してください。"
    return error_msg
        

def calc_bmi(height, weight):
    bmi = float(weight) / (float(height) / 100) ** 2
    return round(bmi, 2)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        res = {}
        res["height"] = request.form.get("height", "")
        res["weight"] = request.form.get("weight", "")
        
        # 入力チェックが必要そう
        res["error_height"] = validate_input("身長", res["height"])
        res["error_weight"] = validate_input("体重", res["weight"])
        
        # 入力チェックがOKなら計算
        if not res["error_height"] and not res["error_weight"]:
            res["calc"] = calc_bmi(res["height"], res["weight"])
            
        return render_template('index.html', res=res)
    else:
        return render_template('index.html')
