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

# curl -X POST -H "Content-Type: application/json" -d '{ "song_ids": [ {"id": "d6416719-d5ad-44f9-ba72-7a922865bc3b"}, {"id": "5f3c97c1-cc14-4429-8e62-c586106ea7d3"}]}' http://127.0.0.1:5000/search/playlist

# curl -X POST -H "Content-Type: application/json" -d "{}" http://127.0.0.1:5000/search/playlist

# curl -X POST -H "Content-Type: application/json" -d """{ "playlist": [{"id": "d6416719-d5ad-44f9-ba72-7a922865bc3b"}, {"id": "5f3c97c1-cc14-4429-8e62-c586106ea7d3"}]}""" http://127.0.0.1:5000/search/playlist


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
           response["song_ids"].append(hit["id"])

    return response
    