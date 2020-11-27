from stavteam import app
from flask import render_template
from flask import jsonify, request
from app import db

@app.route('/auth2')
def Auth():
    s = (db.GetAuth())
    return "<h1 style='color:orange'> "+str(s)+" </h1>"   

