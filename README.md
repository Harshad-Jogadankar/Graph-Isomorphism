# Graph Isomorphism Checker

This Python script checks whether two graphs are isomorphic using their incidence matrices and visualizes the graphs side-by-side.

## Features
- Verifies graph isomorphism by comparing all permutations of the rows of incidence matrices.
- Visualizes both graphs using `matplotlib` and `networkx`.

## Requirements
- Python 3.6+
- Libraries: `numpy`, `networkx`, `matplotlib`

## Usage
1. Run the script and input the incidence matrices for two graphs.
2. The script will display:
   - Whether the graphs are isomorphic.
   - Visualizations of both graphs.

```bash
pip install numpy networkx matplotlib
python graph_isomorphism.py
```

## Input Format
- Enter the number of rows for each graph.
- Input each row of the incidence matrix as space-separated integers.

## Example
Graph 1:
```
1 0 1
0 1 1
1 1 0
```
Graph 2:
```
0 1 1
1 0 1
1 1 0
```

Output:
```
The graphs are isomorphic
```

## Visualization
Displays both graphs for easy comparison.
