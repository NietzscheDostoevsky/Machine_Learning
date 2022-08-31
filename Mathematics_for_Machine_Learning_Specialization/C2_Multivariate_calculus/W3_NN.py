# Simple Artificial Neural Networks _ Coursera

# First we set the state of the network
import numpy as np
σ = np.tanh
w1 = 1.3
b1 = -0.1

# Then we define the neuron activation.


def a1(a0):
    return σ(w1 * a0 + b1)


# Finally let's try the network out!
# Replace x with 0 or 1 below,
a1(0)
