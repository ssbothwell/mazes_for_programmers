"""
Growing Tree Algorithm for Maze Generation 

Solomon Bothwell

Based on examples from "Mazes For Programmers" by Jamis Buck

A generalized version of Prim's algorithm which uses
arbitrary criteria functions to build the spanning tree.

1. Choose a cell at random and add it to the set V.
2. Select a cell C from set V using desired criteria.
3. Choose a random unvisited neighbor of cell C, link
   it to C and add it to the set V.
4. Repeat steps 2 and 3 until all cells have been linked.
"""
from typing import Any, Callable
from random import randint
from functools import reduce
from grid import Grid


def pick_random(arr: list) -> Any:
    """ Return a random element from an array """
    return arr[randint(0, len(arr) - 1)]


def growing_tree(grid: Grid, criteria: Callable) -> None:
    stack = [grid.random_cell()]
    weights = { cell: randint(0, 100) for cell in grid }
    while stack:
        cell = criteria(stack)
        neighbors = [ x for x in cell.neighbors() if not x.visited ]
        
        if neighbors:
            neighbor = pick_random(neighbors)
            cell.link(neighbor)
            stack.append(neighbor)
        else:
            stack.remove(cell)


if __name__ == "__main__":
    random = lambda x: pick_random(x)
    last = lambda x: x[-1]
    g = Grid(10,10)

    growing_tree(g, last)
    g.pretty_print()
