from stavteam import app
from flask import render_template
from flask import jsonify, request


@app.route('/auth2')
def Auth():
    return "<h1 style='color:orange'>Hello Google!</h1>"   
