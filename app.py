from flask import Flask, request, render_template_string, send_from_directory

app = Flask(__name__)

# 提供 Google 驗證檔案
@app.route('/google1de2d1d33522ed28.html')
def serve_verification_file():
    return send_from_directory('.', 'google1de2d1d33522ed28.html')

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        form_type = request.form.get("form_type", "")
        
        # 計算數學加權分數
        if form_type == "math":
            try:
                a = int(request.form.get("math_correct", 0))
                a_total = int(request.form.get("math_choice_total", 1))
                b = int(request.form.get("math_nonchoice", 0))
                b_total = int(request.form.get("math_nonchoice_total", 1))
            except ValueError:
                return "請輸入正確的數字！"

            choice_score = (a / a_total) * 85
            nonchoice_score = (b / b_total) * 15
            math_score = choice_score + nonchoice_score

            return render_template_string("""
                <h2>數學加權分數結果</h2>
                <p>數學加權分數 = {{ math_score }}</p>
                <a href="/">返回</a>
            """, math_score=round(math_score, 2))

        # 計算英文加權分數
        elif form_type == "english":
            try:
                c = int(request.form.get("eng_listen", 0))
                c_total = int(request.form.get("eng_listen_total", 1))
                d = int(request.form.get("eng_read", 0))
                d_total = int(request.form.get("eng_read_total", 1))
            except ValueError:
                return "請輸入正確的數字！"

            english_score = (c / c_total) * 20 + (d / d_total) * 80
            return render_template_string("""
                <h2>英文加權分數結果</h2>
                <p>英文加權分數 = {{ english_score }}</p>
                <a href="/">返回</a>
            """, english_score=round(english_score, 2))

    return """
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>國三生們加油! 一起來算算你的會考數學或英文加權分數吧~</title>
    <meta name="description" content="我是miumiu~ 這個網頁很讚喔~ 你們可以不用再按計算機還要再加起來(真的很麻煩)，模模考或是練習的題本用這個很方便，幫你省下時間，可以多訂正一題~">
    <style>
        body {
            font-family: "微軟正黑體", sans-serif;
            background-color: #f5f0ff;
            padding: 30px;
        }
        .container {
            display: flex;
            justify-content: center;
            gap: 50px;
            flex-wrap: wrap;
        }
        .card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
            width: 300px;
        }
        .card h3 {
            margin-top: 0;
        }
        input, button {
            width: 100%;
            padding: 8px;
            margin: 8px 0;
            border-radius: 4px;
            border: 1px solid #aaa;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        h2 {
            text-align: center;
        }
    </style>
</head>
<body>
    <h2>國中會考加權分數計算機</h2>
    <div class="container">
        <div class="card">
            <h3>計算數學成績</h3>
            <form method="post">
                <input type="hidden" name="form_type" value="math">
                數學選擇題對的題數：<input type="number" name="math_correct"><br>
                數學選擇題總題數：<input type="number" name="math_choice_total"><br>
                數學非選擇題得分：<input type="number" name="math_nonchoice"><br>
                數學非選擇題總分：<input type="number" name="math_nonchoice_total"><br><br>
                <button type="submit">計算數學分數</button>
            </form>
        </div>

        <div class="card">
            <h3>計算英文成績</h3>
            <form method="post">
                <input type="hidden" name="form_type" value="english">
                英文聽力對的題數：<input type="number" name="eng_listen"><br>
                英文聽力總題數：<input type="number" name="eng_listen_total"><br>
                英文閱讀對的題數：<input type="number" name="eng_read"><br>
                英文閱讀總題數：<input type="number" name="eng_read_total"><br><br>
                <button type="submit">計算英文分數</button>
            </form>
        </div>
    </div>
</body>
</html>
    """

if __name__ == "__main__":
    app.run(debug=True)
