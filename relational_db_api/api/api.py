from flask import Blueprint
from flask import request
from DbHandler import *

api = Blueprint('api', __name__)

@api.post('/ping')
def ping():
    return {
        "code" : 200,
        "type" : "ping",
        "message" : "active"
    }


@api.post('/search/phrase')
def search_playlist():
    data = request.json()

    DB_HANDLER = DbHandler()
    result = DB_HANDLER.search(data["search_phrase"])

    response = {

    }
    return response
    