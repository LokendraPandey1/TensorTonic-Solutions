import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    x = np.asarray(x, dtype=float)

    result = 1/(1+np.exp(-x))

    return np.array(result)