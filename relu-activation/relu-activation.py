import numpy as np

def relu(x) -> np.ndarray:
    x = np.asarray(x, dtype=float)

    result = np.maximum(x, 0)

    return np.array(result)
    