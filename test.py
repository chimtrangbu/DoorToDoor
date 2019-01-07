from math import sqrt
from sys import argv


class Node():
    '''
    each Node object holding each city's coordinates
    cal_distance: calculating distance between this Node and another Node
    '''

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def cal_distance(self, another_node):
        return sqrt((self.x - another_node.x) ** 2 +
                    (self.y - another_node.y) ** 2)


class Graph(object):
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
            nearest = must_visit[0]
            cur_node = path[-1]
            min_dist = cur_node.cal_distance(nearest)
            for node in must_visit:
                if cur_node.cal_distance(node) < min_dist:
                    nearest = node
                    min_dist = cur_node.cal_distance(node)
            # nearest = min(must_visit, key=lambda k: path[-1].cal_distance(k))
            path.append(nearest)
            must_visit.remove(nearest)
        return path

    def random_insertion(self, start=None):
        if start is None:
            start = self.nodes[0]
        must_visit = self.nodes.copy()
        path = [start]
        must_visit.remove(start)
        while must_visit:
            # nearest = min(must_visit, key=lambda k: path[-1].cal_distance(k))
            import random
            nearest = must_visit[random.randint(0, len(must_visit) - 1)]
            pos = min(path, key=lambda k: nearest.cal_distance(k))
            pos_index = path.index(pos)
            if pos_index == 0:
                pos_insert = pos_index + 1
            elif pos_index == len(path) - 1:
                case_insert_after = length_road([path[-2], path[-1], nearest])
                case_insert_before = length_road([path[-2], nearest, path[-1]])
                if case_insert_after > case_insert_before:
                    pos_insert = pos_index
                else:
                    pos_insert = pos_index + 1
            else:
                last_node = path[pos_index - 1]
                next_node = path[pos_index + 1]
                case_insert_before = length_road(
                    [last_node, nearest, pos, next_node])
                case_insert_after = length_road(
                    [last_node, pos, nearest, next_node])
                if case_insert_after > case_insert_before:
                    pos_insert = pos_index
                else:
                    pos_insert = pos_index + 1
            path.insert(pos_insert, nearest)
            must_visit.remove(nearest)
        return path

    @staticmethod
    def two_opt(route):
        best = route
        improved = True
        while improved:
            improved = False
            for i in range(1, len(route) - 2):
                for j in range(i + 1, len(route)):
                    if j - i == 1:
                        continue  # changes nothing, skip then
                    new_route = route[:]
                    new_route[i:j] = route[
                                     j - 1:i - 1:-1]  # this is the 2woptSwap
                    if length_road(new_route) < length_road(best):
                        best = new_route
                        improved = True
            route = best
        return best

    def find_shortest_path(self, key='nearest_neighbor'):
        if key == 'nearest_neighbor':
            self.nodes = self.nearest_neighbor()
        elif key == 'random_insertion':
            shortest_path = self.random_insertion()
            for i in range(10):
                random_path = self.random_insertion()
                if length_road(random_path) < length_road(shortest_path):
                    shortest_path = random_path
            self.nodes = shortest_path
        elif key == 'two_opt':
            self.nodes = self.two_opt(self.nearest_neighbor())
        return self.nodes

    def show_graph(self):
        print(' -> '.join([node.name for node in self.nodes]))


def length_road(nodes):
    sum = 0
    for i in range(len(nodes) - 1):
        sum += nodes[i].cal_distance(nodes[i + 1])
    return sum


def main():
    map = Graph()
    f = open(argv[1], 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        info = line.split(', ')
        map.add_node(Node(info[0], float(info[1]), float(info[2])))
    map.find_shortest_path()
    map.show_graph()
    print('length of path:', length_road(map.nodes))


if __name__ == '__main__':
    import time

    now = time.time()
    main()
    print('time:', time.time() - now)
