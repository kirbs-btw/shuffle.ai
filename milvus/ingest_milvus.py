import time

import numpy as np

from pymilvus import (
    connections,
    utility,
    FieldSchema, 
    CollectionSchema, 
    DataType,
    Collection,
)

#from PyPDF2 import PdfReader   # or any other PDF processing library
from sentence_transformers import SentenceTransformer 

fmt = "\n=== {:30} ===\n"
collection_name = "song_collection"

def setup_collection_structure():
    version_name = collection_name
    
    dim = 384

    print("---start connecting to Milvus---")
    connections.connect("default", host="localhost", port="19530")

    fields = [
        # FieldSchema(name="pk", dtype=DataType.VARCHAR, is_primary=False, auto_id=False, max_length=500),
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="title", dtype=DataType.VARCHAR, is_primary=False, auto_id=False, max_length=2048),
        FieldSchema(name="artist", dtype=DataType.VARCHAR, is_primary=False, auto_id=False, max_length=2048),
        FieldSchema(name="text_data", dtype=DataType.VARCHAR, is_primary=False, auto_id=False, max_length=2048),
        FieldSchema(name="duration", dtype=DataType.VARCHAR, is_primary=False, auto_id=False, max_length=2048),
        FieldSchema(name="link", dtype=DataType.VARCHAR, is_primary=False, auto_id=False, max_length=2048),
        FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=dim)
    ]

    schema = CollectionSchema(fields, description="a collection for testing with songs")

    print(f"---created schema---")

    print(f"---Create collection {version_name}---")
    collection_milvus = Collection(version_name, schema, consistency_level="Strong")
    
    return collection_milvus
    
def ingest_data_to_milvus(collection_milvus, data):
    labels = [i[0] for i in data]
    descriptions = [i[1] for i in data]
    artist = [i[2] for i in data]
    duration = [i[3] for i in data]
    link = [i[4] for i in data] 


    
    # Convert text to embeddings
    # model = SentenceTransformer('distilbert-base-nli-mean-tokens')
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # to be inserted the array of descriptions
    embeddings_text = model.encode(descriptions)

    entities = [
        descriptions, 
        labels,
        artist,
        duration,
        link,
        embeddings_text,
    ]

    # insert data to milvus
    collection_milvus.insert(entities)

    # creating the index for the data collection 
    print("---Start Creating index IVF_FLAT---")
    index = {
        "index_type": "IVF_FLAT",
        "metric_type": "L2",
        "params": {"nlist": 128},
    }

    collection_milvus.create_index("embeddings", index)

    print("---ingested data---")
    
def test_index(collection_milvus, search_query="love"):
    print("---testing collection search---")
    print("---loading in collection---")
    collection_milvus.load()
    # asking milvus
    
    # model = SentenceTransformer('distilbert-base-nli-mean-tokens')
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    question_embedding = model.encode([search_query])

    print("---Start searching based on vector similarity---")

    search_params = {
        "metric_type": "L2",
        "params": {"nprobe": 10},
    }

    result = collection_milvus.search(question_embedding, "embeddings", search_params, limit=3, output_fields=["title"])

    for hits in result:
        for hit in hits:
            print(f"hit: {hit}, title: {hit.entity.get('title')}, description: {hit.entity.get('description')}")
            print("------------")

def clearMilvus():
    connections.connect("default", host="localhost", port="19530")
    
    # Check if the collection exists
    if utility.has_collection(collection_name):
        # Drop the collection
        utility.drop_collection(collection_name)
        print(f"Collection '{collection_name}' has been deleted.")
    else:
        print(f"Collection '{collection_name}' does not exist.")

def main():
    clearMilvus()
    
    # my data : "name", "description"
    data = [
        ["Perfect", "Love", "Ed Sheeran", 3.15, "link"],
        ["c'est la vie", "Pop", "Young Gravy", 2.50, "link"],
        ["Kleine Nacht Musik", "Classic", "Mozart", 5.20, "link"],
    ]
    

    collection_milvus = setup_collection_structure()
    ingest_data_to_milvus(collection_milvus, data)
    test_index(collection_milvus, search_query="classic")
    
    clearMilvus()

# after some testing 
# the search feels like crap
# i search "classic" it finds the "classic" but the second entry it about "love" and the third is "classical"
# i think the modle is not greate

# some issue with the model 
# --> distance to small


if __name__ == '__main__':
    main()
    
# miluvs will be the song db in the background
# the vector will somehow save the "vibe" of the song
# title song search is going to be over a relational db or a normal pattern search in the vector db
