"""
Universal Cell class for maze graphs
"""
from collections import defaultdict
from typing import List

class Cell:
    def __init__(self,
                 row: int,
                 col: int,
                 north = None,
                 south = None,
                 east = None,
                 west = None) -> None:
        self.row = row
        self.col = col
        self.links = defaultdict(bool) # type: dict
        self.north = north
        self.south = south
        self.east  = east
        self.west  = west

    
    def link(self, cell, bidi: bool = True) -> None:
        self.links[cell] = True
        if bidi:
            cell.link(self, False)


    def unlink(self, cell, bidi: bool = True) -> None:
        self.links[cell] = False
        if bidi:
            cell.unlink(self, False)

    
    def linked(self, cell) -> bool:
        if self.links[cell]:
            return self.links[cell]
        else:
            return False


    def neighbors(self) -> list:
        neighbors = [self.north, self.south, self.east, self.west]
        return [ cell for cell in neighbors if cell is not None ]
        
