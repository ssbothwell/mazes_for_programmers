"""
Aldous Broder Maze Generation Algorithm

Solomon Bothwell

Based on examples from "Mazes For Programmers" by Jamis Buck

1. Start anywhere in the grid.
2. Choose a random neighbor.
3. Move to that neighbor.
4. If it hasn't been visited then link it to the prior cell.
5. Repeat until all cells have been visited.
"""
from typing import Any, Iterable
from collections import defaultdict
from random import randint
from grid import Grid


def pick_random(arr: list) -> Any:
    """ Return a random element from an array """
    return arr[randint(0, len(arr) - 1)]


def aldous_broder(grid: Grid) -> None:
    visited = defaultdict(bool) # type: dict
    unvisited = len(grid) - 1
    curr_cell = grid.random_cell()
    while unvisited:
        neighbors = curr_cell.neighbors()
        next_cell = pick_random(neighbors)

        if not visited[next_cell]:
            curr_cell.link(next_cell)
            visited[next_cell] = True
            unvisited -= 1
        curr_cell = next_cell


if __name__ == "__main__":
    g = Grid(10,10)
    aldous_broder(g)
    g.pretty_print()

