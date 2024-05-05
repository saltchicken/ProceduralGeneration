import numpy as np

class WaveFunctionCollapse:
    def __init__(self, input_pattern, output_shape):
        self.input_pattern = input_pattern
        self.output_shape = output_shape
        self.output_pattern = np.zeros(output_shape, dtype=int)

    def collapse(self):
        # Iterating over each position in the output pattern
        for i in range(self.output_shape[0]):
            for j in range(self.output_shape[1]):
                # Select a random tile from the input pattern as the initial state
                tile_index = np.random.choice(len(self.input_pattern))
                self.output_pattern[i, j] = self.input_pattern[tile_index]

    def print_output(self):
        for row in self.output_pattern:
            print(' '.join(str(val) for val in row))

# Example input pattern (colors represented as integers)
input_pattern = [0, 1, 2, 3]  # For simplicity, let's assume 4 different colors
output_shape = (5, 5)  # Desired output shape

# Creating a WaveFunctionCollapse instance
wfc = WaveFunctionCollapse(input_pattern, output_shape)

# Generating the output pattern
wfc.collapse()

# Printing the output pattern
wfc.print_output()
