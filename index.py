from neuralNetwork import *

input_nodes = 3
hidden_nodes = 3
output_nodes = 3

learning_rate = 0.3

network = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

print(network.query([1.0, 0.5, -1.5]))
