import numpy as np

class NeuralCircuit:
    def __init__(self, num_neurons):
        self.weights = np.random.rand(num_neurons, num_neurons) * 0.1
        self.activity = np.zeros(num_neurons)

    def stimulate(self, neuron_index, intensity):
        """Stimulate a neuron and propagate the signal."""
        self.activity[neuron_index] = intensity
        self.propagate()

    def propagate(self):
        """Propagate signal through the network."""
        self.activity = np.dot(self.weights, self.activity)
        print("Neural activity:", self.activity)

# Example usage
circuit = NeuralCircuit(num_neurons=10)
circuit.stimulate(0, 1.0)

