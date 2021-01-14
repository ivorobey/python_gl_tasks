# Task is develop a program to define deck of cards.
# Deck is collection of Card objects. Cards are stored in deck's attribute called cards which is a list.
# Card object has suit (in case you want to use UTF-8 characters I'll list unicode codes):

# Spades: "♠" or "\u2660"
# Hearts "♥" or "\u2665"
# Diamonds: "♦" or "\u2666"
# Clubs: "♣" or "\u2663"
# and value: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A.

# As a additional (optional) task - define a Joker card (empty suit but with value "JOKER").

# You should be able to:
# create new deck (initially sorted)
# shuffle deck it using its shuffle() method
# get last card (by default) or with the given index via pop(index=-1) method
# get random card via get_random() method
# get specific card's position via index() method
# You can realize additional stuff you want - like .pop() moving seen card to the bottom of the deck etc. You can design another deck- or card-related methods.

# Basic recommendations:
# add __repr__ methods so you easy print out the contents of card or deck objects.
import random
class Card:
    suit = ''
    value = ''

    def __init__(self, suit='Spade', value='Q'):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"[{self.value}{self.suit}]"

    def __eq__(self, other):
        return (self.suit,self.value)==(other.suit,other.value)

class Deck:
    def __init__(self,cards=None):
        if cards:
            self.cards = cards.copy()
        else:
            self.cards = [Card(a,b)for a in "\u2660\u2666\u2665\u2663"for b in([str(x) for x in range(2,11)]+list("JQKA"))]

    def __repr__(self):
        return str(self.cards)


    def shuffle(): 
        random.shuffle(self.cards)
        return self.cards

    def pop(num=0): pass
    def random(): pass


def run_some_tests():
    "Define a deck and run some tests!"

    deck = Deck()
    print(deck.pop())
    deck.shuffle()
    print(deck.pop())
    print(deck.pop(23))
    print([str(deck.random()) for i in range(5)])
    
run_some_tests()
