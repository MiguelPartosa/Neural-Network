import numpy as np
from neuronClass import Neuron

class Network:
    """
    A neural network with:
    - 2 inputs
    - a hidden layer with 2 neurons(hidden_layer1, hidden_layer2)
        - They have the same weights [0,1] and bias 0 
    - an output layer with 1 neuron(output_layer)

    """

    def __init__(self):
        # adding more arguments here will allow us to make our own weights and biases
        training_weights = np.array([0, 1])
        training_bias = 0

        self.hidden_layer1 = Neuron(training_weights, training_bias)
        self.hidden_layer2 = Neuron(training_weights, training_bias)
        self.output_layer = Neuron(training_weights, training_bias)

    def feedforwardNetwork(self, input):
        # We record the two outputs from the hidden layer to feedforward to make one output layer node
        from_hidden1 = self.hidden_layer1.feedforward(input)
        from_hidden2 = self.hidden_layer2.feedforward(input)

        from_outputlayer = self.output_layer.feedforward(
            np.array([from_hidden1, from_hidden2]))

        return from_outputlayer


if __name__ == '__main__':
    my_network = Network()
    input = np.array([2, 3])
    print("Output: ", my_network.feedforwardNetwork(input))
