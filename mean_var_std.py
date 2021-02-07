import numpy as np

def calculate(list):
    # 1.) convert the list into Numpy array
    #   1a) error handling
    if not len(list) == 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(list).reshape((3, 3))
    # 2.) calculate 
    calculations ={
        "mean": [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(list)],
        "variance": [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(list)],
        "standard deviation": [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(list)],
        "max": [np.maximum(arr, axis=0).tolist(), np.maximum(arr, axis=1).tolist(), np.maximum(list)],
        "min": [np.minimum(arr, axis=0).tolist(), np.minimum(arr, axis=1).tolist(), np.minimum(list)],
        "sum": [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(list)]
    }

    # 3.) Return
    return calculations