"""
Sidewinder Maze Generation Algorithm

Solomon Bothwell

Based on examples from "Mazes For Programmers" by Jamis Buck
"""
from random import randint
from grid import Grid


def sidewinder(grid: Grid) -> Grid:
    for row in grid.grid:
        for cell in row:
            neighbors = list(filter(lambda x: x != None, [cell.north, cell.east]))
            if neighbors:
                index = randint(0, len(neighbors) -1)
                neighbor = neighbors[index]
                cell.link(neighbor)

if __name__ == "__main__":
    g = Grid(4,4)
    binary_tree(g)
    g.pretty_print()

