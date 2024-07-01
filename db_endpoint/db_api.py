# setup flask api - serverless setup

# getting db

# search db

# some helper functions 

from flask import Blueprint, render_template
from flask import request

api = Blueprint('api', __name__)

@api.route('/api/ping')
def ping():
    package = request.args['package']
    return {
        "code" : 200,
        "type" : "ping",
        "message" : package
    }

@api.route('/api/status')
def status():
    expl_json = {
        "code" : 200,
        "type" : "status",
        "message" : "active"
    }

    return expl_json

@api.post('/api/app')
def run():
    data = request.json
    
    # doing something with the pushed data
     
    return {
        "code" : 200,
        "type" : "success",
        "message" : "worked with the data"
    }
    