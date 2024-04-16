from flask import Flask, request

import json

import mongo_interaction

app = Flask(__name__)


@app.route('/')
def home():
    return "An Application to Store, View and Delete Goals"


@app.route('/sample')
def sample():
    return json.dumps({'goal': "goal-name"})


@app.route('/store', methods=['POST'])
def store():
    if request.is_json:
        return mongo_interaction.Mongo_Connect("store", request.json)
    else:
        return json.dumps({'error': 'Request must contain JSON data'})


@app.route('/view', methods=['GET'])
def view():
    return mongo_interaction.Mongo_Connect("view")


@app.route('/delete', methods=['POST'])
def delete():
    if request.is_json:
        return mongo_interaction.Mongo_Connect("delete", request.json)
    else:
        return json.dumps({'error': 'Request must contain JSON data'})


if __name__ == "__main__":
    app.run(debug=True)
