# Texas Hold Em' for the CLI
    # Card Deck and it's functions

# Written by GH on 2-3-2020
import itertools
from random import shuffle

class cards(object):
    def __init__(self):
        suits = ['♦','♥','♣','♠']
        values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.deck = list(itertools.product(values, suits))

    def shuff(self):
        shuffle(self.deck)
    
    def deal(self, num_cards):
        return [self.deck.pop() for i in range(num_cards)]
    
    def burn(self):
        self.deck.pop()
