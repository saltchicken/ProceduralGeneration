import numpy as np

class WaveFunctionCollapse:
    def __init__(self, input_data, output_size, tile_size):
        self.input_data = input_data
        self.output_size = output_size
        self.tile_size = tile_size
        self.output_data = np.zeros(output_size, dtype=int)
        self.compatible_tiles = self.calculate_compatible_tiles()

    def calculate_compatible_tiles(self):
        compatible_tiles = np.ones((len(self.input_data), self.tile_size, self.tile_size, len(self.input_data)), dtype=bool)
        for tile1 in range(len(self.input_data)):
            for tile2 in range(len(self.input_data)):
                if tile1 != tile2:
                    for i in range(self.tile_size):
                        for j in range(self.tile_size):
                            match = False
                            for k in range(self.tile_size):
                                for l in range(self.tile_size):
                                    if self.input_data[tile1][i][j] == self.input_data[tile2][k][l]:
                                        match = True
                            if not match:
                                compatible_tiles[tile1, i, j, tile2] = False
        return compatible_tiles

    def generate_output(self):
        while np.min(self.output_data) == 0:
            min_entropy = float('inf')
            min_tile = None
            for x in range(self.output_size[0]):
                for y in range(self.output_size[1]):
                    if self.output_data[x, y] == 0:
                        entropy = np.sum(self.output_data[x, y] == 0)
                        if entropy == 0:
                            min_tile = np.random.choice(np.flatnonzero(self.output_data[x, y] == 0))
                            self.output_data[x, y] = min_tile + 1
                        elif entropy < min_entropy:
                            min_entropy = entropy
                            possible_tiles = np.flatnonzero(self.output_data[x, y] == 0)
                            min_tile = np.random.choice(possible_tiles)
                            self.output_data[x, y] = min_tile + 1
                        elif entropy == min_entropy:
                            possible_tiles = np.flatnonzero(self.output_data[x, y] == 0)
                            possible_tiles_min_entropy = possible_tiles
                            if len(possible_tiles) < len(possible_tiles_min_entropy):
                                
                                min_tile = np.random.choice(possible_tiles_min_entropy)
                                self.output_data[x, y] = min_tile + 1
            if min_tile is None:
                print("No solution")
                break

input_data = [
    [[0, 0], [1, 1]],
    [[1, 1], [0, 0]],
]

output_size = (4, 4)
tile_size = 2

wfc = WaveFunctionCollapse(input_data, output_size, tile_size)
wfc.generate_output()
print(wfc.output_data)

