# %%
# First we define the functions,
from scipy import optimize
import numpy as np


def f(x, y):
    return np.exp(-(2*x*x + y*y - x*y) / 2)


def g(x, y):
    return x*x + 3*(y+1)**2 - 1

# Next their derivatives,


def dfdx(x, y):
    return 1/2 * (-4*x + y) * f(x, y)


def dfdy(x, y):
    return 1/2 * (x - 2*y) * f(x, y)


def dgdx(x, y):
    return 2 * x


def dgdy(x, y):
    return (6 * y) + 6


# Solving

# %%
def DL(xyλ):
    [x, y, λ] = xyλ
    return np.array([
        dfdx(x, y) - λ * dgdx(x, y),
        dfdy(x, y) - λ * dgdy(x, y),
        - g(x, y)
    ])


# %%
(x0, y0, λ0) = (-1, -1, 0)
x, y, λ = optimize.root(DL, [x0, y0, λ0]).x
print("x = %g" % x)
print("y = %g" % y)
print("λ = %g" % λ)
print("f(x, y) = %g" % f(x, y))

# %%
# You should be able to use the code find the other roots of the system.

# Re-use the code above with different starting values to find the other stationary points on the constraint.
f_xy = list()
for i, j in zip(range(-10, 10), range(-10, 10)):

    (x0, y0, λ0) = (i, j, 0)
    x, y, λ = optimize.root(DL, [x0, y0, λ0]).x
    f_values = round(f(x, y), 4)
    if f_values in f_xy:
        continue  # no need for further execution
    else:
        f_xy.append(f_values)
    print("x = %g" % x)
    print("y = %g" % y)
    print("λ = %g" % λ)
    print("f(x, y) = %g" % f(x, y))
    print("--------------")
print(f_xy)


# %%
