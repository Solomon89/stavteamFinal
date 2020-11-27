from stavteam import app
from flask import render_template
from flask import jsonify, request

 

@app.route("/")
@app.route("/index")
def hello():
    return render_template("index.html", user="Stavteam")

from app import googleFit