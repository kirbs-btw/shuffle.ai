from flask import Blueprint, render_template, request
from .backend.DbHandler import DbHandler
from .backend.MilvusHandler import MilvusHandler
import pandas as pd

main = Blueprint('main', __name__)


# still need 
playlist_ids = []

DB_HANDLER = DbHandler()
MILVUS_HANDLER = MilvusHandler()


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

@main.post('/remove_song')
def remove_song():
    data = request.json
    input = data['song_id']
    playlist_ids.remove(input)

    return {"msg": "done"}

@main.post('/add_song_to_playlist')
def add_song_to_playlist():
    data = request.json
    id = data["song_id"]
    playlist_ids.append(id)
    id_list = [id]
    resp = DB_HANDLER.getDataFromIdList(id_list)

    return {
        "track_name": resp["track_name"].iloc[0],
        "track_artist": resp["track_artist"].iloc[0],
        "track_id": resp["track_id"].iloc[0]
    }

@main.post('/playerlist_suggestions')
def get_songs_from_playlist():
    print("here1")
    results = MILVUS_HANDLER.suggestion_songs_from_ids(playlist_ids)
    
    print("here2")
    response = []
    for hits in results:
       for hit in hits:
           response.append(hit.id)

    print("here3")
    suggestionsDf = DB_HANDLER.getDataFromIdList(response)

    print("here4")
    for id in playlist_ids:
        suggestionsDf = suggestionsDf[suggestionsDf['track_id'] != id]

    print("here5")

    return {
        "data": [
            { 
                "track_name" : row["track_name"],
                "track_artist" : row["track_artist"],
                "track_id": row["track_id"]
            } 
            for index, row in suggestionsDf.iterrows() 
        ]
    }

