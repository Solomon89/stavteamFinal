from flask import Flask
app = Flask(__name__)

@app.route("/Auth")
def Auth():
    return "<h1 style='color:orange'>Hello Google!</h1>"   


