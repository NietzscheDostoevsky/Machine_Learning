# %%

from scipy import optimize
import pandas as pd


def f(x):
    return x**6/6 - 3*x**4 - 2*x**3/3 + 27*x**2/2 + 18*x - 30


def d_f(x):
    return x**5 - 12*x**3 - 2*x**2 + 27*x + 18


# %%
d.clear()
x = 1.99

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
    return x**6/6 - 3*x**4 - 2*x**3/3 + 27*x**2/2 + 18*x - 30


x0 = -5
optimize.newton(f, x0)

# %%
