"""
Randomized Kruskals Maze Generation Algorithm

Solomon Bothwell

Based on examples from "Mazes For Programmers" by Jamis Buck

1. Assign each cell to its own Set.
2. Choose two adjancent nodes at random.
3. If they are part of two distinct sets, merge them.
4. Repeat 2 and 3 until only a single set remains.
"""
from typing import Any, Set
from collections import defaultdict
from random import randint
from grid import Grid


def pick_random(arr: list) -> Any:
    """ Return a random element from an array """
    return arr[randint(0, len(arr) - 1)]


def kruskals(grid: Grid) -> None:
    edges = create_edges(grid)
    D = disjoint_set()
    for edge in edges:
        D.make_set(edge[0])
        D.make_set(edge[1])
    while edges:
        edge = pick_random(edges)
        edges.remove(edge)
        x = D.find(edge[0])
        y = D.find(edge[1])
        if x != y:
            edge[0].link(edge[1])
            D.union(x,y)


def create_edges(grid: Grid) -> list:
    result = []
    for cell in grid:
        for neighbor in cell.neighbors():
            if cell.east == neighbor or cell.south == neighbor:
                result.append((cell, neighbor))
    return result


class disjoint_set(object):
    def __init__(self):
        self.partitions_count = 0
        self.size = {}
        self.parent = {}

    def make_set(self, element):
        if self.find(element) == False:
            self.parent[element] = element
            self.size[element] = 1
            self.partitions_count += 1

    def union(self, x, y):
        xParent = self.find(x)
        yParent = self.find(y)
        if xParent != yParent:
            if self.size[xParent] < self.size[yParent]:
                self.parent[xParent] = yParent
                self.size[yParent] += self.size[xParent]
                self.partitions_count -= 1
            else:
                self.parent[yParent] = xParent
                self.size[xParent] += self.size[yParent]
                self.partitions_count -= 1

    def find(self, element):
        if element in self.parent:
            if element == self.parent[element]:
                return element
            root = self.parent[element]
            while self.parent[root] != root:
                root = self.find(self.parent[root])
            self.parent[element] = root
            return root
        return False
    


if __name__ == "__main__":
    g = Grid(14,14)
    kruskals(g)
    g.pretty_print()

