"""
Recursive Division Algorithm for Maze Generation 

Solomon Bothwell

Based on examples from "Mazes For Programmers" by Jamis Buck

1. Initialize a grid with all neighbors connected (no walls).
2. Divide the grid into two sub grids with a wall between
   and one opening.
3. Repeat step two recurisvely on each subgrid.
"""
from random import randint, shuffle
from grid import Grid


def initialize_grid(grid: Grid) -> None:
    for cell in grid:
        for neighbor in cell.neighbors():
            cell.link(neighbor)


def divide(grid: Grid, xstart, xend, ystart, yend):
    # Base Case:
    if (xend - xstart < 2
        or yend - ystart < 2):
        return
    
    if yend > xend:
        # taller then wide
        wall = randint(ystart, yend)
        draw_horizontal(grid, xstart, xend-1, wall)
        tunnel(grid, wall, randint(xstart, xend-1), True)
        divide(grid, xstart, xend, ystart, wall)
        divide(grid, xstart, xend, wall, yend)

    else:
        # wider then tall
        wall = randint(xstart, xend)
        draw_vertical(grid, ystart, yend-1, wall)
        tunnel(grid, wall, randint(ystart, yend-1), False)
        divide(grid, xstart, wall, ystart, yend)
        divide(grid, wall, xend, ystart, yend)

def tunnel(grid: Grid, row: int, col: int, north: bool) -> None:
    cell = grid.grid[row][col]
    if north and cell.north:
        cell.link(cell.north)
    if not north and cell.west:
        cell.link(cell.west)


def draw_horizontal(grid: Grid, xstart: int,
                    xend: int, row: int) -> None:
    for cell in grid.grid[row][xstart:xend+1]:
        if not cell.north:
            break
        cell.unlink(cell.north)


def draw_vertical(grid: Grid, ystart: int,
                    yend: int, col: int) -> None:
    for row in grid.grid[ystart:yend+1]:
        cell = row[col]
        if cell.west:
            cell.unlink(cell.west)


if __name__ == "__main__":
    g = Grid(8,8)
    initialize_grid(g)
    divide(g, 0, 7, 0, 7)
    #divide_vertically(g, 0, 7)
    #divide_horizontally(g, 0, 7)
    g.pretty_print()

