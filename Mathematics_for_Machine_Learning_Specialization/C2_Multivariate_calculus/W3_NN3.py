# link : https://www.coursera.org/learn/multivariate-calculus-machine-learning/quiz/NrGhK/training-neural-networks/attempt?redirectToCover=true
# ques 1
import numpy as np
# First we set the state of the network

σ = np.tanh
w1 = 1.3
b1 = -0.1

# Then we define the neuron activation.


def a1(a0):
    z = w1 * a0 + b1
    return σ(z)


# Experiment with different values of x below.
x = 0
y = a1(x)
print(a1(x))
cost = (y - 1)**2
print(cost)
