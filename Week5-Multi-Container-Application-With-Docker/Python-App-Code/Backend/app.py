from flask import Flask, request

import json
import logging
import mongo_interaction

app = Flask(__name__)

logging.basicConfig(filename='requests.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@app.route('/')
def home():
    return "An Application to Store, View and Delete Goals"


@app.route('/sample', methods=['GET'])
def sample():
    log_request(request)
    return json.dumps({'goal': "goal-name"})


@app.route('/store', methods=['POST'])
def store():
    log_request(request)
    if request.is_json:
        data = mongo_interaction.Mongo_Connect("store", request.json)
    else:
        data = json.dumps({'error': 'Request must contain JSON data'})
    log_response(data)
    return data


@app.route('/view', methods=['GET'])
def view():
    log_request(request)
    data = mongo_interaction.Mongo_Connect("view")
    log_response(data)
    return data


@app.route('/delete', methods=['POST'])
def delete():
    log_request(request)
    if request.is_json:
        data = mongo_interaction.Mongo_Connect("delete", request.json)
    else:
        data = json.dumps({'error': 'Request must contain JSON data'})
    log_response(data)
    return data


def log_request(req):
    logging.info(f"{req.method} request to {req.url} with data: {req.data}")


def log_response(res):
    logging.info(str(res))


if __name__ == "__main__":
    app.run(debug=True)
