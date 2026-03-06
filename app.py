from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "<p>hello</p>"
@app.route("/louis")
def louis():
    return "<h1>JE SUIS LOUIS</h1>"

