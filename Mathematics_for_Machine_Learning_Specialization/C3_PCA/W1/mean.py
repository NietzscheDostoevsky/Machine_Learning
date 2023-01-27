# %%
import numpy as np

a1 = np.array([1, 4, 7])
a2 = np.array([2, 5, 8])
a3 = np.array([3, 6, 9])
(a1+a2+a3)/3

# %%
a1 = np.array([1, 2, 3])
a2 = np.array([3, 4, 5])
a3 = np.array([5, 3, 1])

(a1*2+a2*2+a3*2)/3

# %%
a1 = np.array([1, 2, 3])
a2 = np.array([3, 4, 5])
a3 = np.array([5, 3, 1])

b = np.array([1,2,3])
a1 = a1 + b
a2 = a2 + b
a3 = a3 + b

(a1+a2+a3)/3

# %%
d = np.array([1,2,3,2])
np.var(d)
np.std(d)
d1 = d + 1

# %%
