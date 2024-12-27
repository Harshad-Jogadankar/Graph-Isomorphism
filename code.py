import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations

def are_isomorphic(incidence_matrix1, incidence_matrix2):
    # Check if dimensions match
    if incidence_matrix1.shape != incidence_matrix2.shape:
        return False

    # Generate all row permutations
    n = incidence_matrix1.shape[0]
    for perm in permutations(range(n)):
        permuted_matrix = incidence_matrix1[list(perm), :]
        if np.array_equal(permuted_matrix, incidence_matrix2):
            return True

    return False

def plot_graph_from_incidence_matrix(incidence_matrix, title):
    # Create a graph from the incidence matrix
    G = nx.Graph()
    num_edges = incidence_matrix.shape[1]

    for edge in range(num_edges):
        vertices = np.where(incidence_matrix[:, edge] == 1)[0]
        if len(vertices) == 2:  # Valid edge between two vertices
            G.add_edge(vertices[0], vertices[1])

    # Draw the graph
    pos = nx.spring_layout(G)  # Layout for better visualization
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=12)
    plt.title(title)
    plt.show()

# Input: Incidence matrices of two graphs
print("Enter the incidence matrix for Graph 1 (rows x columns, space-separated):")
inc1 = np.array([list(map(int, input().split())) for _ in range(int(input("Enter the number of rows for Graph 1: ")))])
print("\nEnter the incidence matrix for Graph 2 (rows x columns, space-separated):")
inc2 = np.array([list(map(int, input().split())) for _ in range(int(input("Enter the number of rows for Graph 2: ")))])

# Check for isomorphism
isomorphic = are_isomorphic(inc1, inc2)
print("\nThe graphs are", "isomorphic" if isomorphic else "not isomorphic")

# Visualize both graphs
plot_graph_from_incidence_matrix(inc1, "Graph 1")
plot_graph_from_incidence_matrix(inc2, "Graph 2")
