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
        "max": [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(list)],
        "min": [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(list)],
        "sum": [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(list)]
    }

    # 3.) Return
    return calculations