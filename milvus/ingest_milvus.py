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

from PyPDF2 import PdfReader   # or any other PDF processing library
from sentence_transformers import SentenceTransformer 

fmt = "\n=== {:30} ===\n"

def setup_collection_structure():
    version_name = "test-name"

    
    dim = 768

    print("---start connecting to Milvus---")
    connections.connect("default", host="localhost", port="19530")

    fields = [
        # FieldSchema(name="pk", dtype=DataType.VARCHAR, is_primary=False, auto_id=False, max_length=500),
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="content", dtype=DataType.VARCHAR, is_primary=False, auto_id=False, max_length=2048),
        FieldSchema(name="pagelabel", dtype=DataType.INT64, is_primary=False, auto_id=False),
        FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=dim)
    ]

    schema = CollectionSchema(fields, "hello_milvus is the simplest demo to introduce the APIs")

    print(f"---Create collection {version_name}---")
    collection_milvus = Collection(version_name, schema, consistency_level="Strong")
    
    return collection_milvus
    
def process_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text_arr = []
        page_numbers = []
        for page_num in range(len(reader.pages)):
            page_numbers.append(page_num+1)
            page_text = reader.pages[page_num].extract_text()
            text_arr.append(page_text)
                
        return text_arr, page_numbers

def ingest_data_to_milvus(collection_milvus,pdf_path):
    # Sample usage:
    pdf_text_arr, page_num_arr = process_pdf(pdf_path)

    # Convert text to embeddings
    model = SentenceTransformer('distilbert-base-nli-mean-tokens')

    embeddings_text = model.encode(pdf_text_arr)

    entities = [
        pdf_text_arr,
        page_num_arr, 
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

def test_index(collection_milvus):
    print("---loading in collection---")
    collection_milvus.load()
    # asking milvus

    question = "What is the Error Number 40300?"
    question_embedding = model.encode([question])

    print("---Start searching based on vector similarity---")

    search_params = {
        "metric_type": "L2",
        "params": {"nprobe": 10},
    }

    result = collection_milvus.search(question_embedding, "embeddings", search_params, limit=3, output_fields=["content"])

    for hits in result:
        for hit in hits:
            print(f"hit: {hit}, random field: {hit.entity.get('content')}")
            print("------------")


def main():
    pdf_path = "TRUMPF_Manual_TruConvert_DC_1030.pdf"
    collection_milvus = setup_collection_structure()
    ingest_data_to_milvus(collection_milvus, pdf_path)
    test_index(collection_milvus)
    
if __name__ == '__main__':
    main()
    