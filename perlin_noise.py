import numpy as np
import noise
import matplotlib.pyplot as plt

def generate_perlin_noise(width, height, scale=100.0, octaves=6, persistence=0.5, lacunarity=2.0, seed=None):
    perlin_noise = np.zeros((height, width))
    for y in range(height):
        for x in range(width):
            perlin_noise[y][x] = noise.pnoise2(x/scale,
                                                y/scale,
                                                octaves=octaves,
                                                persistence=persistence,
                                                lacunarity=lacunarity,
                                                repeatx=1024,
                                                repeaty=1024,
                                                base=seed)
    return perlin_noise

def display_noise(noise_map):
    plt.imshow(noise_map, cmap='gray', interpolation='nearest')
    plt.colorbar()
    plt.show()
# Generate Perlin noise
width = 512
height = 512
scale = 100.0
octaves = 6
persistence = 0.5
lacunarity = 2.0
seed = np.random.randint(0, 100)
noise_map = generate_perlin_noise(width, height, scale, octaves, persistence, lacunarity, seed)

# Display the generated noise map
display_noise(noise_map)
