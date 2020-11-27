from stavteam import app
from flask import render_template
from flask import jsonify, request

 

@app.route("/")
@app.route("/index")
def hello():
    return "<h1 style='color:orange'>Hello There!</h1>"

from app import googleFit