"""
Monte Carlo Tic-Tac-Toe Player
"""
import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
# do not change their names.
NTRIALS = 50        # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
GAME_IN_PROG = None
GAME_OVER = -1
    
# Add your functions here.
def mc_trial(board, player):
    """
    Takes the current game board and the next player to move.
    Plays a game starting with the given player by making
    random moves. the function should modify the board input.
    """
    # while game is in progress
    while (board.check_win() == GAME_IN_PROG):
        # get a list of empty spots on the current game board
        avail_spots = board.get_empty_squares()
        # randomly select the spots from the empty board
        sel_spot_idx = random.randrange(0,len(avail_spots))
        # get the row and column of selected spot
        row = avail_spots[sel_spot_idx][0]
        col = avail_spots[sel_spot_idx][1]
        # place the current player on the spot found on the board
        board.move(row, col, player)
        # switch the player
        player = provided.switch_player(player)
    
    
def mc_update_scores(scores, board, player):
    """
    Takes a grid of scores (a list of lists) with the same 
    dimensions as the Tic-Tac-Toe board, a board from a completed 
    game, and which player the machine player is. It then scores 
    the completed board and update the scores grid. 
    """
    if (board.check_win() != provided.DRAW):
        if (player == board.check_win()):
            # set increment score to positive
            incr_score = 1
        else:
            # set incrment score to negative
            incr_score = -1

        # iterate over the board
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):

                if (player == board.square(row, col)):
                    scores[row][col] += (incr_score * SCORE_CURRENT)
                elif (board.square(row, col) != provided.EMPTY):
                    scores[row][col] += (-incr_score * SCORE_CURRENT)

def get_best_move(board, scores): 
    """
    Takes a current board and a grid of scores and returns the (row, col) 
    of empty square with the maximum score, randomly return one in case of
    more then one maximum score. Returns none if no empty square is present
    """
    # get the locations of empty squares on the game board
    avail_spots = board.get_empty_squares()
    # if not spots available print message and return
    if len(avail_spots) == 0:
        print "no empty squares available"
        return 
    
    # intialize the max score value to be the value of the first available
    # empty square in the list of empty squares
    max_val = scores[avail_spots[0][0]][avail_spots[0][1]]
    # iterate over all available empty squares and update the max score 
    for row, col in avail_spots:
        if scores[row][col] > max_val:
            max_val = scores[row][col]
            
    # store all other occurances of max score if any        
    max_val_locs = [(row, col) for row, col in avail_spots 
                    if max_val == scores[row][col]]
    
    # return either the location of max score or a randomly selected location
    # if more than 1 occurances of max score are present
    return max_val_locs[random.randrange(0, len(max_val_locs))]
    
def mc_move(board, player, trials):
    """
    Takes a current board, which player the machine player 
    is, and the number of trials to run. Uses the 
    Monte Carlo simulation to return a move for the
    machine player in the form of a (row, column)
    """
    # check to see if current game is in progress
    if (board.check_win() == GAME_IN_PROG):
        # initialize a list of lists of all zero values and same dimension
        # as the board
        scores = [[0] * board.get_dim() for dummy_num in range(board.get_dim())]
        for dummy_trial in range(trials):
            # clone the current board configuration to be used for all trials of
            # Monte Carlo(MC) simulation since the MC function mutates the board
            # configuration after MC completion
            board_copy = board.clone()
            # run the MC simulation on a copy of the current board configuration
            mc_trial(board_copy, player)
            # update the scores based on the simulation results
            mc_update_scores(scores, board_copy, player)

        return get_best_move(board, scores)
    else:
        print "Game has already concluded !"


## Test game with the console or the GUI.  Uncomment whichever 
## you prefer.  Both should be commented out when you submit 
## for testing to save time.
# provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
