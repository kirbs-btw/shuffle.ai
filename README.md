# Shuffle.ai

## General
The project aims to use a [vector database](https://milvus.io/docs/install_standalone-docker.md) to find songs that fit well with a given playlist. By leveraging a vector database, the project tries interpret the overall theme or "direction" of the playlist and suggest songs that align closely with it. The playlists themselves are built using a relational database.

The method for embedding the songs (currently a work in progress and subject to further research) involves embedding song lyrics using the [e5-small](https://huggingface.co/intfloat/multilingual-e5-small) model. Each song in the playlist is represented as a vector in the database. By calculating the average of these vectors, the system can then search for the nearest matching songs in the database.

## Quality analysis
### Results on Small Dataset: 
The overall intention of the playlist generation is clear. For example, when creating a playlist labeled "girly party music," the algorithm suggests tracks that generally align with this theme (with 5 out of 10 songs being a good fit). Similarly, when generating a rap playlist, the recommendations lean heavily toward the genre. Considering the limited data available, the results are quite promising.

However, it's difficult to fully assess the quality of the recommended songs. Since the dataset only includes the top 3,000 worldwide hits, it's likely that any song suggested will already be a popular, high-quality track. Therefore, further analysis would be needed to judge whether the recommendations offer variety or true relevance beyond these popular songs.

### Results from Larger Dataset and Ingestion Tweaks:
The overall quality of the suggested titles decreased with the use of a larger dataset. Only 4 out of 10 suggestions were deemed acceptable or good for inclusion in the playlist. While the intention behind the recommendations remains identifiable, and the clustering of songs based on their lyrics still holds, the quality of recommendations has suffered. Notably, the genre range of the suggestions remains consistent.

An interesting observation is the quality of recommendations varies significantly depending on the genre of the playlist. For instance, pop music recommendations are considerably worse compared to those for Hip-Hop or Electronic genres.

With the expansion of the dataset, which includes many lesser-known songs, there are more selections that align with the lyrical themes of the playlist, but the overall quality of these tracks does not match that of the hit songs in the playlist. However, when a song does fit well, it often aligns better than before, likely due to the finer distinctions made possible by the larger dataset.

At this point, it is unclear how the ingestion changes have affected the output quality. Further research will be conducted to investigate this.

## Architecture
The Architecture is base on Flask. There is one frontend that is connected with a milvus and a relational DB.
Sketch comming...

## Setup
0. Install the [requirements.txt](https://github.com/kirbs-btw/shuffle.ai/blob/main/requirements.txt).
1. Setup the vectorstore with [this](https://github.com/kirbs-btw/shuffle.ai/blob/main/milvus/setup.sh) shell script.
2. Ingest the data into the vector store with the [ingestion notebook](https://github.com/kirbs-btw/shuffle.ai/blob/main/song_data/data_ingestion/data_ingestion.ipynb).
3. Run the [run.py](https://github.com/kirbs-btw/shuffle.ai/blob/main/run.py).
4. Access the project on [localhost](http://localhost:5000/).
5. Try it, fork it, open an issue, ...


## Datasets
[Small Dataset](https://raw.githubusercontent.com/kirbs-btw/shuffle.ai/refs/heads/main/song_data/old_data_preprocessing/song_data.csv) (3.5k):

The startingpoint for the songs is a [dataset](https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs) from kaggle. The set is cleaned for unnecessary columns and duplicates. With webscraping the data is extended by a lyrics column.

[Big Dataset](https://github.com/kirbs-btw/shuffle.ai/tree/main/song_data/big_data_scraping)(70k): 
1. Combining datasets to in terms of track_name and track_artist.
2. Adding a unique id to every song
3. scraping the lyrics via the [genius API](https://genius.com/)

Note: The big dataset is not inside the repo because the file is to big...

base datasets:
- [Top 30k Spotify Songs](https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs)
- [Most Streamed Spotify Songs 2024](https://www.kaggle.com/datasets/nelgiriyewithana/most-streamed-spotify-songs-2024)
- [Spotify Million Song Dataset](https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset)
- [Spotify 1.2M+ Songs](https://www.kaggle.com/datasets/rodolfofigueroa/spotify-12m-songs)

## Relevant Papers
B. Logan, A. Kositsky and P. Moreno, "[Semantic analysis of song lyrics](https://ieeexplore.ieee.org/abstract/document/1394328)" 2004 IEEE International Conference on Multimedia and Expo (ICME) (IEEE Cat. No.04TH8763), Taipei, Taiwan, 2004, pp. 827-830 Vol.2, doi: 10.1109/ICME.2004.1394328. 

K. I. Batcho, M. L. DaRin, A. M. Nave, and R. R. Yaworsky, "[Nostalgia and identity in song lyrics](https://doi.org/10.1037/1931-3896.2.4.236)," Psychology of Aesthetics, Creativity, and the Arts, vol. 2, no. 4, pp. 236-244, 2008, doi: 10.1037/1931-3896.2.4.236.

Wang, Liang, et al. "[Multilingual e5 text embeddings: A technical report](https://arxiv.org/abs/2402.05672)" arXiv preprint arXiv:2402.05672 (2024).

Wang, Jianguo, et al. "[Milvus: A purpose-built vector data management system](https://dl.acm.org/doi/abs/10.1145/3448016.3457550)" Proceedings of the 2021 International Conference on Management of Data. 2021.