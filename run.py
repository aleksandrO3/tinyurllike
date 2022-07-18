from flask import Flask, request
from db import *

app = Flask(__name__)

@app.route('/', methods=["POST"])
def processingPost():
    data = request.get_json()
    return setLink(data)
  
    
@app.route('/<code>', methods=['GET'])
def showLink(code):
    return getLink(code)


if __name__ == '__main__':
    app.run(debug=True)

