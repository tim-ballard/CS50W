from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    names = ["Tim", "Simon", "Bob"]
    return render_template("index.html", names=names)
