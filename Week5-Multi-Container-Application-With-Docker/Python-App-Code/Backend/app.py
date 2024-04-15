from flask import Flask, request

import json

app = Flask(__name__)


@app.route('/')
def home():
    return "An Application to Store, View and Delete Goals"


@app.route('/store', methods=['POST'])
def store():
    if request.is_json:
        return request.json
    else:
        return json.dumps({'error': 'Request must contain JSON data'})


@app.route('/view')
def view():
    pass


@app.route('/delete')
def delete():
    pass
