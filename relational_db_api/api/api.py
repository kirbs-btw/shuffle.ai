from flask import Blueprint
from flask import request
from .DbHandler import DbHandler

api = Blueprint('api', __name__)

@api.post('/ping')
def ping():
    return {
        "code" : 200,
        "type" : "ping",
        "message" : "active"
    }


@api.post('/get/songs')
def search_playlist():
    """
    input = {
        "songs_ids": [
            {"id": "some_id"}
        ]
    }
    """

    data = request.json

    DB_HANDLER = DbHandler()
    results = DB_HANDLER.get_data_from_ids(data["songs_ids"])
    print(results)

    response = {
        "song_data": []
    }
    
    for result in results:
        response.append(result)
    return response
    