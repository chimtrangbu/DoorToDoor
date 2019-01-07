from math import sqrt
from sys import argv


class Node(object):
    """
    each Node object holding each city's coordinates
    cal_distance: calculating distance between this Node and another Node
    """

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def cal_distance(self, another_node):
        return sqrt((self.x - another_node.x) ** 2 +
                    (self.y - another_node.y) ** 2)


class Graph(object):
    """
    Graph object holding list of nodes
    """
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)
        return self.nodes

    def nearest_neighbor(self, start=None):
        if start is None:
            start = self.nodes[0]
        must_visit = self.nodes.copy()
        path = [start]
        must_visit.remove(start)
        while must_visit:
            # finding the nearest city from the last in passed-cities
            nearest = must_visit[0]
            cur_node = path[-1]
            min_dist = cur_node.cal_distance(nearest)
            for node in must_visit:
                if cur_node.cal_distance(node) < min_dist:
                    nearest = node
                    min_dist = cur_node.cal_distance(node)
            path.append(nearest)
            must_visit.remove(nearest)
        return path

    def find_shortest_path(self):
        self.nodes = self.nearest_neighbor()
        return self.nodes

    def show_graph(self):
        print(' -> '.join([node.name for node in self.nodes]))


def length_road(nodes):
    total = 0
    for i in range(len(nodes) - 1):
        total += nodes[i].cal_distance(nodes[i + 1])
    return total


def main():
    import time
    now = time.time()
    graph = Graph()
    f = open(argv[1], 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        info = line.split(', ')
        graph.add_node(Node(info[0], float(info[1]), float(info[2])))
    graph.find_shortest_path()
    graph.show_graph()
    print('length of path:', length_road(graph.nodes))
    print('time:', time.time() - now)


if __name__ == '__main__':
    main()
