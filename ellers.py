"""
Eller's Algorithm for Maze Generation 

Solomon Bothwell

Based on examples from "Mazes For Programmers" by Jamis Buck

1. Add the first row of the maze into a disjoint set.
2. Randomly union and link adjacent cells in the row set if
   they are not already in the same set.
3. Choose atleast one cell from each set to union and link
   with its southern neighbor. 
4. Repeat for each subsequent row.
"""
from typing import Any, Callable
from random import randint, shuffle
from functools import reduce
from grid import Grid


def pick_random(arr: list) -> Any:
    """ Return a random element from an array """
    return arr[randint(0, len(arr) - 1)]


def ellers(grid: Grid) -> None:
    D = disjoint_set()
    for row in grid.grid:
        for cell in row:
            D.make_set(cell) 
        for i, cell in enumerate(row[:-1]):
            join = randint(0, 1)
            x = D.find(row[i])
            y = D.find(row[i+1])
            if x != y and (not join or not cell.south):
                D.union(row[i], row[i+1])
                row[i].link(row[i+1])
        if cell.south:
            sets = D.sets()
            for sett in sets:
                shuffle(sett)
                for i, cell in enumerate(sett):
                    if not i or not randint(0, 5):
                        south = cell.south
                        cell.link(south)
                        D.make_set(south)
                        D.union(cell, south)
                        

class disjoint_set(object):
    def __init__(self):
        self.partitions_count = 0
        self.size = {}
        self.parent = {}

    def get_set(self, element):
        """ Super slow way to return a full set """
        parent = self.find(element)
        result = []
        for key, value in self.parent.items():
            if self.find(key) == parent:
                result.append(key)
        return result

    def sets(self):
        """ Super slow returns all the sets as nested lists """
        result = []
        for parent in self.parent.values():
            s = self.get_set(parent)
            if s not in result:
                result.append(s)
        return result

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
    g = Grid(10,10)

    ellers(g)
    g.pretty_print()
