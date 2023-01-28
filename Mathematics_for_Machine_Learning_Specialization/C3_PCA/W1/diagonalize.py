# %%
import numpy as np


def diagonalize(A):
    """
    Diagonalizes the input matrix A

    Arguments:
    A: A two dimensional Numpy array which is guaranteed to be diagonalizable

    Returns:
    S, D, S_inv: As explained above
    """

    # BEGIN SOLUTION

    # Retrieve the number of rows in A
    n = A.shape[0]

    # Get the eigenvalues and eigenvectors of A
    eig_vals, S = np.linalg.eig(A)

    # Start by initializing D to a matrix of zeros of the appropriate shape
    D = np.zeros(A.shape)

    # Set the diagonal element of D to be the eigenvalues
    for i in range(n):
        D[i, i] = eig_vals[i]

    # Compute the inverse of S
    S_inv = np.linalg.inv(S)

    # END SOLUTION

    return S, D, S_inv


# %%
A = np.array([[1, 5],
              [2, 4]])
S_exp = np.array([[-0.92847669, -0.70710678],
                  [0.37139068, -0.70710678]])
D_exp = np.array([[-1, 0],
                  [0, 6]])
S_inv_exp = np.array([[-0.76930926,  0.76930926],
                      [-0.40406102, -1.01015254]])

print("1")
S, D, S_inv = diagonalize(A)
print("2")

np.testing.assert_allclose(S_exp, S, rtol=1e-5, atol=1e-10)
print("3")

np.testing.assert_allclose(D_exp, D, rtol=1e-5, atol=1e-10)
print("4")

np.testing.assert_allclose(S_inv_exp, S_inv, rtol=1e-5, atol=1e-10)
print("5")


A = np.array([[4, -9, 6, 12],
              [0, -1, 4, 6],
              [2, -11, 8, 16],
              [-1, 3, 0, -1]])
S_exp = np.array([[5.00000000e-01, -8.01783726e-01,  9.04534034e-01,  3.77964473e-01],
                  [5.00000000e-01, -5.34522484e-01,
                      3.01511345e-01,  7.55928946e-01],
                  [-5.00000000e-01,  1.98636631e-14,
                      3.01511345e-01,  3.77964473e-01],
                  [5.00000000e-01, -2.67261242e-01, -5.03145109e-15,  3.77964473e-01]])
D_exp = np.array([[1, 0, 0, 0],
                  [0, 2, 0, 0],
                  [0, 0, 3, 0],
                  [0, 0, 0, 4]])
S_inv_exp = np.array([[2.00000000e+00, -1.00000000e+01,  4.00000000e+00,  1.40000000e+01],
                      [3.74165739e+00, -2.24499443e+01,
                          1.12249722e+01,  2.99332591e+01],
                      [3.31662479e+00, -1.32664992e+01,
                          6.63324958e+00,  1.65831240e+01],
                      [2.74154909e-15, -2.64575131e+00,  2.64575131e+00,  5.29150262e+00]])

S, D, S_inv = diagonalize(A)
print("6")

np.testing.assert_allclose(S_exp, S, rtol=1e-5, atol=1e-10)
print("7")

np.testing.assert_allclose(D_exp, D, rtol=1e-5, atol=1e-10)
print("8")

np.testing.assert_allclose(S_inv_exp, S_inv, rtol=1e-5, atol=1e-10)
print("9")


print("All tests passed!")

# %%
