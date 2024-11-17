#! /usr/bin/env python
from itertools import permutations

class Node:
    def __init__(self, x, y, size, used, avail):
        self.x = x
        self.y = y
        self.size = size
        self.used = used
        if size - used != avail:
            raise "Size isn't right"
        self.avail = avail

    def is_same_node(self, b):
        return self.x == b.x and self.y == b.y

    @staticmethod
    def is_variable_pair(a, b):
        if a.used == 0:
            return False
        if a.is_same_node(b):
            return False
        return a.used <= b.avail


def main():
    nodes = []

    with open('sample.txt', 'r') as f:
        df = f.read().splitlines()[2:]

    for n in df:
        x, y = (n[15:24].split('-')[i].strip()[1:] for i in (0, 1))
        size = int(n[24:27])
        used = int(n[30:33])
        avail = int(n[35:40])

        nodes.append(Node(x, y, size, used, avail))

    pairs = [p for p in permutations(nodes, 2) if Node.is_variable_pair(p[0], p[1])]
    print(len(pairs))

if __name__ == '__main__':
    main()
