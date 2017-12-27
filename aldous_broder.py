"""
Aldous Broder Maze Generation Algorithm

Solomon Bothwell

Based on examples from "Mazes For Programmers" by Jamis Buck

Start anywhere in the grid.
Choose a random neighbor.
Move to that neighbor.
If it hasn't been visited then link it to the prior cell.
Repeat until all cells have been visited.
"""
from collections import defaultdict
from random import randint
from grid import Grid


def aldous_broder(grid: Grid) -> Grid:
    visited = defaultdict(bool)
    unvisited = len(grid) - 1
    curr_cell = grid.random_cell()
    while unvisited > 0:
        neighbors = list(filter(lambda x: x != None, curr_cell.neighbors()))
        index = randint(0, len(neighbors) -1)
        next_cell = neighbors[index]

        if not visited[next_cell]:
            curr_cell.link(next_cell)
            visited[next_cell] = True
            unvisited -= 1
        curr_cell = next_cell

        


if __name__ == "__main__":
    g = Grid(10,10)
    aldous_broder(g)
    g.pretty_print()

