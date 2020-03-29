from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

# Manual route
@app.route("/david")
def david():
    return "Hello, David!"

# Dynamic react to the route name
@app.route("/<string:name>")
def hello(name):
        name = name.capitalize()
        return f"Hello, {name}!!!"
