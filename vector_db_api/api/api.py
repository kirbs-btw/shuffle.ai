from flask import Blueprint
from flask import request
from .MilvusHandler import MilvusHandler
import json

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
    # don't know if in need ?
    pass

# curl -X POST -H "Content-Type: application/json" -d '{ "song_ids": [ {"id": "42"}, {"id": "13"}]}' http://127.0.0.1:5000/search/playlist


@api.post('/search/playlist')
def search_playlist():
    """
    takes playlist and returns list of songs
    - openapi spec comming...
    playlist has form 
    {
        "song_ids": [
            {"id": 42},
            {"id": 13},
        ]
    }
    """
    print("search_playlist")
    print("data")

    # request.get_data() works to get a string
    # json.loads does not like me...
 
    data = json.loads(request.get_data())

    print(data)
    playlist_list = data['song_ids']

    # still need a way to sort out the songs that are already in the playlist
    
    # handle if the song is not in the db
    milvusHandler = MilvusHandler()
    results = milvusHandler.searchPlaylist(playlist_list)    

    # build response
    response = {
        "song_ids": []
    }
    for hits in results:
        for hit in hits:
            response["song_ids"].append(hit["id"])
    return response
    