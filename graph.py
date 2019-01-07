from abc import ABC, abstractmethod


def length_road(nodes):
    total = 0
    for i in range(len(nodes)-1):
        total += nodes[i].cal_distance(nodes[i+1])
    return total


class Graph(ABC):
    """
    Graph object holding list of nodes
    """
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)
        return self.nodes

    @abstractmethod
    def find_shortest_path(self, key):
        pass

    def show_graph(self):
        print(' -> '.join([node.name for node in self.nodes]))
