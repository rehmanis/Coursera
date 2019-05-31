"""
Testing suite for functions used in one implementation
of Yathzee game
"""
import poc_simpletest as simpletest
import user46_NHM1TTnSvs_129 as ttt_minimax
import poc_ttt_provided as provided


import codeskulptor
codeskulptor.set_timeout(60)


class TestTicTacToeMinimax():
    """
    function that tests the mm_move function
    of the Tic-Tac-Toe game with minimax mini-project
    """
    def test_mm_move(self):
        # create a TestSuite object
        suite = simpletest.TestSuite()    

        print "running mm_move function test..."

        # Test #1.1: check the base case for when the game is drawn and
        # no more legal moves are left
        board = provided.TTTBoard(3, False, 
                                  [[provided.PLAYERO, provided.PLAYERX, provided.PLAYERO],
                                   [provided.PLAYERO, provided.PLAYERX, provided.PLAYERO],
                                   [provided.PLAYERX, provided.PLAYERO, provided.PLAYERX]])
        actual_move = ttt_minimax.mm_move(board, provided.PLAYERX)
        exp_move = (0, (-1, -1))
        # run the Test #1.1 and compare the expected vs actual output
        suite.run_test(str(actual_move), str(exp_move), 
                       "Test #1.1: mm_move")

        # Test #1.2: check the base case for when PLAYERX has won and no more
        # legal moves are left
        board = provided.TTTBoard(3, False, 
                                  [[provided.PLAYERO, provided.PLAYERX, provided.PLAYERX],
                                   [provided.PLAYERO, provided.PLAYERX, provided.PLAYERO],
                                   [provided.PLAYERX, provided.PLAYERO, provided.PLAYERX]])
        actual_move = ttt_minimax.mm_move(board, provided.PLAYERX)
        exp_move = (1, (-1, -1))
        # run the Test #1.3 and compare the expected vs actual output
        suite.run_test(str(actual_move), str(exp_move), 
                       "Test #1.2: mm_move")
        
        # Test #1.3: check the base case for when PLAYERX has lost and no more
        # legal moves are left
        board = provided.TTTBoard(3, False, 
                                  [[provided.PLAYERO, provided.PLAYERX, provided.PLAYERO],
                                   [provided.PLAYERO, provided.PLAYERX, provided.PLAYERO],
                                   [provided.PLAYERO, provided.PLAYERO, provided.PLAYERX]])
        actual_move = ttt_minimax.mm_move(board, provided.PLAYERX)
        exp_move = (-1, (-1, -1))
        # run the Test #1.3 and compare the expected vs actual output
        suite.run_test(str(actual_move), str(exp_move), 
                       "Test #1.3: mm_move")
        
        # Test #1.4: check the case when only one move is left, and choosing
        # results in PLAYERX winning
        board = provided.TTTBoard(3, False, 
                                  [[provided.PLAYERO, provided.PLAYERX, provided.PLAYERX],
                                   [provided.PLAYERO, provided.PLAYERX, provided.PLAYERO],
                                   [provided.EMPTY, provided.PLAYERO, provided.PLAYERX]])
        actual_move = ttt_minimax.mm_move(board, provided.PLAYERX)
        exp_move = (1, (2, 0))
        # run the Test #1.4 and compare the expected vs actual output
        suite.run_test(str(actual_move), str(exp_move), 
                       "Test #1.4: mm_move")
        
        # Test #1.5: check the case when only two moves are left, and PLAYERO
        # minimizes its score so that it wins
        board = provided.TTTBoard(3, False, 
                                  [[provided.PLAYERO, provided.PLAYERX, provided.PLAYERX],
                                   [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
                                   [provided.EMPTY, provided.PLAYERO, provided.PLAYERX]])
        actual_move = ttt_minimax.mm_move(board, provided.PLAYERO)
        exp_move = (-1, (2, 0))
        # run the Test #1.5 and compare the expected vs actual output
        suite.run_test(str(actual_move), str(exp_move), 
                       "Test #1.5: mm_move")
        
        # Test #1.6: check the case when two moves are left and the PLAYERO
        # minimizes to draw the game
        board = provided.TTTBoard(3, False, 
                                  [[provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
                                   [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
                                   [provided.PLAYERX, provided.PLAYERO, provided.PLAYERX]])
        actual_move = ttt_minimax.mm_move(board, provided.PLAYERO)
        exp_move = (0, (0, 2))
        # run the Test #1.6 and compare the expected vs actual output
        suite.run_test(str(actual_move), str(exp_move), 
                       "Test #1.6: mm_move")
        
        # Test #1.7: check to see if PLAYERO chooses the correct move
        # that will result in a draw
        board = provided.TTTBoard(3, False, 
                                  [[provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
                                   [provided.PLAYERO, provided.PLAYERX, provided.EMPTY],
                                   [provided.EMPTY, provided.PLAYERO, provided.PLAYERX]])
        actual_move = ttt_minimax.mm_move(board, provided.PLAYERX)
        exp_move = (0, (2, 0))
        # run the Test #1.7 and compare the expected vs actual output
        suite.run_test(str(actual_move), str(exp_move), 
                       "Test #1.7: mm_move")
        
        
        # Test #1.8: test another board configuration for the draw vs loss for PLAYERO
        board = provided.TTTBoard(3, False, 
                                  [[provided.PLAYERX, provided.PLAYERO, provided.PLAYERX], 
                                   [provided.PLAYERX, provided.PLAYERO, provided.PLAYERO], 
                                   [provided.EMPTY, provided.PLAYERX, provided.EMPTY]])
        actual_move = ttt_minimax.mm_move(board, provided.PLAYERO)
        exp_move = (0, (2, 0))
        # run the Test #1.8 and compare the expected vs actual output
        suite.run_test(str(actual_move), str(exp_move), 
                       "Test #1.8: mm_move")


        # Test #1.9: test another board configuration for the draw vs loss for PLAYERO
        board = provided.TTTBoard(3, False, 
                                  [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO],
                                   [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX],
                                   [provided.EMPTY, provided.EMPTY, provided.PLAYERO]])
        actual_move = ttt_minimax.mm_move(board, provided.PLAYERO)
        exp_move = (0, (2, 1))
        # run the Test #1.9 and compare the expected vs actual output
        suite.run_test(str(actual_move), str(exp_move), 
                       "Test #1.9: mm_move")
        
        # Test #1.10: test to see if we get the correct score for a 2 by 2
        # board. Since PLAYERX made the first move, current player, PLAYERO
        # will lose no matter what move is selected. Thus, score should be 1
        board = provided.TTTBoard(2, False,
                                  [[provided.PLAYERX, provided.EMPTY],
                                   [provided.EMPTY, provided.EMPTY]])
        actual_score = ttt_minimax.mm_move(board, provided.PLAYERO)[0]
        exp_score = 1
        # run the Test #1.10 and compare the expected vs actual output
        suite.run_test(str(actual_score), str(exp_score), 
                       "Test #1.10: mm_move")


        # Test #1.11: Test the case for a game that just started i.e.
        # the board is empty except for the first move. Since both
        # player are minimzing their losses, it will result in a draw.
        # Therefore, we should get a score of 0
        board = provided.TTTBoard(3, False, 
                                  [[provided.EMPTY, provided.EMPTY, provided.PLAYERX], 
                                   [provided.EMPTY, provided.EMPTY, provided.EMPTY], 
                                   [provided.EMPTY, provided.EMPTY, provided.EMPTY]])
        actual_score = ttt_minimax.mm_move(board, provided.PLAYERO)[0]
        exp_score = 0
        # run the Test #1.11 and compare the expected vs actual output
        suite.run_test(str(actual_score), str(exp_score), 
                       "Test #1.11: mm_move")

        # report number of tests and failures
        suite.report_results()
        print      
    
# test all functions of the word wangler pini-project
minimax_sim = TestTicTacToeMinimax()
minimax_sim.test_mm_move()

