from typing import Dict
from numba.typed import Dict as NumbaDict, List as NumbaList
from numba import int32
from models import Node, Edge  

class Graph:
    def __init__(self):
        # Using Numba's typed Dict and List for compatibility with Numba optimized functions
        # Key: node ID, Value: Node instance
        self.nodes = NumbaDict.empty(
            key_type=int32,
            value_type=Node.class_type.instance_type
        )
        # List of Edge instances
        self.edges = NumbaList.empty_list(Edge.class_type.instance_type)

    def add_node(self, node: Node):
        """Add a Node to the graph."""
        self.nodes[node.id] = node

    def add_edge(self, edge: Edge):
        """Add an Edge to the graph. Assumes nodes already exist in the graph."""
        self.edges.append(edge)
        # You might also want to update the Node instances to include edge information
        # depending on how you plan to traverse the graph

    def get_node(self, node_id: int) -> Node:
        """Retrieve a node by its ID."""
        return self.nodes.get(node_id, None)

