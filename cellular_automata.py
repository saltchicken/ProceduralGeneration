import numpy as np
import matplotlib.pyplot as plt

def apply_rule(rule, left, center, right):
    """
    Apply the rule to determine the state of the center cell based on its neighbors.
    """
    return rule[(left, center, right)]

def generate_ca(rule, size):
    """
    Generate a one-dimensional cellular automaton using the given rule and size.
    """
    # Initialize the grid with zeros and set the center cell to 1.
    ca = np.zeros((size, size), dtype=int)
    ca[0, size // 2] = 1

    # Generate subsequent rows based on the rule.
    for i in range(1, size):
        for j in range(1, size - 1):
            left = ca[i-1, j-1]
            center = ca[i-1, j]
            right = ca[i-1, j+1]
            ca[i, j] = apply_rule(rule, left, center, right)

    return ca

def visualize_ca(ca):
    """
    Visualize the cellular automaton grid.
    """
    plt.imshow(ca, cmap='binary', interpolation='nearest')
    plt.show()

def main():
    # Define the size of the grid and the rule (Rule 30).
    size = 100
    rule = { (1, 1, 1): 0, (1, 1, 0): 0, (1, 0, 1): 0, (1, 0, 0): 1, 
             (0, 1, 1): 1, (0, 1, 0): 1, (0, 0, 1): 1, (0, 0, 0): 0 }

    # Generate the cellular automaton.
    ca = generate_ca(rule, size)

    # Visualize the cellular automaton.
    visualize_ca(ca)

if __name__ == "__main__":
    main()
