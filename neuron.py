import numpy as np


def sigmoid(x):
    """
    Our activation function: f(x) = 1 / (1 + e^(-x))
    """
    return (1/(1+np.exp(-x)))


class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        """
        Doing our little dot product: (w*x) + b 
        """
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)
        # feedforward -> activation function


weights = np.array([0, 1])  # w1 = 0, w2 = 1
bias = 4                   # b = 4
n = Neuron(weights, bias)

x = np.array([2, 3])

print(n.feedforward(x))
