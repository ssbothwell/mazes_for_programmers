"""
Sidewinder Maze Generation Algorithm

Solomon Bothwell

Based on examples from "Mazes For Programmers" by Jamis Buck
"""
from typing import Any
from random import randint
from grid import Grid


def pick_random(arr: list) -> Any:
    """ Return a random element from an array """
    return arr[randint(0, len(arr) - 1)]


def sidewinder(grid: Grid) -> None:
    for cell in reversed(grid):
        run = []
        run.append(cell)
        choice = randint(0, 1)
        if ((choice == 1 and cell.north is not None) or 
            cell.east is None):
            close_out = True
            run_choice = pick_random(run) 
            if run_choice.north:
                run_choice.link(run_choice.north)
            run = []
        else:
            cell.link(cell.east)

if __name__ == "__main__":
    g = Grid(4,4)
    sidewinder(g)
    g.pretty_print()

