# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.listOfCards = [] # create a hand object

    def __str__(self):
        s = "Hand contains: "
        for card in self.listOfCards:
            s += str(card) + " " 
        return s	# return a string representation of a hand

    def add_card(self, card):
        self.listOfCards.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0
        ace_present = False
        
        for card in self.listOfCards:
            hand_value += VALUES[card.rank]
            if (card.rank == RANKS[0]):
                ace_present = True
            
        if (ace_present):
            if (hand_value + 10 <= 21):
                hand_value += 10            
                
        return hand_value
    
    def draw(self, canvas, pos):
        i = 0
        for card in self.listOfCards:
            card.draw(canvas, (pos[0] + i * (CARD_SIZE[0]+10), pos[1]))
            i += 1

        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deckOfCards = [Card(suit,rank) for suit in SUITS for rank in RANKS]
         
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deckOfCards)  
        
    def deal_card(self):
        return self.deckOfCards.pop()	# deal a card object from the deck
    
    def __str__(self):
        s = "Deck Contains: "
        for card in self.deckOfCards:
            s += str(card) + " " 
        return s	# return a string representation of a hand

#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, deck, message, score
    
    if (in_play):
        outcome = "Game forfeited. You loose"
        score -= 1
        in_play = False
        message = "New Deal?"
    else:    
        deck = Deck() # create the deck object with cards
        deck.shuffle() # shuffle the cards inside the deck

        player_hand = Hand() # create a hand for the player
        dealer_hand = Hand() # create a hand for the dealer
        # give two cards to both player and the dealier
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        
        outcome = ""
        message = "Hit or stand?"    
        in_play = True

def hit():
    global outcome, in_play, player_hand, deck, score, message
    # if the hand is in play, hit the player
    if (in_play):
        player_hand.add_card(deck.deal_card())
        if (player_hand.get_value() > 21):
            # if busted, assign a message to outcome, update in_play and score
            outcome = "You have busted!"
            message = "New Deal?"
            in_play = False
            score -= 1   
                 
def stand():
    global outcome, in_play, player_hand, dealer_hand, deck, score, message
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if(in_play):
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        
        if (dealer_hand.get_value() > 21):
            outcome = "Dealer Busted. You Win"
            score += 1
        elif (dealer_hand.get_value() >= player_hand.get_value()):
            outcome = "You Loose"
            score -= 1
        else:
            outcome = "You Win"
            score += 1
            
        in_play = False
        message = "New Deal?"

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Black Jack", (CANVAS_WIDTH/4, CANVAS_HEIGHT/12), 30, 'cyan')
    
    canvas.draw_text(message, (CANVAS_WIDTH/2 - 50, CANVAS_HEIGHT*3/4 - CARD_SIZE[1]-20), 30, 'Black')
    canvas.draw_text(outcome, (CANVAS_WIDTH/2 - 50, CANVAS_HEIGHT/2 - CARD_SIZE[1]-20), 30, 'Black')
    canvas.draw_text("Score " + str(score), (CANVAS_WIDTH/2+50, CANVAS_HEIGHT/12), 30, 'Black')
   
    canvas.draw_text("Dealer", (CANVAS_WIDTH/5 - CARD_SIZE[0], CANVAS_HEIGHT/2 - CARD_SIZE[1]-20), 30, 'Black')
    dealer_hand.draw(canvas, (CANVAS_WIDTH/5 - CARD_SIZE[0], CANVAS_HEIGHT/2 - CARD_SIZE[1]))
    
    if (in_play):
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, (CANVAS_WIDTH/5-CARD_CENTER[0], CANVAS_HEIGHT/2-CARD_CENTER[1]), CARD_BACK_SIZE)
    
    canvas.draw_text("Player", (CANVAS_WIDTH/5 - CARD_SIZE[0], CANVAS_HEIGHT*3/4 - CARD_SIZE[1]-20), 30, 'Black')
    player_hand.draw(canvas, (CANVAS_WIDTH/5 - CARD_SIZE[0], CANVAS_HEIGHT*3/4 - CARD_SIZE[1]))
                      
# initialization frame
frame = simplegui.create_frame("Blackjack", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_canvas_background("Green")

# create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
