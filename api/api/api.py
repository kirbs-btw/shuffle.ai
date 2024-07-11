from flask import Blueprint
from flask import request
from flask import jsonify
from MilvusHandler import *

api = Blueprint('api', __name__)

@api.post('/ping')
def ping():
    return {
        "code" : 200,
        "type" : "ping",
        "message" : "active"
    }

@api.post('/search/word')
def search_word():
    # correct open api comming 
    """
    request
    {
        "search_phrase" : int,
        "user": string, ?
    }

    response
    {
        results: {
            type: array,
            [
                {
                    id,
                    score
                }
            ]
        }
    }
    """
    pass

@api.post('/search/playlist')
def search_playlist():
    """
    takes playlist and returns list of songs
    - openapi spec comming...
    playlist has form 
    {
        "playlist": [
            {"id": 42},
            {"id": 13},
        ]
    }
    """

    data = request.json()
    playlist_list = data['playlist']


    milvusHandler = MilvusHandler()
    milvusHandler.searchPlaylist(playlist_list)    
    
    
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
    