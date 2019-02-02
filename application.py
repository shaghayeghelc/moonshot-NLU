#!usr/bin/env python3

# Importing Packages
from flask import Flask, jsonify
from flask import request
from flask_restful import Resource, Api
from dialogue_manager import DialogueManager
from flask_cors import CORS
import json
import os 

# Placeholder for the module
application = Flask(__name__)
cors = CORS(application, resources={r"/": {"origins": "*"}})
application.config['CORS_HEADERS'] = 'Content-Type'
api = Api(application)
 
class data(Resource):
    def get(self):
        return jsonify({"intent": 5})

    def post(self):
        data_json = request.get_json()
        print(data_json)
        request = data_json['request']
        language = data_json['language']
        DM = DialogueManager()
        if language == 'en':
            value = DM.intentClassifierEN(request)
        else:
            value = DM.intentclassifierFR(request)
        return jsonify({"intent": value})

api.add_resource(data, '/')

 
if __name__ == "__main__":
    application.run(host='0.0.0.0')

