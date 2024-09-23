# Shuffle.ai
You can test the project [here]().
If there is no website --> project not finished :) 

## General
The project aims to use a [vector database](https://milvus.io/docs/install_standalone-docker.md) to find fitting songs for a playlist. Using the Vector DB the project understands the direction of the playlist and can suggest really fitting songs. Building up the Playlist with a relational DB. 

The method of embedding the songs (work in progress / research) is to embedd the songs lyrics with the [e5-small](https://huggingface.co/intfloat/multilingual-e5-small) model. The playlist contains multiple songs that all can be described by a vector in the db. After taking the average the nearest fitting songs are searched in the db. 

## Quality analysis
Unittests comming...

Reuslts at first glance are ok --> 3 out of 6 suggestions okay fit the playlist

## Architecture
The Architecture is base on Flask. There is one frontend that is connected with a milvus and a relational DB.
Sketch comming...

## Setup
0. Install the [requirements.txt](https://github.com/kirbs-btw/shuffle.ai/blob/main/requirements.txt).
1. Setup the vectorstore with [this](https://github.com/kirbs-btw/shuffle.ai/blob/main/milvus/setup.sh) shell script.
2. Ingest the data into the vector store with the [ingestion notebook](https://github.com/kirbs-btw/shuffle.ai/blob/main/song_data/data_ingestion/data_ingestion.ipynb).
3. Run the [run.py](https://github.com/kirbs-btw/shuffle.ai/blob/main/run.py).
4. Access the project on [localhost](http://localhost:5000/).
5. Try it - open an issue, ...


## Data
[Small Dataset](https://raw.githubusercontent.com/kirbs-btw/shuffle.ai/refs/heads/main/song_data/old_data_preprocessing/song_data.csv) (3.5k):

The startingpoint for the songs is a [dataset](https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs) from kaggle. The set is cleaned for unnecessary columns and duplicates. With webscraping the data is extended by a lyrics column.

[Big Dataset](https://github.com/kirbs-btw/shuffle.ai/tree/main/song_data/big_data_scraping)(90k): 
1. Combining datasets to in terms of track_name and track_artist.
2. Adding a unique id to every song
3. scraping the lyrics via the [genius API](https://genius.com/)

datasets:
- [Top 30k Spotify Songs](https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs)
- [Most Streamed Spotify Songs 2024](https://www.kaggle.com/datasets/nelgiriyewithana/most-streamed-spotify-songs-2024)
- [Spotify Million Song Dataset](https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset)
- [Spotify 1.2M+ Songs](https://www.kaggle.com/datasets/rodolfofigueroa/spotify-12m-songs)



## WIP - Comments
- fine tweek milvus 
- filter out basic words, something like I, you, and, filler words...
- get some test going to determin if the suggestion gets better