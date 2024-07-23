# Shuffle.ai
You can test the project [here]().

## General
The project aims to use a [vector database](https://milvus.io/docs/install_standalone-docker.md) to find fitting songs for a playlist. Using the Vector DB the project understands the direction of the playlist and can suggest really fitting songs. Building up the Playlist with a relational DB.

## Quality analysis

## Achitecture

## Vector DB
### Setup
The project uses a milvus vectordatabase setup with the [e5-small](https://huggingface.co/intfloat/multilingual-e5-small) embedding model to create the vector representation.

### Ingestion


## Data
The startingpoint for the songs is a [dataset](https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs) from kaggle. The set is cleaned for unnecessary columns and duplicates. With webscraping the data is extended by a lyrics column.
