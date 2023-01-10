# First we set the state of the network
import numpy as np
σ = np.tanh
w1 = 1.3
b1 = -0.1

# Then we define the neuron activation.


def a1(a0):
    z = w1 * a0 + b1
    return σ(z)

# Experiment with different values of x below.


x = 1
y = 0
a1(x)

# Cost function
c_k = np.square((a1(x) - y))
print(c_k)
