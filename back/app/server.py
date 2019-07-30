from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api
from flask_cors import CORS
import random
import requests
from .data import Data

app = Flask(__name__)
# get data from file
app.config.from_object(Data())
# enable CORS
CORS(app)
api = Api(app)

photos = [{'id': 1, 'content': '', }, {'id': 2, 'content': '', }]


class Home(Resource):
    def get(self):
        return {'hello': 'world'}


class GetContent(Resource):
    def get(self):
        # API request
        a = requests.get(
            'https://picsum.photos/v2/list?page=2&limit=50')
        # if the API request is successful
        if a:
            # pick 3 random numbers to select two photos among 50 and a banner
            j = random.randint(0, 24)
            k = random.randint(25, 49)
            i = random.choice([0, 1, 2])
            photos[0]['content'] = a.json()[j]['download_url']
            photos[1]['content'] = a.json()[k]['download_url']
            return make_response(jsonify({'photos': photos, 'banner': app.config['BANNER'][i]}))
        # if the request is unsuccessful, send `Internal Server Error`
        else:
            return make_response(jsonify({"error": "API error"}), 500)


api.add_resource(Home, '/')
api.add_resource(GetContent, '/get_content/')

if __name__ == '__main__':
    app.run()
