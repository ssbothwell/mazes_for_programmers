"""
Recursive Backtracker Maze Generation Algorithm

Solomon Bothwell

Based on examples from "Mazes For Programmers" by Jamis Buck

1. Pick a random cell to start.
2. Perform a random walk avoiding visited cells.
3. If the walk ends surrouned by visited cells,
   walk back through visited cells until you 
   find a cell with unvisited neighbors.
4. Perfom a random walk from here.
5. Repeat until all cells have been visited.

"""
from typing import Any
from random import randint
from functools import reduce
from grid import Grid


def pick_random(arr: list) -> Any:
    """ Return a random element from an array """
    return arr[randint(0, len(arr) - 1)]


def recursive_backtracker(grid: Grid) -> None:
    cell = grid.random_cell()
    stack = [cell]
    while stack:
        cell = stack[-1]
        nor = lambda x, y: not (x or y)
        neighbors = [ x for x in cell.neighbors() if
                      not x.visited ]  

        if neighbors:
            next_cell = pick_random(neighbors)
            cell.link(next_cell)
            stack.append(next_cell)
        else:
            stack.pop()


if __name__ == "__main__":
    g = Grid(14,14)
    recursive_backtracker(g)
    g.pretty_print()

