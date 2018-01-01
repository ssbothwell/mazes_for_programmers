"""
Grid Class for maze graphs
"""
from typing import List, Iterable, Iterator
from cell import Cell
from random import randint

class Grid(Iterable):
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(r, c) for c in range(self.cols)] for r in range(self.rows)]
        self.configure_cells()


    def configure_cells(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if row > 0:
                    self.grid[row][col].north = self.grid[row - 1][col]
                if row < self.rows - 1:
                    self.grid[row][col].south = self.grid[row + 1][col]
                if col > 0:
                    self.grid[row][col].west  = self.grid[row][col - 1]
                if col < self.cols - 1:
                    self.grid[row][col].east  = self.grid[row][col + 1]

    def random_cell(self) -> Cell:
        return self.grid[randint(0, self.rows - 1)][randint(0, self.cols - 1)]


    def pretty_print(self) -> None:
        top = "+" + ("---+" * self.cols)
        print(top)
        for  row in self.grid:
            row_middle_output = "|"
            row_bottom_output = "+"
            for cell in row:
                body = "   "
                row_middle_output += body
                if cell.linked(cell.east):
                    row_middle_output += " "
                else:
                    row_middle_output += "|"
                if cell.linked(cell.south):
                    row_bottom_output += "   "
                else:
                    row_bottom_output += "---"
                row_bottom_output += "+"

            print(row_middle_output)
            print(row_bottom_output)
    
    
    def __len__(self) -> int:
        return self.rows * self.cols


    def __iter__(self) -> Iterator[Cell]:
        for row in self.grid:
            for cell in row:
                yield cell


    def __reversed__(self) -> Iterator[Cell]:
        for row in reversed(self.grid):
            for cell in reversed(row):
                yield cell


    def __getitem__(self, index) -> Cell:
        if index > (self.rows*self.cols - 1):
            raise IndexError("list index out of range")
        for i, cell in enumerate(self):
            if i == index:
                return cell
                
if __name__ == "__main__":
    g = Grid(4,4)
    g.pretty_print()
