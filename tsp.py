#!/usr/bin/env python3

import sys
from node import Node
import argparse
from algos import *


def parse_input():
    parser = argparse.ArgumentParser(conflict_handler='resolve')
    parser.add_argument('--algo', action='store', default='nearest_neighbor',
                        type=str, help='specify which algorithm to use for '
                                       'finding path among [nearest_neighbor|'
                                       'random_insertion|two_opt]')
    parser.add_argument('filename', action='store', default='wrong name',
                        type=str, help='take a filename containing list of '
                                       'cities to visit')
    args = parser.parse_args()
    if args.algo not in ['nearest_neighbor', 'random_insertion', 'two_opt']:
        parser.print_help(sys.stderr)
        exit(1)
    return args


def main():
    from time import time
    now = time()
    args = parse_input()
    algo = args.algo
    file_name = args.filename

    if algo == 'random_insertion':
        graph = RandomInsertion()
    else:
        graph = NearestNeighbor()

    try:
        f = open(file_name, 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            info = line.split(', ')
            graph.add_node(Node(info[0], float(info[1]), float(info[2])))
    except Exception:
        print('Invalid file')
        exit(1)

    graph.find_shortest_path()
    if algo == 'two_opt':
        two_opt_graph = TwoOpt()
        two_opt_graph.find_shortest_path(graph.nodes)
        graph = two_opt_graph

    graph.show_graph()
    print('length of path:', length_road(graph.nodes))
    print('time:', time()-now)


if __name__ == '__main__':
    main()
