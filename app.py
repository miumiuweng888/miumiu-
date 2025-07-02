from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return """
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>國中會考加權分數計算機</title>
    <meta name="keywords" content="國中會考, 會考分數計算, 國中英文成績, 國中數學成績, 線上會考工具, 加權分數計算">
</head>
<body>
    <h2 style="text-align:center;">國中會考加權分數計算機</h2>
    <div class="container">
    ...
<h2 style="text-align:center;">國中會考加權分數計算機</h2>
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
</style>
    """

@app.route("/math", methods=["POST"])
def calc_math():
    try:
        a = int(request.form.get("math_correct", 0))
        b = int(request.form.get("math_nonchoice", 0))
    except ValueError:
        return "請輸入正確的整數！"

    math_score = a * (85 / 25) + b * (15 / 6)
    return render_template_string("""
        <h2>計算結果</h2>
        <p>數學加權分數 = {{ math_score }}</p>
        <a href="/">回到首頁</a>
    """, math_score=round(math_score, 2))

@app.route("/english", methods=["POST"])
def calc_english():
    try:
        c = int(request.form.get("eng_listen", 0))
        d = int(request.form.get("eng_read", 0))
    except ValueError:
        return "請輸入正確的整數！"

    listen_total = 21
    read_total = 43
    english_score = (c / listen_total) * 20 + (d / read_total) * 80
    return render_template_string("""
        <h2>計算結果</h2>
        <p>英文加權分數 = {{ english_score }}</p>
        <a href="/">回到首頁</a>
    """, english_score=round(english_score, 2))

if __name__ == "__main__":
    app.run(debug=True)
