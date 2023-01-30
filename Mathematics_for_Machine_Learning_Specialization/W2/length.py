

import numpy as np


def length(x):
    """Compute the length of a vector"""
    length_x = 0
    for i in range(x.shape[0]):
        length_x = length_x + (x[i] * x[i])

    length_x = np.sqrt(length_x)

    return length_x


print(length(np.array([1, 0])))

# Always generalize the code
