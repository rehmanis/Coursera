# implementation of card game - Memory

import simplegui
import random

deck_of_cards = []
exposed_cards = []
SIZE_OF_DECK = 16
CARD_WIDTH = 50
CARD_HEIGHT = 100
TXT_SIZE = 50
idx_card1 = 0
idx_card2 = 0
state = 0
tot_turns = 0

# helper function to initialize globals
def new_game():
    global deck_of_cards, exposed_cards, state, tot_turns
    state = 0
    tot_turns = 0
    deck_of_cards = range(SIZE_OF_DECK/2)+ range(SIZE_OF_DECK/2)
    random.shuffle(deck_of_cards)
    exposed_cards = [False]*SIZE_OF_DECK
    label.set_text("Turns = " + str(tot_turns))
    
     
# define event handlers
def mouseclick(pos):
    global exposed_cards, state, idx_card1, idx_card2, tot_turns
    
    curr_exposed_idx = pos[0] // CARD_WIDTH
    
    if not exposed_cards[curr_exposed_idx]:
        if state == 0:
            state = 1
            exposed_cards[curr_exposed_idx] = True
            idx_card1 = curr_exposed_idx
        elif state == 1:
            state = 2
            exposed_cards[curr_exposed_idx] = True
            idx_card2 = curr_exposed_idx
            tot_turns += 1
        elif state == 2:
            if (deck_of_cards[idx_card1] != deck_of_cards[idx_card2]):
                exposed_cards[idx_card1] = False
                exposed_cards[idx_card2] = False

            exposed_cards[curr_exposed_idx] = True
            idx_card1 = curr_exposed_idx
            state = 1
        
        label.set_text("Turns = " + str(tot_turns))
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    i = 0
    for num, is_exposed in zip(deck_of_cards, exposed_cards):
        txt_size = frame.get_canvas_textwidth(str(num), TXT_SIZE)
        if (is_exposed):
            canvas.draw_text(str(num), (txt_size/2 +CARD_WIDTH*i, 
                                        CARD_HEIGHT/2 + TXT_SIZE/2),
                             TXT_SIZE, 'white')
        else:
            canvas.draw_polygon([(CARD_WIDTH * i, 0), 
                                 (CARD_WIDTH * i, CARD_HEIGHT), 
                                 (CARD_WIDTH * (i+1), CARD_HEIGHT),
                                 (CARD_WIDTH * (i+1) , 0)], 1,
                                'gold', 'green')
        i+=1
        


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", CARD_WIDTH * SIZE_OF_DECK, CARD_HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
