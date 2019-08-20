"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Other global constants
EMPTY = 0

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # create an empty list
    mergelst = []
    
    # put all non-zero values from the list line to begining of mergelst
    for val in list(line):
        if (val != 0):
            mergelst.append(val)
    
    # replace same pairs values with twice it's value
    mergelst2 = [];
    idx = 0
    while idx < (len(mergelst)):
        if (idx < len(mergelst)-1 and mergelst[idx] == mergelst[idx+1]):
            mergelst2.append(2*mergelst[idx])
            idx += 1
        else:
            mergelst2.append(mergelst[idx])
            
        idx +=1
    
    # add zeros at the end of merged list to make the size same as list line         
    mergelst2.extend([0]*(len(line)-len(mergelst2)))
    
    return mergelst2

def get_indices(lst_of_lst):
    """
    Helper function that travesrses over a list of lists and returns
    a list of indices corresponding to zero value
    """
    # initialize empty list to hold indices(row, col) for locations
    # of zero value in the input list 
    lst_of_indices = []
    # iterate over the input list and add indices(row,col) as required
    for row_idx in range(len(lst_of_lst)):
        lst_of_indices += [[row_idx, col_idx] 
         for col_idx in range(len(lst_of_lst[row_idx])) 
         if lst_of_lst[row_idx][col_idx] == EMPTY ]
        
    return lst_of_indices

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # intialize the class private members
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid_empty_indices = []
        self._grid = []
        # holds the initial/starting tile values for each direction
        self._strt_tiles = {UP: [(0,col) for col in range(self._grid_width)],
           DOWN: [(self._grid_height - 1,col) for col in range(self._grid_width)],
           LEFT: [(row, 0) for row in range(self._grid_height)],
           RIGHT: [(row, self._grid_width - 1) for row in range(self._grid_height)]}
        # reset creates any empty grid and adds two new tiles
        self.reset()
                
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # create an empty grid(list of lists)
        self._grid = [[0] * self._grid_width 
                     for dummy_num in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        grid_str = "current grid values:\n"
        for row in range(self._grid_height):
            grid_str += str(self._grid[row])+ "\n"
        return grid_str

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # state to store if any title value has changed or not after a move
        changed = False
        # iterate of initial/start tile for the given direction to perform move
        for row, col in self._strt_tiles[direction]:
            # line will hold all the row or cols for the given starting tile
            line = []
            # store the start tile row and column
            strt_row = row
            strt_col = col
            # iterate over all tiles starting at the start tile and add the values
            # of the tiles to a temporay list line
            while 0 <= row < self.get_grid_height() and 0 <= col < self.get_grid_width():
                line.append(self.get_tile(row, col))
                row += OFFSETS[direction][0]
                col += OFFSETS[direction][1]
                
            # perform merge on the stored values for a given row or column of the grid      
            merge_line = merge(line)
            # check to see if any values changed during merge and update the value
            # of that location on the grid
            for val in merge_line:
                if val != self.get_tile(strt_row, strt_col):
                    changed = True
                    self.set_tile(strt_row, strt_col, val)
                strt_row += OFFSETS[direction][0]
                strt_col += OFFSETS[direction][1]
                
        # if any tile changed during a move along a given direction, randomly
        # add a new tile
        if (changed):
            self.new_tile()
                

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # get a list of all the empry location on the grid
        self._grid_empty_indices = get_indices(self._grid)

        # add new tile only to if grid has any empty tiles 
        if len(self._grid_empty_indices) != EMPTY:
            # randomly select an empty row and col indices of the grid
            rnd_val = random.randrange(0, len(self._grid_empty_indices))
            # get the row and col number of this empty tile
            row = self._grid_empty_indices[rnd_val][0]
            col = self._grid_empty_indices[rnd_val][1]
            # create a list of nine 2's and one 4 to achieve the 90%
            # and 10% probablity criteria
            lst_tiles = [2] * 9 + [4]
            # select 2 90% or 4 10% of the time and set it to the empty
            # tile value randomly selected earlier
            self._grid[row][col] = random.choice(lst_tiles) 

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

