from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model_data import *

app_api = Blueprint('api', __name__,
                   url_prefix='/api/college')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_api)

class DataAPI:
    # not implemented
    class _Create(Resource):
        def post(self, joke):
            pass
            
    # getJokes()
    class _Read(Resource):
        def get(self):
            return jsonify(getData())

    # getJoke(id)
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getData(id))

    # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_Create, '/create/<string:joke>')
    api.add_resource(_Read, '/')
    api.add_resource(_ReadID, '/<int:id>')
    
if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'https://sadv.nighthawkcodescrums.gq' # run from web
    url = server + "/api/college"
    responses = []  # responses list

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")