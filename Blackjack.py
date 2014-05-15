# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
order = ""
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
        self.hand = []

    def __str__(self):
        self.hand_str = "Hand contains"
        for i in range(len(self.hand)):
            self.hand_str += " " +str(self.hand[i])
        return  self.hand_str
            
    
    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        self.value = 0
        rank_ls = []
        for i in self.hand:
            rank =i.get_rank()
            self.value += VALUES[rank]
            rank_ls.extend(rank)
        if "A" in rank_ls:
                if self.value <= 11:
                    self.value += 10
                    
        return self.value
                      
   
    def draw(self, canvas, pos):
        for i in range(0, len(self.hand)):
            pos = [pos[0]+CARD_CENTER[0]+ 35, pos[1]]
            card= self.hand[i]
            card.draw(canvas, pos)
            
          
        
# define deck class 
class Deck:
    def __init__(self):
       self.deck =[]
       for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))
                      
    def shuffle(self):
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))
        random.shuffle(self.deck)
        return self.deck

    def deal_card(self):
         
         return self.deck.pop()
        
        
    def __str__(self):
        self.deck_str  = "Deck contains"
        for i in range(0,len(self.deck)):
            self.deck_str += " "+str(self.deck[i])        
        return self.deck_str
    
deck = Deck()
my_hand = Hand()
dealer_hand = Hand()  
#define event handlers for buttons
def deal():
    my_hand.hand = []
    dealer_hand.hand = []
    global outcome, in_play, my_value, dealer_value, first_round, order
    outcome = ""
    first_round = True
    in_play = True
    my_value = 0
    dealer_value = 0
    deck.shuffle()
    my_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    my_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    my_value = my_hand.get_value()
    dealer_value = "?"
    order  ="Hit or stand?"
    

def hit():
    global my_value, outcome, score, in_play, order
    if in_play ==  True:
        my_hand.add_card(deck.deal_card())
        dealer_value = dealer_hand.get_value()
        my_value = my_hand.get_value()
        if my_value > 21:
            in_play = False
            outcome = "You lose"
            score -= 1 
            order = "New deal?"
        else:
            order ="Hit or stand?"
     
    return   
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    global dealer_value, outcome, in_play, score, my_value, dealer_value, first_round, order
    if in_play ==  True:
        dealer_value = dealer_hand.get_value()
        my_value = my_hand.get_value()
        in_play = False
        while dealer_value < 17:
            dealer_hand.add_card(deck.deal_card())
            dealer_value = dealer_hand.get_value()
        if (my_value > dealer_value) and (my_value <= 21):
            outcome = "You win"
            score += 1
            order = "New deal?"
        elif (dealer_value >21) and (my_value <= 21):
            outcome = "You win"
            score += 1
            order = "New deal?"
        else:
            outcome = "You lose"
            score -= 1
            order = "New deal?"
    return

def reset_score():
    global score, in_play
    score = 0
    in_play = False
    deal()
    return

def restart():
    global score, outcome, in_play
    if in_play:
        score -= 1
        outcome = "You lose"
        in_play = False
        deal()
    else:
        deal()
                      

# draw handler    
def draw(canvas):        
    my_hand.draw(canvas, [100, 300])
    dealer_hand.draw(canvas, [100, 100])
    canvas.draw_text(outcome, (20, 500), 40, 'Red')
    canvas.draw_text("Your score: "+ str(score), (320, 40), 40, 'Yellow')
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER , CARD_BACK_SIZE, [CARD_BACK_SIZE[0]+135,100+CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    else:
        dealer_hand.draw(canvas, [100, 100])
    canvas.draw_text("Dealer", (40, 150), 40, 'Black')
    canvas.draw_text("You",  (40, 350), 40, 'Black')
    canvas.draw_text(str(dealer_value), (40, 230), 40, 'Yellow')
    canvas.draw_text(str(my_value), (40, 430), 40, 'Yellow')
    canvas.draw_text(order, (300, 500), 40, 'Red')
    canvas.draw_text("Blackjack", (20, 40), 40, 'Black')
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", restart, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.add_button("Reset score", reset_score, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
