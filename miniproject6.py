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
        # create Hand object
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        return ' '.join([str(card) for card in self.cards])

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        ace = False
        value = 0
        for card in self.cards:
            value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                ace = True
        if ace and value + 10 <= 21:
            return value + 10
        else:
            return value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        offset = 0
        for c in self.cards:
            c.draw(canvas,[pos[0]+offset, pos[1]])
            offset += 100
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards_ = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.cards_)

    def deal_card(self):
        # deal a card object from the deck
        return self.cards_.pop()
    
    def __str__(self):
        # return a string representing the deck
        return ' '.join([str(card) for card in self.cards_])


#define event handlers for buttons
def deal():
    global outcome, in_play,score
    global new_deck, new_player, dealer
    # your code goes here
    if in_play:
        score -= 1
        outcome = "You have lost!"
    in_play = True
    new_deck = Deck()
    new_deck.shuffle()
    new_player = Hand()
    dealer = Hand()
    for c in range(2):
        new_player.add_card(new_deck.deal_card())
        dealer.add_card(new_deck.deal_card())
    print new_player
    print dealer

def hit():
    # replace with your code below
    global outcome, in_play, score
    global new_deck, new_player, dealer
    # if the hand is in play, hit the player
    if not in_play:
        return
    if new_player.get_value() <= 21:
        new_player.add_card(new_deck.deal_card())
    if new_player.get_value() > 21:
        outcome = "You have busted and lost!"
        score -= 1
        in_play = False
    print outcome
    print new_player
    print dealer
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    # replace with your code below
    global outcome, in_play, score
    global new_deck, new_player, dealer
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if not in_play:
        return
    while dealer.get_value() < 17:
        dealer.add_card(new_deck.deal_card())
    print "Dealer busts"
    if new_player.get_value() >= dealer.get_value():
        outcome = "You have won"
        score += 1
    elif dealer.get_value() > 21:
        outcome = "You have won"
        score += 1
    else:
        outcome = "You have lost"
        score -= 1
        
    in_play = False
    print new_player
    print dealer
    print outcome
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    canvas.draw_text("Blackjack", (100,100), 48,"Cyan", 'sans-serif')
    canvas.draw_text("Score "+str(score), (350, 100), 36, "Black", 'sans-serif' )
    canvas.draw_text("Dealer", (50, 200), 36, "Black", 'sans-serif')
    canvas.draw_text(outcome, (200, 200), 28, "Black", 'sans-serif')
    canvas.draw_text("Player", (50, 400), 36, "Black", 'sans-serif')
    if in_play:
        canvas.draw_text("Hit or Stand?", (220, 400), 30, "Black", 'sans-serif')
    else:
        canvas.draw_text("New Deal?", (220, 400), 30, "Black", 'sans-serif')
    
    dealer.draw(canvas, (50,220))
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, 
                          (51+CARD_BACK_CENTER[0], 221+CARD_BACK_CENTER[1]) , CARD_SIZE)
    new_player.draw(canvas, (50,420))


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
