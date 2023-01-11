# %%

from scipy import optimize
import pandas as pd
import numpy as np


def f(x):
    return np.sin(x)


def d_f(x):
    return np.cos(x)


# %%
d.clear()
x = 14.0

d = {"x": [x], "f(x)": [f(x)], "d_f(x)": [d_f(x)]}
# %%
for i in range(0, 30):
    x = x - f(x) / d_f(x)
    d["x"].append(x)
    d["f(x)"].append(f(x))
    d["d_f(x)"].append(d_f(x))

pd.DataFrame(d, columns=['x', 'f(x)', 'd_f(x)'])

# %%


def f(x):
    return np.sin(x)


x0 = 14.0
optimize.newton(f, x0)

# %%
