# coding:utf-8
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world_x():
    return "Hello World!だよ"

@app.route('/hello')
def hello_world_y():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True)
