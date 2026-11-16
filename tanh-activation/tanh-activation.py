import numpy as np

def tanh(x: list) -> np.ndarray:
    x = np.asarray(x, dtype=float)

    result = (np.exp(x) - np.exp(-x))/(np.exp(x)+np.exp(-x))

    return np.array(result)