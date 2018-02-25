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


def divide(grid: Grid, row, col, height, width):
    # Base Case:
    if height <= 1 or width <= 1:
        return

    divide_vertically(grid, height)
    #divide_horizontally(grid, row, col, height, width)
    #if height > width:
    #    divide_horizontally(row, column, height, width)
    #else:
    #    divide_vertically(row, column, height, width)


def divide_vertically(grid: Grid, ystart: int = 0,
                      yend: int = 0) -> None:
    if yend <= 1 or ystart == yend:
        return
     
    wall = randint(ystart, yend)
    if wall == 0:
        return

    tunnel = grid.grid[wall][randint(0,grid.rows-1)]
    if wall != 0:
        for cell in grid.grid[wall]:
            cell.unlink(cell.north)
        tunnel.link(tunnel.north)

    # North Subgraph
    divide_vertically(grid, 0, wall)
    # South Subgraph
    divide_vertically(grid, wall, yend)
    

def divide_horizontally(grid: Grid, xstart: int = 0,
                        xend: int = 0) -> None:
    if xend <= 1 or xstart == xend:
        return
     
    wall = randint(xstart, xend)
    if wall == 0:
        return

    tunnel = grid.grid[randint(0,grid.cols-1)][wall]
    if wall != 0:
        for row in grid.grid:
            cell = row[wall]
            cell.unlink(cell.west)
        tunnel.link(tunnel.west)

    # West Subgraph
    divide_horizontally(grid, 0, wall)
    # East Subgraph
    divide_horizontally(grid, wall, xend)


if __name__ == "__main__":
    g = Grid(8,8)
    initialize_grid(g)
    g.pretty_print()
    divide_vertically(g, 0, 7)
    divide_horizontally(g, 0, 7)
    g.pretty_print()

