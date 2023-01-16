# %%
# First we define the functions,
from scipy import optimize
import numpy as np


def f(x, y):
    return -(np.exp(x - y**2 + x*y))


def g(x, y):
    return (np.cosh(y) + x - 2)

# Next their derivatives,


def dfdx(x, y):
    return (1+y) * f(x, y)


def dfdy(x, y):
    return (x - 2*y) * f(x, y)


def dgdx(x, y):
    return 1


def dgdy(x, y):
    return np.sinh(y)


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
print(g(x, y))

# %%
# You should be able to use the code find the other roots of the system.

# Re-use the code above with different starting values to find the other stationary points on the constraint.
f_xy = list()
for i, j in zip(range(-10, 10), range(-10, 10)):

    (x0, y0, λ0) = (i, j, 0)
    x, y, λ = optimize.root(DL, [x0, y0, λ0]).x
    f_values = round(f(x, y), 4)
    if f_values in f_xy:
        continue
    else:
        f_xy.append(f_values)
    print("x = %g" % x)
    print("y = %g" % y)
    print("λ = %g" % λ)
    print("f(x, y) = %g" % f(x, y))
    print("--------------")
print(f_xy)


# %%
