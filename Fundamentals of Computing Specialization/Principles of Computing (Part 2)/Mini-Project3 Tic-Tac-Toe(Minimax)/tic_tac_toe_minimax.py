"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    # get the current state of the board
    game_state = board.check_win()
    # check the base case when the game is over
    if (game_state != None):
        return SCORES[game_state], (-1,-1)
    else:
        # initialize a list that will store all moves to be maximized
        moves = []
        # get all the possible empty board positions where the
        # current player can make a move if the game is still in progress
        empty_squares = board.get_empty_squares()
        # iterate over all of these possible empty position on the current
        # board
        for empty_square in empty_squares:  
            # create a copy of the board so as not to mutate the current board
            board_copy = board.clone()
            # make a move on the current empty location of the board copy 
            board_copy.move(empty_square[0], empty_square[1], player)
            # call mm_move recursively to perform depth first search of the
            # current game board's children i.e all possible board layout
            score =  mm_move(board_copy, provided.switch_player(player))[0]
            # if the score is such that the current player has won the game,
            # return that score, and th winning move location (row, col).
            # Otherwise store the score * SCORES[player] and the move location.
            # score * SCORES[player] is needed so that we can maximize the moves
            # for both players rather than maximizing for PLAYERX and minimizing 
            # for PLAYERO
            if (score == SCORES[player]):
                return score, empty_square
            else:
                moves += [(score * SCORES[player], empty_square)]

        # find the move that has the max score. Since the score is multplied 
        # by SCORES[player], we are actually maximizing for one player(PLAYERX)
        # and minimizing for the other(PLAYERO)
        max_move = list(max(moves))
        # change the move back to the original value 
        max_move[0] = max_move[0] * SCORES[player]
        # return this max/minimzied move
        return tuple(max_move)
        

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
