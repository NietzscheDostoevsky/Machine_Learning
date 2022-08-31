# Simple Artificial Neural Networks _ Coursera

# First we set the state of the network
import numpy as np
σ = np.tanh
w1 = 1.3
b1 = -0.1

# Then we define the neuron activation.


def a1(a0, w1, b1):
    return σ(w1 * a0 + b1)


# Finally let's try the network out!
# Replace x with 0 or 1 below,
w_b = [(10, 0), (0, 5), (3, 1), (-3, 0), (-5, 5)]

for w, b in w_b:
    print(w, b)
    for i in range(2):
        print("a1 : ", i)
        print("w : ", w, "b : ", b)
        print(a1(i, w, b))
        print("-----------")
        print("\n")
