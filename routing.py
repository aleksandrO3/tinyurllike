from __init__ import app
from flask import render_template, redirect, request
from db import *

@app.route('/', methods=["POST", "GET"])
def  Main():
    if request.method == "POST":
        hash = setLink(request.form['value'], request.form['time'])
        return f'<h1>{hash}</h1>'
    elif request.method == "GET" and request.args.get('link'):
        link = getLink(request.args.get('link'))
        return f'<h1>{link}</h1>'
    else:
        return render_template('index.html')
    

    

 