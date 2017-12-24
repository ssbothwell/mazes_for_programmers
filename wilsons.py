"""
Wilson's Maze Generation Algorithm

Solomon Bothwell

Based on examples from "Mazes For Programmers" by Jamis Buck

Start by marking a random cell as visited.
Choose a random unvisited cell.

"""
from collections import defaultdict
from random import randint
from grid import Grid


def wilson(grid: Grid) -> Grid:
    visited = defaultdict(bool)
    visited[grid.random_cell()] = True

    def pick_new(grid: Grid, visited: defaultdict, unvisited: int):
        """ Recursively find an unvisted cell """
        cell = grid.random_cell()
        if not visited[cell]:
            return cell
        else:
            return pick_new(grid, visited)



if __name__ == "__main__":
    g = Grid(14,14)
    wilson(g)
    g.pretty_print()

