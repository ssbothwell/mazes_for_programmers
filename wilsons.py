"""
Wilson's Maze Generation Algorithm

Solomon Bothwell

Based on examples from "Mazes For Programmers" by Jamis Buck

Start by marking a random cell as visited.
Choose a random unvisited cell.
perform a 'loop erased randomized walk` until it
encounters a visited cell.
mark all cells from the walk as visited.
repeat until all cells are visited.

"""
from operator import indexOf
from collections import defaultdict
from typing import Any
from random import randint
from grid import Grid

def pick_random(arr: list) -> Any:
    """ Return a random element from an array """
    return arr[randint(0, len(arr) - 1)]


def wilson(grid: Grid) -> Grid:
    unvisited = []
    for row in grid.grid:
        for cell in row:
            unvisited.append(cell)
    
    starting_cell = pick_random(unvisited)
    unvisited.remove(starting_cell)

    while unvisited:
        cell = pick_random(unvisited)
        path = [cell]

        cell = pick_random(unvisited)
        start = cell
        path = [cell]
        while cell in unvisited:
            cell = pick_random(cell.neighbors())
            if cell in path:
                cell = start
                path = [cell] 
                continue
            else:
                path.append(cell)
        for i, cell in enumerate(path[:-1]):
            cell.link(path[i+1])
            unvisited.remove(cell)


if __name__ == "__main__":
    g = Grid(14,14)
    wilson(g)
    g.pretty_print()

