import numpy as np


class MilvusHandler:
    def __init__(self):
        pass
    
    def __avg_vector_array(self, vectorArr):
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
    