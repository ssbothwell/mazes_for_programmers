"""
Sidewinder Maze Generation Algorithm

Solomon Bothwell

Based on examples from "Mazes For Programmers" by Jamis Buck
"""
from random import randint
from grid import Grid


def sidewinder(grid: Grid) -> Grid:
    for row in reversed(grid.grid):
        run = []
        for cell in row:
            run.append(cell)
            choice = randint(0, 1)
            if ((choice == 1 and cell.north is not None) or 
                cell.east is None):
                close_out = True
                index = randint(0, len(run) - 1)
                run_choice = run[index]
                if run_choice.north:
                    run_choice.link(run_choice.north)
                run = []
            else:
                cell.link(cell.east)

if __name__ == "__main__":
    g = Grid(10,10)
    sidewinder(g)
    g.pretty_print()

