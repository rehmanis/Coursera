# "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

chosen_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, num_guesses
    num_guesses = int(math.ceil(math.log(chosen_range, 2)))
    secret_number = random.randrange(0,chosen_range)
    print ""
    print "New game. Range of number is between 0 to", chosen_range
    print "Number of remaining guesses is", num_guesses
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game    
    global chosen_range
    chosen_range = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global chosen_range
    chosen_range = 1000
    new_game()

    
def input_guess(guess):
    # main game logic goes here
    global num_guesses
    num_guesses -= 1
    guess = int(guess)
    print ""
    print "Guess was", guess
    print "Number of remaining guesses is ", num_guesses

    if (guess == secret_number):
        print "Correct"
        new_game()
    elif (num_guesses <= 0):
        print "you ran out of guesses. Correct number was", secret_number
        new_game()
    elif (guess > secret_number):
        print "Lower"
    else:
        print "Higher"
        
    
# create frame
frame = simplegui.create_frame("Guess the game", 200, 200)

# register event handlers for control elements and start frame
frame.add_input("Please enter your guess", input_guess, 100)
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)

# call new_game 
new_game()
