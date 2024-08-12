from flask import Blueprint
from flask import request
from .DbHandler import DbHandler
import pandas as pd


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
    results = DB_HANDLER.get_data_from_ids(data["song_ids"])

    return format_song_data(results)

@api.post('/search/string')
def search_db():
    data = request.json
    user_input = data["user_input"]
    DB_HANDLER = DbHandler()
    results = DB_HANDLER.search_input(user_input)

    return format_song_data(results)    

def format_song_data(df: pd.DataFrame):
    response = {
        "song_data": []
    }
    
    song_data_structure = {
        "track_name": "",
        "track_artist": "",
        "track_popularity": -1,
        "track_album_name": "",
        "track_id": "" 
    }

    for index, row in df.iterrows():
        song_data_entry = song_data_structure.copy()  # Make a copy of the structure
        song_data_entry['track_name'] = row['track_name']
        song_data_entry['track_artist'] = row['track_artist']
        song_data_entry['track_popularity'] = row['track_popularity']
        song_data_entry['track_album_name'] = row['track_album_name']
        song_data_entry['track_id'] = row['track_id']
    
        response["song_data"].append(song_data_entry)


    return response