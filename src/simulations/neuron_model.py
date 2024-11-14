import physx

class Neuron:
    def __init__(self, location, resting_potential=-70):
        self.location = location
        self.potential = resting_potential
        self.threshold = -55  # Action potential threshold

    def stimulate(self, input_signal):
        """Simulate input to the neuron."""
        self.potential += input_signal
        if self.potential >= self.threshold:
            self.fire_action_potential()

    def fire_action_potential(self):
        """Simulate action potential firing."""
        print("Action potential fired!")
        self.potential = -70  # Reset to resting potential

# Example usage
neuron = Neuron(location=(0, 0, 0))
neuron.stimulate(20)  # Test stimulation

