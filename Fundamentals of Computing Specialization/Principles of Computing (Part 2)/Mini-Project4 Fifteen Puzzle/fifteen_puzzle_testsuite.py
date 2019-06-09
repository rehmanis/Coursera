"""
Testing suite for functions used in  
Loyd's Fifteen puzzle - solver Mini-project
Note that solved configuration has the blank 
(zero) tile in upper left
"""

import poc_simpletest as simpletest
import user46_p9CLHFUXsW_56 as puzzle

class TestFifteenPuzzle():
    """
    function that tests the lower_row_invariant
    of the Fifteen puzzle - solver
    """
    def test_lower_row_invariant(self):
        # create a TestSuite object
        suite = simpletest.TestSuite()    

        print "running lower_row_invariant function test..."

        # Test #1.1: create an scramble board with Zero tile
        # not at target position
        game_board = [[0, 1, 4, 3], 
                      [9, 7, 5, 8], 
                      [15, 2, 6, 14], 
                      [13, 11, 12, 10]]
        my_game = puzzle.Puzzle(4, 4, game_board)
        comp_lower_row_inv = my_game.lower_row_invariant(1,1)
        exp_lower_row_inv = False
        
        # run the Test #1.1 and compare the computed vs expected
        suite.run_test(str(comp_lower_row_inv), str(exp_lower_row_inv), 
                       "Test #1.1: lower_row_invariant")
        
        # Test #1.2: create an scramble board with Zero tile
        # at the target position but still failing the invariant
        game_board = [[8, 1, 4, 3], 
                      [9, 7, 5, 0], 
                      [15, 2, 6, 14], 
                      [13, 11, 12, 10]]
        my_game = puzzle.Puzzle(4, 4, game_board)
        comp_lower_row_inv = my_game.lower_row_invariant(1,3)
        exp_lower_row_inv = False
        
        # run the Test #1.2 and compare the computed vs expected
        suite.run_test(str(comp_lower_row_inv), str(exp_lower_row_inv), 
                       "Test #1.2: lower_row_invariant")
        
        # Test #1.3: create an board with Zero tile not at the 
        # target position but all other tiles are in solved position
        game_board = [[0, 1, 4, 3], 
                      [6, 2, 5, 7], 
                      [8, 9, 10, 11], 
                      [12, 13, 14, 15]]
        my_game = puzzle.Puzzle(4, 4, game_board)
        comp_lower_row_inv = my_game.lower_row_invariant(1,2)
        exp_lower_row_inv = False
        
        # run the Test #1.3 and compare the computed vs expected
        suite.run_test(str(comp_lower_row_inv), str(exp_lower_row_inv), 
                       "Test #1.3: lower_row_invariant")
        
        
        
        # Test #1.4: create an scramble board with Zero tile
        # at the target position but invariant is false because 
        # the following conidiotn is not met:
        # all tiles in target_row + 1 or below are positioned 
        # at their solved location.
        game_board = [[8, 1, 4, 3], 
                      [9, 5, 0, 7], 
                      [15, 2, 6, 14], 
                      [13, 11, 12, 10]]
        my_game = puzzle.Puzzle(4, 4, game_board)
        comp_lower_row_inv = my_game.lower_row_invariant(1,2)
        exp_lower_row_inv = False
        
        # run the Test #1.4 and compare the computed vs expected
        suite.run_test(str(comp_lower_row_inv), str(exp_lower_row_inv), 
                       "Test #1.4: lower_row_invariant")
        
        # Test #1.5: create an scramble board with Zero tile
        # at the target position but invariant is false because 
        # the following conidiotn is not met:
        # all tiles in target_row to the right of target position are 
        # positioned at their solved location.
        game_board = [[1, 2, 3, 4], 
                      [5, 7, 0, 6], 
                      [8, 9, 10, 11], 
                      [12, 13, 14, 15]]
        my_game = puzzle.Puzzle(4, 4, game_board)
        comp_lower_row_inv = my_game.lower_row_invariant(1,2)
        exp_lower_row_inv = False
        
        # run the Test #1.5 and compare the computed vs expected
        suite.run_test(str(comp_lower_row_inv), str(exp_lower_row_inv), 
                       "Test #1.5: lower_row_invariant")
        
        # Test #1.6: create an scramble board with that meets the 
        # lower row invariant
        game_board = [[3, 2, 1, 4], 
                      [6, 5, 0, 7], 
                      [8, 9, 10, 11], 
                      [12, 13, 14, 15]]
        my_game = puzzle.Puzzle(4, 4, game_board)
        comp_lower_row_inv = my_game.lower_row_invariant(1,2)
        exp_lower_row_inv = True
        
        # run the Test #1.6 and compare the computed vs expected
        suite.run_test(str(comp_lower_row_inv), str(exp_lower_row_inv), 
                       "Test #1.6: lower_row_invariant")
        
        # Test #1.7: check row, col corner positions to see if 
        # invriant is still valid
        game_board = [[3, 2, 1, 0], 
                      [4, 5, 6, 7], 
                      [8, 9, 10, 11], 
                      [12, 13, 14, 15]]
        my_game = puzzle.Puzzle(4, 4, game_board)
        comp_lower_row_inv = my_game.lower_row_invariant(0,3)
        exp_lower_row_inv = True
        
        # run the Test #1.7 and compare the computed vs expected
        suite.run_test(str(comp_lower_row_inv), str(exp_lower_row_inv), 
                       "Test #1.7: lower_row_invariant")
        
        # Test #1.8: all tiles except for one are in solved position
        # invariant should be False
        game_board = [[3, 2, 1, 10], 
                      [4, 5, 6, 7], 
                      [8, 9, 0, 11], 
                      [13, 12, 14, 15]]
        my_game = puzzle.Puzzle(4, 4, game_board)
        comp_lower_row_inv = my_game.lower_row_invariant(2,2)
        exp_lower_row_inv = False
        
        # run the Test #1.8 and compare the computed vs expected
        suite.run_test(str(comp_lower_row_inv), str(exp_lower_row_inv), 
                       "Test #1.8: lower_row_invariant")


        # report number of tests and failures
        suite.report_results()
        print 
        
    def test_solve_interior_tile(self):
        # create a TestSuite object
        suite = simpletest.TestSuite()    

        print "running solve_interior_tile function test..."

        # Test #2.1: check the case when the current column
        # of the target tile is to the right of target_col
        # and current row > 0 
        my_puzzle = puzzle.Puzzle(5, 5, [[1, 2, 3, 4, 5],
                                         [6, 7, 8, 9, 22],
                                         [11, 12, 13, 14, 15],
                                         [16, 17, 18, 19, 20],
                                         [21, 10, 0, 23, 24]])
        my_puzzle.solve_interior_tile(4, 2)
        comp_out = my_puzzle.lower_row_invariant(4, 1)
        act_out = True
        
        # run the Test #2.1 and compare the computed vs expected
        suite.run_test(str(comp_out), str(act_out), 
                       "Test #2.1: solve_interior_tile")
        
        # Test #2.2: check the case when the current column
        # of the target tile is to the right of target_col
        # and current row of target tile is 0
        my_puzzle = puzzle.Puzzle(5, 5, [[1, 2, 3, 4, 22],
                                         [6, 7, 8, 9, 5],
                                         [11, 12, 13, 14, 15],
                                         [16, 17, 18, 19, 20],
                                         [21, 10, 0, 23, 24]])
        my_puzzle.solve_interior_tile(4, 2)
        comp_out = my_puzzle.lower_row_invariant(4, 1)
        act_out = True
        
        # run the Test #2.2 and compare the computed vs expected
        suite.run_test(str(comp_out), str(act_out), 
                       "Test #2.2: solve_interior_tile")
        
        # Test #2.3: check the case when the current column
        # of the target tile is to the right of target_col
        # and current row is just above target_row 
        my_puzzle = puzzle.Puzzle(5, 5, [[1, 2, 3, 4, 19],
                                         [6, 7, 8, 9, 5],
                                         [11, 12, 13, 14, 15],
                                         [16, 17, 18, 20, 22],
                                         [21, 10, 0, 23, 24]])
        my_puzzle.solve_interior_tile(4, 2)
        comp_out = my_puzzle.lower_row_invariant(4, 1)
        act_out = True
        
        # run the Test #2.3 and compare the computed vs expected
        suite.run_test(str(comp_out), str(act_out), 
                       "Test #2.3: solve_interior_tile")
        
        # Test #2.4: check the case when the current column
        # of the target tile is to the left of target_col
        # and current row is 0
        my_puzzle = puzzle.Puzzle(5, 5, [[22, 2, 3, 4, 19],
                                         [6, 7, 8, 9, 5],
                                         [11, 12, 13, 14, 15],
                                         [16, 17, 18, 20, 1],
                                         [21, 10, 0, 23, 24]])
        my_puzzle.solve_interior_tile(4, 2)
        comp_out = my_puzzle.lower_row_invariant(4, 1)
        act_out = True
        
        # run the Test #2.4 and compare the computed vs expected
        suite.run_test(str(comp_out), str(act_out), 
                       "Test #2.4: solve_interior_tile")
        
        # Test #2.5: check the case when the current column
        # of the target tile is to the left of target_col
        # and current row > 0
        my_puzzle = puzzle.Puzzle(5, 5, [[6, 2, 3, 4, 19],
                                         [22, 7, 8, 9, 5],
                                         [11, 12, 13, 14, 15],
                                         [16, 17, 18, 20, 1],
                                         [21, 10, 0, 23, 24]])
        my_puzzle.solve_interior_tile(4, 2)
        comp_out = my_puzzle.lower_row_invariant(4, 1)
        act_out = True
        
        # run the Test #2.5 and compare the computed vs expected
        suite.run_test(str(comp_out), str(act_out), 
                       "Test #2.5: solve_interior_tile")
        
        # Test #2.6: check the case when the current column
        # of the target tile is to the left of target_col
        # and current row is just above target_row
        my_puzzle = puzzle.Puzzle(5, 5, [[6, 2, 3, 4, 19],
                                         [16, 7, 8, 9, 5],
                                         [11, 12, 13, 14, 15],
                                         [22, 17, 18, 20, 1],
                                         [21, 10, 0, 23, 24]])
        my_puzzle.solve_interior_tile(4, 2)
        comp_out = my_puzzle.lower_row_invariant(4, 1)
        act_out = True
        
        # run the Test #2.6 and compare the computed vs expected
        suite.run_test(str(comp_out), str(act_out), 
                       "Test #2.6: solve_interior_tile")
        
        # Test #2.7: check the case when the target_col - current column > 1 
        # and current row = target_row
        my_puzzle = puzzle.Puzzle(5, 5, [[6, 2, 3, 4, 19],
                                         [16, 7, 8, 9, 5],
                                         [11, 12, 13, 14, 15],
                                         [22, 17, 18, 20, 1],
                                         [23, 10, 21, 0, 24]])
        my_puzzle.solve_interior_tile(4, 3)
        comp_out = my_puzzle.lower_row_invariant(4, 2)
        act_out = True
        
        # run the Test #2.7 and compare the computed vs expected
        suite.run_test(str(comp_out), str(act_out), 
                       "Test #2.7: solve_interior_tile")
        
        # Test #2.8: check the case when the (target_col - current column) = 1 
        # and current row = target_row
        my_puzzle = puzzle.Puzzle(5, 5, [[6, 2, 3, 4, 19],
                                         [16, 7, 8, 9, 5],
                                         [11, 12, 13, 14, 15],
                                         [22, 17, 18, 20, 1],
                                         [21, 10, 23, 0, 24]])
        my_puzzle.solve_interior_tile(4, 3)
        comp_out = my_puzzle.lower_row_invariant(4, 2)
        act_out = True
        
        # run the Test #2.8 and compare the computed vs expected
        suite.run_test(str(comp_out), str(act_out), 
                       "Test #2.8: solve_interior_tile")
        
        # Test #2.9: check the case when the (target_col = current column
        # and current row - target_row = 1
        my_puzzle = puzzle.Puzzle(5, 5, [[6, 2, 3, 4, 19],
                                         [16, 7, 8, 9, 5],
                                         [11, 12, 13, 14, 15],
                                         [22, 17, 18, 23, 1],
                                         [21, 10, 20, 0, 24]])
        my_puzzle.solve_interior_tile(4, 3)
        comp_out = my_puzzle.lower_row_invariant(4, 2)
        act_out = True
        
        # run the Test #2.9 and compare the computed vs expected
        suite.run_test(str(comp_out), str(act_out), 
                       "Test #2.9: solve_interior_tile")
        
        # Test #2.10: check the case when the (target_col = current column
        # and current row - target_row > 1
        my_puzzle = puzzle.Puzzle(5, 5, [[6, 2, 3, 23, 4],
                                         [16, 7, 8, 9, 5],
                                         [11, 12, 13, 14, 15],
                                         [22, 17, 18, 19, 1],
                                         [21, 10, 20, 0, 24]])
        my_puzzle.solve_interior_tile(4, 3)
        comp_out = my_puzzle.lower_row_invariant(4, 2)
        act_out = True
        
        # run the Test #2.10 and compare the computed vs expected
        suite.run_test(str(comp_out), str(act_out), 
                       "Test #2.10: solve_interior_tile")
        
        # report number of tests and failures
        suite.report_results()
        print 
        
    def test_solve_col0_tile(self):
        # create a TestSuite object
        suite = simpletest.TestSuite()    

        print "running solve_col0_tile function test..."

        # Test #3.1: check the case when the target tile's
        # current column is to the right of column 0.
        # current column > 1 and (current row - target_row) = 1
        my_puzzle = puzzle.Puzzle(5, 5, [[1, 2, 3, 4, 5],
                                         [6, 7, 8, 9, 10],
                                         [11, 12, 13, 14, 15],
                                         [16, 17, 18, 19, 20],
                                         [0, 21, 22, 23, 24]])
        my_puzzle.solve_col0_tile(4)
        comp_out = my_puzzle.lower_row_invariant(3, 4)
        exp_out = True
        
        # run the Test #3.1 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #3.1: solve_col0_tile")
        
        # Test #3.2: check the case when the target tile's
        # current column is to the right of column 0.
        # current column = 1 and (current row - target_row) = 1
        my_puzzle = puzzle.Puzzle(5, 5, [[1, 2, 3, 4, 5],
                                         [6, 7, 8, 9, 10],
                                         [11, 12, 13, 14, 15],
                                         [16, 20, 18, 19, 17],
                                         [0, 21, 22, 23, 24]])
        my_puzzle.solve_col0_tile(4)
        comp_out = my_puzzle.lower_row_invariant(3, 4)
        exp_out = True
        
        # run the Test #3.2 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #3.2: solve_col0_tile")
        
        # Test #3.3: check the case when the target tile's
        # current column is to the right of column 0 (current column > 1)
        # and current row = 0
        my_puzzle = puzzle.Puzzle(5, 5, [[1, 2, 3, 4, 20],
                                         [6, 7, 8, 9, 10],
                                         [11, 12, 13, 14, 15],
                                         [16, 5, 18, 19, 17],
                                         [0, 21, 22, 23, 24]])
        my_puzzle.solve_col0_tile(4)
        comp_out = my_puzzle.lower_row_invariant(3, 4)
        exp_out = True
        
        # run the Test #3.3 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #3.3: solve_col0_tile")
        
        # Test #3.4: check the case when the target tile's
        # current column is column 0 (current column = 0) 
        # and current row = 0
        my_puzzle = puzzle.Puzzle(5, 5, [[20, 2, 3, 4, 1],
                                         [6, 7, 8, 9, 10],
                                         [11, 12, 13, 14, 15],
                                         [16, 5, 18, 19, 17],
                                         [0, 21, 22, 23, 24]])
        my_puzzle.solve_col0_tile(4)
        comp_out = my_puzzle.lower_row_invariant(3, 4)
        exp_out = True
        
        # run the Test #3.4 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #3.4: solve_col0_tile")
        
        # Test #3.5: check the case when the target tile's
        # current column is column 0 (current column = 0) 
        # and current row = target_row - 1
        my_puzzle = puzzle.Puzzle(5, 5, [[16, 2, 3, 4, 1],
                                         [6, 7, 8, 9, 10],
                                         [11, 12, 13, 14, 15],
                                         [20, 5, 18, 19, 17],
                                         [0, 21, 22, 23, 24]])
        my_puzzle.solve_col0_tile(4)
        comp_out = my_puzzle.lower_row_invariant(3, 4)
        exp_out = True
        
        # run the Test #3.5 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #3.5: solve_col0_tile")
        
        # report number of tests and failures
        suite.report_results()
        print 
        
    def test_row0_invariant(self):
        
        # create a TestSuite object
        suite = simpletest.TestSuite()    

        print "running row0_invariant function test..."        
        
        # Test #4.1: tile zero is in the incorrect position
        my_puzzle = puzzle.Puzzle(5, 5, [[2, 3, 0, 1, 4],
                                         [5, 6, 7, 8, 9],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 17, 18, 19],
                                         [20, 21, 22, 23, 24]])
        
        comp_out = my_puzzle.row0_invariant(3)
        exp_out = False
        
        # run the Test #4.1 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #4.1: row0_invariant")
        
        # Test #4.2: row 1 tiles are not in their solved
        # positions
        my_puzzle = puzzle.Puzzle(5, 5, [[2, 3, 1, 0, 4],
                                         [5, 6, 7, 9, 8],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 17, 18, 19],
                                         [20, 21, 22, 23, 24]])
        
        comp_out = my_puzzle.row0_invariant(3)
        exp_out = False
        
        # run the Test #4.2 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #4.2: row0_invariant")
        
        # Test #4.3: row 0 tiles are not in their solved
        # positions
        my_puzzle = puzzle.Puzzle(5, 5, [[2, 4, 1, 0, 3],
                                         [5, 6, 7, 8, 9],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 17, 18, 19],
                                         [20, 21, 22, 23, 24]])
        
        comp_out = my_puzzle.row0_invariant(3)
        exp_out = False
        
        # run the Test #4.3 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #4.3: row0_invariant")
        
        # Test #4.4: a row > 1 has tiles that are not in their solved
        # positions
        my_puzzle = puzzle.Puzzle(5, 5, [[2, 3, 1, 0, 4],
                                         [5, 6, 7, 8, 9],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 17, 18, 19],
                                         [20, 21, 23, 22, 24]])
        
        comp_out = my_puzzle.row0_invariant(3)
        exp_out = False
        
        # run the Test #4.4 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #4.4: row0_invariant")
        
        
        # Test #4.5: the puzzle configurate meets the invariant 
        my_puzzle = puzzle.Puzzle(5, 5, [[2, 3, 1, 0, 4],
                                         [5, 7, 6, 8, 9],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 17, 18, 19],
                                         [20, 21, 22, 23, 24]])
        
        comp_out = my_puzzle.row0_invariant(3)
        exp_out = True
        
        # run the Test #4.5 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #4.5: row0_invariant")          
                
        # report number of tests and failures
        suite.report_results()
        print 
    
    def test_row1_invariant(self):

        # create a TestSuite object
        suite = simpletest.TestSuite()    

        print "running row1_invariant function test..."        
        
        # Test #5.1: tile zero is in the incorrect position
        my_puzzle = puzzle.Puzzle(5, 5, [[2, 3, 9, 1, 4],
                                         [5, 6, 7, 8, 0],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 17, 18, 19],
                                         [20, 21, 22, 23, 24]])
        
        comp_out = my_puzzle.row1_invariant(3)
        exp_out = False
        
        # run the Test #5.1 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #5.1: row1_invariant")
        
        # Test #5.2: tiles in row 0 to the right of
        # the zero tile are not in their solved position
        my_puzzle = puzzle.Puzzle(5, 5, [[2, 4, 8, 1, 3],
                                         [5, 7, 6, 0, 9],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 17, 18, 19],
                                         [20, 21, 22, 23, 24]])
        
        comp_out = my_puzzle.row1_invariant(3)
        exp_out = False
        
        # run the Test #5.2 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #5.2: row1_invariant")
        
        # Test #5.3: tiles in row 1 to the right of
        # the zero tile are not in their solved position
        my_puzzle = puzzle.Puzzle(5, 5, [[2, 3, 9, 1, 4],
                                         [5, 7, 6, 0, 8],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 17, 18, 19],
                                         [20, 21, 22, 23, 24]])
        
        comp_out = my_puzzle.row1_invariant(3)
        exp_out = False
        
        # run the Test #5.3 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #5.3: row1_invariant")

        # Test #5.4: tiles in row > 1 are not in their solved position
        my_puzzle = puzzle.Puzzle(5, 5, [[2, 3, 8, 1, 4],
                                         [5, 7, 6, 0, 9],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 18, 17, 19],
                                         [20, 21, 22, 23, 24]])
        
        comp_out = my_puzzle.row1_invariant(3)
        exp_out = False
        
        # run the Test #5.4 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #5.4: row1_invariant")
        
        # Test #5.5: puzzle configuration meets the invariant
        my_puzzle = puzzle.Puzzle(5, 5, [[2, 3, 8, 1, 4],
                                         [5, 7, 6, 0, 9],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 17, 18, 19],
                                         [20, 21, 22, 23, 24]])
        
        comp_out = my_puzzle.row1_invariant(3)
        exp_out = True
        
        # run the Test #5.5 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #5.5: row1_invariant")           
                
        # report number of tests and failures
        suite.report_results()
        print
        
    def test_solve_row0_tile(self):
        
        # create a TestSuite object
        suite = simpletest.TestSuite()    

        print "running solve_row0_tile function test..."

        # Test #6.1: current position of the target tile  
        # is just left of target position and current row
        # is 0
        my_puzzle = puzzle.Puzzle(5, 5, [[3, 1, 2, 4, 0],
                                         [5, 6, 7, 8, 9],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 17, 18, 19],
                                         [20, 21, 22, 23, 24]])
        my_puzzle.solve_row0_tile(4)
        comp_out = my_puzzle.row1_invariant(3)
        exp_out = True
        
        # run the Test #6.1 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #6.1: solve_row0_tile")
        
        
        # Test #6.2: current position of the target tile  
        # is just left of target position and current row
        # is 1
        my_puzzle = puzzle.Puzzle(5, 5, [[3, 1, 2, 8, 0],
                                         [5, 6, 7, 4, 9],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 17, 18, 19],
                                         [20, 21, 22, 23, 24]])
        my_puzzle.solve_row0_tile(4)
        comp_out = my_puzzle.row1_invariant(3)
        exp_out = True
        
        # run the Test #6.2 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #6.2: solve_row0_tile")
        
        
        # Test #6.3: target_col - current column > 1 and 
        # current row is 0
        my_puzzle = puzzle.Puzzle(5, 5, [[4, 1, 2, 8, 0],
                                         [5, 6, 7, 3, 9],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 17, 18, 19],
                                         [20, 21, 22, 23, 24]])
        my_puzzle.solve_row0_tile(4)
        comp_out = my_puzzle.row1_invariant(3)
        exp_out = True
        
        # run the Test #6.3 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #6.3: solve_row0_tile")
        
        # Test #6.4: target_col - current column > 1 and 
        # current row is 1
        my_puzzle = puzzle.Puzzle(5, 5, [[6, 1, 2, 8, 0],
                                         [5, 4, 7, 3, 9],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 17, 18, 19],
                                         [20, 21, 22, 23, 24]])
        my_puzzle.solve_row0_tile(4)
        comp_out = my_puzzle.row1_invariant(3)
        exp_out = True
        
        # run the Test #6.4 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #6.4: solve_row0_tile")          
        
        # report number of tests and failures
        suite.report_results()
        print 
    
    def test_solve_row1_tile(self):
        
        # create a TestSuite object
        suite = simpletest.TestSuite()    

        print "running solve_row1_tile function test..."        
        
        # Test #7.1: target_col = current column and 
        # current row is 0
        my_puzzle = puzzle.Puzzle(5, 5, [[3, 1, 2, 8, 4],
                                         [5, 6, 7, 0, 9],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 17, 18, 19],
                                         [20, 21, 22, 23, 24]])
        my_puzzle.solve_row1_tile(3)
        comp_out = my_puzzle.row0_invariant(3)
        exp_out = True
        
        # run the Test #7.1 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #7.1: solve_row1_tile")
        
        # Test #7.2: target_col - current column = 1 and 
        # current row is 0
        my_puzzle = puzzle.Puzzle(5, 5, [[3, 1, 8, 2, 4],
                                         [5, 6, 7, 0, 9],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 17, 18, 19],
                                         [20, 21, 22, 23, 24]])
        my_puzzle.solve_row1_tile(3)
        comp_out = my_puzzle.row0_invariant(3)
        exp_out = True
        
        # run the Test #7.2 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #7.2: solve_row1_tile")
        
        # Test #7.3: target_col - current column = 1 and 
        # current row is 1
        my_puzzle = puzzle.Puzzle(5, 5, [[3, 1, 7, 2, 4],
                                         [5, 6, 8, 0, 9],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 17, 18, 19],
                                         [20, 21, 22, 23, 24]])
        my_puzzle.solve_row1_tile(3)
        comp_out = my_puzzle.row0_invariant(3)
        exp_out = True
        
        # run the Test #7.3 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #7.3: solve_row1_tile")
        
        # Test #7.4: target_col - current column > 1 and 
        # current row is 1
        my_puzzle = puzzle.Puzzle(5, 5, [[3, 1, 7, 2, 4],
                                         [5, 8, 6, 0, 9],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 17, 18, 19],
                                         [20, 21, 22, 23, 24]])
        my_puzzle.solve_row1_tile(3)
        comp_out = my_puzzle.row0_invariant(3)
        exp_out = True
        
        # run the Test #7.4 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #7.4: solve_row1_tile")
        
        # Test #7.5: target_col - current column > 1 and 
        # current row is 0
        my_puzzle = puzzle.Puzzle(5, 5, [[3, 1, 7, 2, 4],
                                         [5, 8, 6, 0, 9],
                                         [10, 11, 12, 13, 14],
                                         [15, 16, 17, 18, 19],
                                         [20, 21, 22, 23, 24]])
        my_puzzle.solve_row1_tile(3)
        comp_out = my_puzzle.row0_invariant(3)
        exp_out = True
        
        # run the Test #7.5 and compare the computed vs expected
        suite.run_test(str(comp_out), str(exp_out), 
                       "Test #7.5: solve_row1_tile")        
        
        # report number of tests and failures
        suite.report_results()
        print 

# test all functions of the word wangler pini-project
test_puzzle = TestFifteenPuzzle()
test_puzzle.test_lower_row_invariant()
test_puzzle.test_solve_interior_tile()
test_puzzle.test_solve_col0_tile()
test_puzzle.test_row0_invariant()
test_puzzle.test_row1_invariant()
test_puzzle.test_solve_row0_tile()
test_puzzle.test_solve_row1_tile()


