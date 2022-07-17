from __init__ import app
from flask import render_template, request, jsonify
from db import *

@app.route('/', methods=["POST", 'GET'])
def Main():
    if request.method == "POST":
        return setLink(request.form['value'], request.form['time'])
    else:    
        return render_template('index.html')
    
@app.route('/<code>', methods=['GET'])
def showLink(code):
    return getLink(code)

 