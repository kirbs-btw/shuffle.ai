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

class MilvusHandler:
    def __init__(self, 
                 fields, 
                 collectionName = "SONG_DB", 
                 indexName = "embeddings",
                 dim=384, 
                 connection_type:str = "default", 
                 host:str="localhost", 
                 port:str="19530", 
                 embedding_model="intfloat/multilingual-e5-large"):
        
        self.collection_name:str = collectionName
        self.dim:int = dim
        self.index_name:str = indexName
        self.embedding_model = embedding_model
        self.connection_type:str = connection_type
        self.host:str = host
        self.port:str = port



        self.__connect_to_db(connection_type=connection_type, host=host, port=port)
        
    def __connect_to_db(self, connection_type:str = "default", host:str="localhost", port:str="19530") -> None:
        connections.connect(connection_type, host=host, port=port)
        
    def __avg_vector_array(self, vectorArr) -> np.array:
        # Convert vectors to numpy arrays
        npVectorArr = [np.array(i) for i in vectorArr]
        
        # checking for shape
        base_shape = npVectorArr[0].shape
        for i in npVectorArr[1:]:
            if base_shape != i.shape: raise ValueError("Vectors must have the same shape")

        # calculate the avg vector
        sumV = npVectorArr[0]
        for i in npVectorArr[1:]: sumV += i
        return sumV / len(vectorArr)
    
    def setup_collection(self) -> Collection:
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=self.dim)
        ]
        
        schema = CollectionSchema(fields, description="")
        collection_milvus = Collection(version_name=self.collection_name, schema=schema, consistency_level="Strong")
        return collection_milvus
    
    def ingest_data(self, data):
        """ 
        data = [
            [id, song_description] 
        ]
        """
        
        id_arr: list = [data_point[0] for data_point in data]
        description_arr: list = [data_point[1] for data_point in data]
        
        model: SentenceTransformer = SentenceTransformer(self.embedding_model)    

        description_embedding: list = model.encode(description_arr)
        
        entities = [
            id_arr, 
            description_embedding,
        ]

        collection_milvus: Collection = Collection(name=self.collection_name) 
        # insert data to milvus
        collection_milvus.insert(entities)
        
        index = {
            "index_type": "IVF_FLAT",
            "metric_type": "L2",
            "params": {"nlist": 128},
        }
        collection_milvus.create_index(self.index_name, index)

    def search_embedding(self, embedding) -> list:
        collection_milvus: Collection = Collection(name=self.collection_name) 
        collection_milvus.load()

        search_params = {
            "metric_type": "L2",
            "params": {"nprobe": 10},
        }

        # results
        return collection_milvus.search(embedding, "embeddings", search_params, limit=3, output_fields=["id"])
    
    def clear_collection(self) -> None:
        self.__connect_to_db(connection_type= self.connection_type, host=self.host, port=self.port)
            # Check if the collection exists
        if utility.has_collection(self.collection_name):
            # Drop the collection
            utility.drop_collection(self.collection_name)
            print(f"Collection '{self.collection_name}' has been deleted.")
        else:
            print(f"Collection '{self.collection_name}' does not exist.")