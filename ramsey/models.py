import numpy as np
from numba import int32, float32
from numba.experimental import jitclass

# Specifying the structure for Numba's jitclass
node_spec = [
    ('id', int32),
    ('properties', float32[:]),  # Assuming properties is a 1D array of floats
]

@jitclass(node_spec)
class Node:
    def __init__(self, id: int, properties: np.ndarray):
        self.id = id
        self.properties = properties

edge_spec = [
    ('source', int32),
    ('target', int32),
    ('weight', float32),
]

@jitclass(edge_spec)
class Edge:
    def __init__(self, source: int, target: int, weight: float):
        self.source = source
        self.target = target
        self.weight = weight
