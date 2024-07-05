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
    def __init__(self, fields, collectionName = "SONG_DB", dim=384, connection_type:str = "default", host:str="localhost", port:str="19530"):
        self.collection_name:str = collectionName
        self.dim:int = dim
        
        # connect to db
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
    
    def ingest(self) -> Collection:
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=self.dim)
        ]
        
        schema = CollectionSchema(fields, description="")
        collection_milvus = Collection(version_name=self.collection_name, schema=schema, consistency_level="Strong")
        return collection_milvus
    