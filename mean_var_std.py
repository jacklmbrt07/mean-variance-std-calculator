import numpy as np

def calculate(list):
    # 1.) convert the list into Numpy array
    arr = np.array(list).reshape((3, 3))
    # 2.) calculate 
    calculations ={
        "mean": [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(list)],
        "variance": [],
        "standard deviation": [],
        "max": [],
        "min": [],
        "sum": []
    }

    # 3.) Return
    return calculations