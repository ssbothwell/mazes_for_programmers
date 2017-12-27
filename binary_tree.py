"""
Binary Tree Maze Generation Algorithm

Solomon Bothwell

Based on examples from "Mazes For Programmers" by Jamis Buck
"""
from typing import Any
from random import randint
from grid import Grid


def pick_random(arr: list) -> Any:
    """ Return a random element from an array """
    return arr[randint(0, len(arr) - 1)]


def binary_tree(grid: Grid) -> None:
    for cell in reversed(grid):
        neighbors = list(filter(lambda x: x != None, [cell.north, cell.east]))
        if neighbors:
            neighbor = pick_random(neighbors)
            cell.link(neighbor)


if __name__ == "__main__":
    g = Grid(4,4)
    binary_tree(g)
    g.pretty_print()

