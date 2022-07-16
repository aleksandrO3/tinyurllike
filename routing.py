from __init__ import app
from flask import render_template

@app.route('/')
def showMain():
    return render_template('index.html')
