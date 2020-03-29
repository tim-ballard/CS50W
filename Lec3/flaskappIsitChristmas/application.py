from flask import Flask, render_template
from datetime import date

app = Flask(__name__)


@app.route("/")
def check():
    today = date.today()
    newyearcheck = today.month == 1 and today.day == 1
    return render_template("index.html", newyearcheck=newyearcheck)
