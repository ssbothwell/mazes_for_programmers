"""
Hunt and Kill Maze Generation Algorithm

Solomon Bothwell

Based on examples from "Mazes For Programmers" by Jamis Buck

1. Pick a random cell to start.
2. Perform a random walk avoiding visited cells.
3. If the walk ends surrouned by visited cells,
   Scan the graph from the upper left corner, until
   you find an unvisited cell that has at least one
   visited neighbor.
4. Perfom a random walk from here.
5. Repeat until all cells have been visited.

"""
from typing import Any
from collections import defaultdict
from random import randint
from grid import Grid


def pick_random(arr: list) -> Any:
    """ Return a random element from an array """
    return arr[randint(0, len(arr) - 1)]


def hunt_and_kill(grid: Grid) -> None:
    visited = defaultdict(bool)
    # Start with a random cell
    curr_cell = grid.random_cell()
    visited[curr_cell] = True
    while curr_cell:
        # All the unvisited neighbors of curr_cell
        neighbors = list(filter(lambda x: x != None and
                                visited[x] == False,
                                curr_cell.neighbors()))
        if neighbors:
            next_cell = pick_random(neighbors)
            curr_cell.link(next_cell)
            curr_cell = next_cell
            visited[curr_cell] = True
        else:
            curr_cell = None
            for cell in grid.cells():
                if not visited[cell]:
                    # All the visited neighbors of cell
                    neighbors = [ x for x in cell.neighbors() if
                                  x != None and visited[x] == True ]
                    if neighbors:
                        curr_cell = cell
                        next_cell = pick_random(neighbors)
                        curr_cell.link(next_cell)
                        visited[curr_cell] = True
                        break


                    #print(randint(0, 99999))
if __name__ == "__main__":
    g = Grid(14,14)
    hunt_and_kill(g)
    g.pretty_print()

