from flask import Blueprint, render_template
from flask import request
from flask import jsonify

api = Blueprint('api', __name__)

@api.post('/api/ping')
def ping():
    return {
        "code" : 200,
        "type" : "ping",
        "message" : "active"
    }

@api.post('/api/app')
def app():

    data = request.get_json() 
    return {
        "code" : 200,
        "type" : "success",
        "message" : "worked with the data",
        "data" : data
    }
    