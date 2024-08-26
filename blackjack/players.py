from blackjack.cards import *

class Player:
    def __init__(self):
        self.hand=Hand()
        self.chip_total=2500

class Dealer:
    def __init__(self):
        self.hand=Hand()