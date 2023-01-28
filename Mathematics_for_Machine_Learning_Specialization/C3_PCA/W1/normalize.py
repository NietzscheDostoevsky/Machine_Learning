
# %%
import numpy as np


def normalize(x):
    """
    Normalize all the columns of x

    Arguments:
    x: A two dimensional Numpy array

    Returns:
    c: The normalized version of x
    """

    # BEGIN SOLUTION

    # Calculate the mean of all columns
    mean = np.mean(x, axis=0, keepdims=True)

    # Calculate the standard deviation all columns
    sigma = np.std(x, axis=0, keepdims=True)

    # Compute the final answer
    c = (x - mean) / sigma

    # END SOLUTION

    return c


# %%
x = np.array([[1, 4],
              [3, 2]])
expected = np.array([[-1, 1],
                     [1, -1]])
np.testing.assert_allclose(normalize(x), expected, rtol=1e-5)

x = np.array([[324.33, 136.11, 239.38, 237.17],
              [123.43, 325.24, 243.52, 745.25],
              [856.36, 903.02, 430.25, 531.35]])
expected = np.array([[-0.35694152, -0.97689929, -0.73023324, -1.28391946],
                     [-1.00662188, -0.39712973, -0.68372539,  1.1554411],
                     [1.3635634,  1.37402902,  1.41395863,  0.12847837]])
np.testing.assert_allclose(normalize(x), expected, rtol=1e-5)

print("All tests passed!")

# %%
