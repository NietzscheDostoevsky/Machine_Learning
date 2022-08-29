# %%
# PACKAGE
# Run this cell first once to load the dependancies.
import numpy as np
from numpy.linalg import norm, inv
from numpy import transpose
from readonly.bearNecessities import *

# %%

# GRADED FUNCTION
# You should edit this cell.

# In this function, you will return the transformation matrix T,
# having built it out of an orthonormal basis set E that you create from Bear's Basis
# and a transformation matrix in the mirror's coordinates TE.


# The parameter bearBasis is a 2×2 matrix that is passed to the function.
def build_reflection_matrix(bearBasis):
    # Use the gsBasis function on bearBasis to get the mirror's orthonormal basis.
    E = ???
    # Write a matrix in component form that performs the mirror's reflection in the mirror's basis.
    # Recall, the mirror operates by negating the last component of a vector.
    # Replace a,b,c,d with appropriate values
    TE = np.array([[a, b],
                   [c, d]])
    # Combine the matrices E and TE to produce your transformation matrix.
    T = ???
    # Finally, we return the result. There is no need to change this line.
    return T


˝
