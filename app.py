from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'index page :)'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)

@app.route('/music')
def music():
    return render_template('index1.html')