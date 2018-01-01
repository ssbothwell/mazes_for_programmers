"""
Simplified Prim's Algorithm for Maze Generation 

Solomon Bothwell

Based on examples from "Mazes For Programmers" by Jamis Buck

1. Pick a random starting cell and add it to a set.
2. Pick a random unvisted cell neighboring the set.
3. Add it to the set and link it to it's neighbor in the set.
4. Repeat 2 and 3 until all cells are in the set.
"""
from typing import Any, Set
from random import randint
from grid import Grid


def pick_random(arr: list) -> Any:
    """ Return a random element from an array """
    return arr[randint(0, len(arr) - 1)]


def prims(grid: Grid) -> None:
    stack = [grid.random_cell()]
    
    while stack:
        cell = pick_random(stack)
        neighbors = [ x for x in cell.neighbors() if not x.visited ]
        
        if neighbors:
            neighbor = pick_random(neighbors)
            cell.link(neighbor)
            stack.append(neighbor)
        else:
            stack.remove(cell)


if __name__ == "__main__":
    g = Grid(14,14)
    prims(g)
    g.pretty_print()
