from flask import Blueprint
from flask import request
from flask import jsonify

api = Blueprint('api', __name__)

@api.post('/ping')
def ping():
    return {
        "code" : 200,
        "type" : "ping",
        "message" : "active"
    }


@api.post('/search/playlist')
def search_playlist():
    """
    takes playlist and returns list of songs
    - openapi spec comming...
    """
    pass    
    
    
# testing 
@api.post('/api/app')
def app():

    data = request.get_json() 
    return {
        "code" : 200,
        "type" : "success",
        "message" : "worked with the data",
        "data" : data
    }
    