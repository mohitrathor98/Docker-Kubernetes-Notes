from flask import Flask, request
from pymongo import MongoClient
# pymongo needs to be installed

import requests

app = Flask(__name__)


@app.route('/')
def home():
    return "<h3>Information about Star Wars</h3>"


@app.route('/fav', methods=['GET'])
def get_favs():
    data = mongo_interactions()
    return f"<h3>{data}</h3>"


@app.route('/fav', methods=['POST'])
def post_favs():
    item_data = request.json
    return mongo_interactions(item_data)


@app.route('/movies', methods=['GET'])
def get_movies():
    data = get_data_from_swapi('https://swapi.dev/api/films/')
    title = data["results"][0]["title"]
    details = data["results"][0]["opening_crawl"]
    return f"<h3>{title}</h3><h4>{details}</h4>"


@app.route('/people', methods=['GET'])
def get_people():
    data = get_data_from_swapi('https://swapi.dev/api/people/')
    name = data["results"][0]["name"]
    return f"<h3>Your people is --- {name}</h3>"


def get_data_from_swapi(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()
        return json_data
    except Exception as e:
        print("ERROR: ", e)
        return None


def mongo_interactions(data=None):
    client = MongoClient('mongodb://172.17.0.2:27017/')
    db = client['favorites']
    if data is None:
        return get_data(db)
    else:
        return post_data(db, data)


def get_data(db):
    data = []
    for col in ['movie', 'people']:
        collection = db[col]
        cursor = collection.find()
        for document in cursor:
            data.append(str(document))
    return data


def post_data(db, data):
    if 'movie' in data.keys():
        collection = db['movie']
    else:
        collection = db['people']

    result = collection.insert_one(data)
    return f"Inserted the data. ID: {result.inserted_id}"


if __name__ == "__main__":
    app.run(debug=True)
