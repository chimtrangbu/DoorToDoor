from math import sqrt


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
