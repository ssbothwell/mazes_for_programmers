"""
Prim's Algorithm for Maze Generation 

Solomon Bothwell

Based on examples from "Mazes For Programmers" by Jamis Buck

Prim's algorithm variation where weights are applied to
nodes rather then edges.

1. Assign each cell a random weight.
2. Pick a random starting cell and add it to the set V.
3. From the set of cells neighboring the set V, pick the
   one with the smallest weight.
4. Add it to the set V and link it to it's neighbor in the set.
5. Repeat 2 and 3 until all cells are in the set V.
"""
from typing import Any, Set
from random import randint
from functools import reduce
from grid import Grid


def pick_random(arr: list) -> Any:
    """ Return a random element from an array """
    return arr[randint(0, len(arr) - 1)]


def prims(grid: Grid) -> None:
    stack = [grid.random_cell()]
    weights = { cell: randint(0, 100) for cell in grid }
    while stack:
        cell = reduce(lambda x, y: x if weights[x] < weights[y] else y, stack)
        neighbors = [ x for x in cell.neighbors() if not x.visited ]
        
        if neighbors:
            neighbor = reduce(lambda x, y: x if weights[x] < weights[y] else y, neighbors)
            cell.link(neighbor)
            stack.append(neighbor)
        else:
            stack.remove(cell)


if __name__ == "__main__":
    g = Grid(10,10)
    prims(g)
    g.pretty_print()
