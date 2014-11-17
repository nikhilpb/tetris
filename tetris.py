from flask import Flask, render_template
tetris = Flask(__name__)

@tetris.route('/')
def index():
    return render_template('tetris.html')
