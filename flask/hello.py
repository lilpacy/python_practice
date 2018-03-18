# coding: UTF-8

from flask import Flask, render_template
import pymysql

app = Flask(__name__) # 何してる

@app.route('/') # ルーティング設定
def hello():

    # db setting
#    db = pymysql.connect(
#            host = 'localhost',
#            user = 'root',
#            password = 'root',
#            db = 'testdb',
#            charset = 'utf8',
#            cursorclass = pymysql.cursors.DictCursor,
#        )
#
#    cur = db.cursor()
#    sql = "select * from members"
#    cur.execute(sql)
#    members = cur.fetchall()
#
#    cur.close()
#    db.close()

    return render_template('hello.html', title='flask test') # render_template('ビュー',引数)

@app.route('/good')
def good():
    name = "Good"
    return name

## おまじない？
if __name__ == "__main__":
    app.run(debug=True)

