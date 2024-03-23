from flask import Flask, request, jsonify

import requests

app = Flask(__name__)


def get_data_from_swapi(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()
        return json_data
    except Exception as e:
        print("ERROR: ", e)
        return None


@app.route('/')
def home():
    return "<h3>Information about Star Wars</h3>"


@app.route('/fav', methods=['GET'])
def get_favs():
    return "<h3>Give the favs here</h3>"


@app.route('/fav', methods=['POST'])
def post_favs():
    item_data = request.json
    return jsonify(item_data)


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


if __name__ == "__main__":
    app.run(debug=True)