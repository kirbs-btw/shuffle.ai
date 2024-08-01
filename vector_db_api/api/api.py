from flask import Blueprint
from flask import request
from .MilvusHandler import MilvusHandler
import json

api = Blueprint('api', __name__)

@api.route('/alive')
def alive():
    return {
        "code" : 200,
        "type" : "ping",
        "message" : "active"
    }

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
    # don't know if in need ?
    pass

@api.post('/search/playlist')
def search_playlist():
    # need to optimize that fun stuff here
    """
    playlist has form 
    {
        "playlist": [
            {"id": 42},
            {"id": 13},
        ]
    }
    """

    data = request.json

    playlist_list = data['playlist']

    # still need a way to sort out the songs that are already in the playlist
    
    # handle if the song is not in the db
    milvusHandler = MilvusHandler()
    results = milvusHandler.search_playlist(playlist_list)    

    # build response
    response = {
        "song_ids": []
    }
    for hits in results:
       for hit in hits:
           response["song_ids"].append(hit.id)
    
    return response
    