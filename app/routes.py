from flask import Blueprint, render_template, request
from .backend.DbHandler import DbHandler
from .backend.MilvusHandler import MilvusHandler
import pandas as pd

main = Blueprint('main', __name__)
playlist_ids = []


DB_HANDLER = DbHandler()
# MILVUS_HANDLER = MilvusHandler()


@main.route('/')
def index():
    return render_template('index.html')

@main.post('/word_search')
def get_songs_from_word_search():
    """
    {
        "input": {
            "type": "string"
        }
    }
    """

    data = request.json
    user_input = data["input"]

    results: pd.DataFrame = DB_HANDLER.searchInput(user_input)

    return {
        "data": [
            { 
                "track_name" : row["track_name"],
                "track_artist" : row["track_artist"],
                "track_id": row["track_id"]
            } 
            for index, row in results.iterrows() 
        ]
    }

@main.post('/add_song')
def add_song():
    data = request.json
    id = data["song_id"]
    playlist_ids.append(id)


@main.post('/playerlist_suggestions')
def get_songs_from_playlist():
    """
    {
        playlist: {
            "type": "array"
            "items": {
                "song_id": {
                    "type": "string"
                }
            }
        }
    }
    """

    # don't know about the logic behind the db handler and the mapping 
    # of the found id to song data seems a bite komplex writte 
    # rebuild pls

    data = request.json
    playlist = data["playlist"]

    results = MILVUS_HANDLER.search_playlist(playlist)

    response = []
    for hits in results:
       for hit in hits:
           response.append(hit.id)

    DB_HANDLER.get_data_from_ids(response)


    return response

