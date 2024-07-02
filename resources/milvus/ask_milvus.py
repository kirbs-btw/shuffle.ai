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
from sentence_transformers import SentenceTransformer 

def query_question(question, collection_milvus, model):

    question_embedding = model.encode([question])

    search_params = {
        "metric_type": "L2",
        "params": {"nprobe": 10},
    }

    result = collection_milvus.search(question_embedding, "embeddings", search_params, limit=5, output_fields=["content", "pagelabel"])

    return result


def search_db(question):
    # num_entities = 3000
    # dim = 768 # dim of the embeddings
    collection_name = "name-collection"

    # connecting to localhost db
    connections.connect("default", host="localhost", port="19530")

    collection_milvus = Collection(name=collection_name)  # Get the collection object
    collection_milvus.load()  # Load the collection into memory

    # get embedding model
    model = SentenceTransformer('distilbert-base-nli-mean-tokens')

    collection_milvus.load()

    results = query_question(question, collection_milvus, model)

    return results

def main():
    print("\n")
    found = search_db("What is the Error Number 40300?")

    for hits in found:
        for hit in hits:
            print("\n")
            print(hit.entity.get("content"))
            print(hit.entity.get("pagelabel"))
    
    
if __name__ == '__main__':
    main()

