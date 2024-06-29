import numpy as np
import pandas as pd 

# just some thinking 
# some vector describing the song
# songA = [0, 2, 5]
# songB = [1, 8, 2]
# songAvg = [1, 10, 7] / 2
# = [0.5, 5, 3.5]
# the question is how to combine songs with different depths ?

# some function to avg two v that have the same shape
#     
def avgV(vectorArr):
    # Convert vectors to numpy arrays
    npVectorArr = [np.array(i) for i in vectorArr]
    
    # checking for shape
    base_shape = npVectorArr[0].shape
    for i in npVectorArr[1:]:
        if base_shape != i.shape: raise ValueError("Vectors must have the same shape")

    sumV = npVectorArr[0]
    for i in npVectorArr[1:]:
        sumV += i
    
    # Calculate the average of the two vectors
    return sumV / len(vectorArr)

