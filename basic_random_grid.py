import numpy as np

class RandomGrid:
    def __init__(self, input_pattern, output_shape):
        self.input_pattern = input_pattern
        self.output_shape = output_shape
        self.output_pattern = np.zeros(output_shape, dtype=int)

    def init_grid(self, random=True):
        # Iterating over each position in the output pattern
        
        for i in range(self.output_shape[0]):
            for j in range(self.output_shape[1]):
                # Select a random tile from the input pattern as the initial state
                if random:
                    tile_index = np.random.choice(len(self.input_pattern))
                else:
                    tile_index = 0
                self.output_pattern[i, j] = self.input_pattern[tile_index]

    def print_output(self):
        for row in self.output_pattern:
            print(' '.join(str(val) for val in row))

if __name__ == '__main__':
    # Example input pattern (colors represented as integers)
    input_pattern = [0, 1, 2, 3]  # For simplicity, let's assume 4 different colors
    output_shape = (22, 18)  # Desired output shape

    random_grid = RandomGrid(input_pattern, output_shape)
    random_grid.init_grid()
    random_grid.print_output()