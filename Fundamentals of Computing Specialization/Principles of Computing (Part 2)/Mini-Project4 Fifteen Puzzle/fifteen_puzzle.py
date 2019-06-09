"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        #1. check if zero is at position (target_row, target_col)
        if self.get_number(target_row, target_col):
            return False
            
        #2. check if all tiles in target_row + 1 or below are positioned at their
        #	solved location.   
        for row in range(target_row + 1, self._height):
            for col in range(self._width):
                if (row, col) != self.current_position(row, col):
                    return False
        
        #3. check if all tiles in target_row to the right of target position are 
        #	positioned at their solved location.
        for col in range(target_col + 1, self._width):
            if (target_row, col) != self.current_position(target_row, col):
                return False
        
        return True

    def position_tile_left(self, target_row, target_col, curr_row, curr_col):
        """
        move the current position of the target tile one column
        closer to the the target position i.e to the left by
        applying a cyclic move
        Updates the puzzle and returns a move string
        invariant : curr_col > target_col
        """
        # make sure the invariant holds true before calling the function
        assert curr_col > target_col, "curr_col should be > target_col "
        
        move = "u" + "r" * (curr_col - target_col)
        
        if (curr_row > 0):
            move += ("u" * (target_row - curr_row) + 
                     "l" * (curr_col - target_col))
            move += "d" * (target_row - curr_row + 1)
        else:
            move += ("u" * (target_row - curr_row - 1) +
                         "l" * (curr_col - target_col))
            move += "d" * (target_row - curr_row )

        self.update_puzzle(move)
        
        return move
    
    def position_tile_right(self, target_row, target_col, curr_row, curr_col):
        """
        move the current position of the target tile one column
        closer to the the target position i.e to the right by
        applying cyclic move
        Updates the puzzle and returns a move string
        invariant : curr_col < target_col
        """ 
        
        # make sure the invariant holds true before calling the function
        assert curr_col < target_col, "curr_col should be < target_col "
        
        if ( curr_row < target_row):
            move = "u" * (target_row - curr_row)
            move += "l" * (target_col - curr_col)
            move += "d" * (target_row - curr_row)
            move += "r" * (target_col - curr_col)
            self.update_puzzle(move)
        else:
            move = "l" * (target_col - curr_col)
            move += "u"
            move += "r" * (target_col - curr_col)
            move += "d"
            self.update_puzzle(move)     
        
        return move
    
    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # intialize a move sequence
        move_seq = ""
        
        while (True):
            # get the current position of the target tile
            (curr_row, curr_col) = self.current_position(target_row, target_col)
            
            # case 1: target tile is in the same column as zero tile
            if curr_col == target_col:

                # get the current position of the zero tile
                (zero_row, dummy_zero_col) = self.current_position(0,0)
                
                # move the zero tile above the target tile if it is
                # not the case 
                if (zero_row > curr_row):
                    add_move = "u" * (target_row - curr_row)
                    self.update_puzzle(add_move)
                    move_seq += add_move
                    
                # move the zero tile to the left of and same row as the target
                # tile and return the sequence
                if (target_row, target_col) == self.current_position(
                    target_row, target_col):
                    move_seq += "ld"
                    self.update_puzzle("ld")
                    return move_seq
                
                # do a cyclic move to bring the target tile one position
                # closer to the target position
                add_move = "lddru"
                self.update_puzzle(add_move)
                move_seq += add_move
                
            # case 2: if curr_col < target_col, bring the target tile
            # above the zero tile by applying cyclic move that moves
            # the target tile right
            elif curr_col < target_col:
                move_seq += self.position_tile_right(target_row, 
                                                     target_col, 
                                                     curr_row, curr_col)
            # case 3: if curr_col > target_col, bring the target tile
            # above the zero tile by applying cyclic move that moves
            # the target tile left
            else:
                move_seq += self.position_tile_left(target_row, 
                                                    target_col, 
                                                    curr_row, curr_col)
                
        return move_seq
    
    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
       
        # make sure the invariants are not violated
        assert target_row > 1, "Invalid input argument. target_row should be > 1"
        assert self.lower_row_invariant(target_row, 0),( 
                        "invariant was violated before solve_col0_tile")
        
        
        # initialize the move sequence
        move_seq = ""
          
        while(True):
            
            # get the current poisition of the target tile
            (curr_row, curr_col) = self.current_position(target_row, 0)
            
            # if the target tile is at row target_row - 1, and
            # column 0, (and zero tile is just below it) move
            # the zero tile up and all the way right, and the
            # puzzle is solved for position, (target_row, 0)
            if curr_col == 0 and (target_row - curr_row) == 1:
                add_move = "u"
                add_move += "r" * (self._width - 1)
                self.update_puzzle(add_move)
                move_seq += add_move
                return move_seq
            # otherwise apply the move string to solve a 3 x 2 puzzle
            # if the target tile is at row target_row - 1 and
            # column 1 and zero tile is at (target_row, 0)
            # and move the zero tile all the way to the right
            # once target tile is at (target_row, 0) 
            elif (target_row - curr_row) == 1 and curr_col == 1:
                add_move = "u"
                add_move += "ruld" + "rdlu" * 2 + "urddlu"
                add_move += "r" * (self._width - 1)
                self.update_puzzle(add_move)
                move_seq += add_move
                return move_seq
            
            # otherwise if target tile is at column 0 but 
            # row < target_row - 1 bring it to position 
            # (target_row - 1, 1)
            if curr_col == 0:
                add_move = "u" * (target_row - curr_row) + "r"
                add_move += "d" * (target_row - curr_row - 1) + "l" + "d"
                self.update_puzzle(add_move)
                move_seq +=  add_move
            
            # otherwise apply cyclic move to bring the target tile 
            # to position (target_row - 1, 1) by moving it left
            else:
                move_seq += self.position_tile_left(target_row, 
                                                    0, curr_row, curr_col)
                        
    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        
        #1. return False if zero tile is not at position (0, target_col)
        if self.get_number(0, target_col) != 0:
            return False
            
        #2. check if all tiles in row 0 and row 1 are are in their
        #	solved position (except the zero tile)
        for row in range(2):
            for col in range(target_col, self._width):
                if ((row, col) != (0, target_col) and 
                      (row, col) != self.current_position(row, col)):
                    return False
        
        #3. check if all tiles in 2 or below are positioned at their
        #	solved location.   
        for row in range(2, self._height):
            for col in range(self._width):
                if (row, col) != self.current_position(row, col):
                    return False
        
        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        
        #1. return False if zero tile is not at position (1, target_col)
        if self.get_number(1, target_col) != 0:
            #print "here1"
            return False
        
        #2. check if all tiles in row 0 and row 1 to the right of 
        #	target_col are in their solved position
        for row in range(2):
            for col in range(target_col + 1, self._width):
                if (row, col) != self.current_position(row, col):
                    #print "here2"
                    #print (row, col)
                    return False
                
        #3. check if all tiles in row 2 or below are positioned at their
        #	solved location.   
        for row in range(2, self._height):
            for col in range(self._width):
                if (row, col) != self.current_position(row, col):
                    #print "here3"
                    return False
                
        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        
        # initialize the move sequence
        move_seq = ""
        
        while(True):
            # get the current poisition of the target tile
            (curr_row, curr_col) = self.current_position(0, target_col)  
            
            # if target tile is just left of and same row 
            # as target poition move left and down and the
            # puzzle is solved at position (0, target_col)
            if (target_col - curr_col) == 1 and curr_row == 0:
                add_move = "ld"
                self.update_puzzle(add_move)
                move_seq += add_move
                return move_seq
            
            # otherwise, if target tile is just left of target
            # position but at row 1, move the zero tile to
            # the left of the current position of the target
            # tile and apply a move string to solve a 2 x 3
            # puzzle for position (0, target_col)
            elif (target_col - curr_col) == 1 and curr_row == 1:
                add_move = "lld"
                add_move += "urdlurrdluldrruld"
                self.update_puzzle(add_move)
                move_seq += add_move
                return move_seq
            
            # otherwise bring the target tile to position
            # (1, target_col - 1)
            else:
                add_move = "ld"
                add_move += "l" * (target_col - curr_col - 1)
                add_move += "u" + "r" * (target_col - curr_col)
                self.update_puzzle(add_move)
                move_seq += add_move
                
        return move_seq

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        
        # initialize the move sequence
        move_seq = ""
        
        while (True):
            # get the current position of the target tile
            (curr_row, curr_col) = self.current_position(1, target_col)
            
            # if target tile is just above the target position,
            # i.e target tile row = 0 and target tile column = target_col
            # move up and we have puzzle solved at the position
            # (0, target_col)
            if curr_col == target_col:
                add_move = "u"
                self.update_puzzle(add_move);
                move_seq += add_move
                return move_seq
            
            # otherise move the target tile right to bring it
            # to position (0, target_col)
            else:
                move_seq += self.position_tile_right(1, target_col, 
                                                     curr_row, curr_col)

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        
        # move the zero tile in its solved position
        move_seq = "lu"
        self.update_puzzle(move_seq)
        
        # keep applying the cyclic move until all tiles in
        # the upper left 2 x 2 portion of the puzzle is
        # solved. The loop runs a maximum of 2 times
        # and a minimum of 0 times
        while(not self.lower_row_invariant(0,0)):
            add_move = "rdlu"
            self.update_puzzle(add_move)
            move_seq += add_move
            
        return move_seq

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        
        Note: the solution approach needs to be modified
        to make it more efficeint since currently it solves 
        the whole puzzle from the beginning even if some 
        portion of the puzzle may already be solved
        """
        
        # initialze the move sequence
        move_seq = ""
        
        # get the current position of the zero tile
        (zero_row, zero_col) = self.current_position(0,0)
        
        # move the zero tile all the way to bottom right position 
        add_move = "r" * (self._width - 1 - zero_col)
        add_move += "d" * (self._height - 1 - zero_row)
        self.update_puzzle(add_move)
        move_seq += add_move
        
        # solve the bottom self._width - 2 rows of the puzzle 
        # from right to left moving bottom to top
        for row in range(self._height - 1, 1, -1 ):
            for col in range(self._width - 1, -1, -1):
                if( col == 0):
                    assert self.lower_row_invariant(row, 0), (
                        "col 0 invariant violated before function call "  + 
                        "at position "+ str(row) + ", " + str(col) + ")")
                    move_seq += self.solve_col0_tile(row)
                    assert self.lower_row_invariant(row - 1, self._width - 1), (
                        "col 0 invariant violated after function call "  + 
                        "at position ("+ str(row) + ", " + str(col) + ")")
                else:
                    assert self.lower_row_invariant(row, col), ( 
                        "lower row invariant violated before function call" + 
                        "at position (" + str(row) + ", " + str(col) + ")")
                    move_seq += self.solve_interior_tile(row, col)
                    assert self.lower_row_invariant(row, col - 1), (
                        "lower row invariant violated after function call" + 
                        "at position (" + str(row) + ", " + str(col) + ")")
                
        
        # solve the right self._height - 2 columns of the puzzle
        # bottom to top moving right to left
        for col in range(self._width - 1, 1, -1):
            assert self.row1_invariant(col), (
                "row1 invariant violated at position (" 
                + str(1) + ", " + str(col) + ")")
            move_seq += self.solve_row1_tile(col)
            assert self.row0_invariant(col), (
                "row0 invariant violated at position (" 
                + str(0) + ", " + str(col) + ")")
            move_seq += self.solve_row0_tile(col)            
        
        
        move_seq += self.solve_2x2()
        
        return move_seq

#Start interactive simulation
poc_fifteen_gui.FifteenGUI(Puzzle(4, 5))

