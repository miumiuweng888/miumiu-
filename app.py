from flask import Flask, request, render_template_string, send_from_directory

app = Flask(__name__)

# 👇 這個路由讓 Google Search Console 能讀到驗證檔案
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
                math_correct = int(request.form["math_correct"])
                math_nonchoice = int(request.form["math_nonchoice"])
            except ValueError:
                return "請輸入正確的數字！"

            math_score = math_correct * (85 / 25) + math_nonchoice * (15 / 6)
            return render_template_string("""
                <h2>數學加權分數計算結果</h2>
                <p>數學加權分數: {{ math_score }}</p>
                <a href="/">返回</a>
            """, math_score=round(math_score, 2))
        
        # 計算英文加權分數
        elif form_type == "english":
            try:
                eng_listen = int(request.form["eng_listen"])
                eng_read = int(request.form["eng_read"])
            except ValueError:
                return "請輸入正確的數字！"

            listen_total = 21
            read_total = 43
            english_score = (eng_listen / listen_total) * 20 + (eng_read / read_total) * 80
            return render_template_string("""
                <h2>英文加權分數計算結果</h2>
                <p>英文加權分數: {{ english_score }}</p>
                <a href="/">返回</a>
            """, english_score=round(english_score, 2))

    return """
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>國中會考加權分數計算機</title>
    <meta name="keywords" content="國中會考, 會考分數計算, 國中英文成績, 國中數學成績, 線上會考工具, 加權分數計算">
    <style>
        body {
            font-family: "微軟正黑體", sans-serif;
            background-color: #f5f0ff;  /* 淺紫色 */
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
                數學非選擇題得分：<input type="number" name="math_nonchoice"><br><br>
                <button type="submit">計算數學分數</button>
            </form>
        </div>

        <div class="card">
            <h3>計算英文成績</h3>
            <form method="post">
                <input type="hidden" name="form_type" value="english">
                英文聽力對的題數：<input type="number" name="eng_listen"><br>
                英文閱讀對的題數：<input type="number" name="eng_read"><br><br>
                <button type="submit">計算英文分數</button>
            </form>
        </div>
    </div>
</body>
</html>
    """

if __name__ == "__main__":
    app.run(debug=True)
