from flask import Flask, render_template
app = Flask(__name__) # 何してる

@app.route('/') # ルーティング設定
def hello():
    name = "Hoge"
    return render_template('hello.html', title='flask test', name=name) # render_template('ビュー',引数)

@app.route('/good')
def good():
    name = "Good"
    return name

## おまじない？
if __name__ == "__main__":
    app.run(debug=True)

