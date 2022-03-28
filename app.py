from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/tweedeurl")
def hello_second_world():
    return "<p>Hello, Tweede World!</p>"