from blackjack.cards import *

class Player:
    def __init__(self):
        self.hand=Hand()
        self.chip_total=2500

    def to_dict(self):
        return {
            'hand': self.hand.to_dict(),
            'chip_total': self.chip_total
        }

    @classmethod
    def from_dict(cls, data):
        player = cls()
        player.hand = Hand.from_dict(data['hand'])
        player.chip_total = data['chip_total']
        return player

class Dealer:
    def __init__(self):
        self.hand=Hand()

    def to_dict(self):
        return {
            'hand': self.hand.to_dict()
        }

    @classmethod
    def from_dict(cls, data):
        dealer = cls()
        dealer.hand = Hand.from_dict(data['hand'])
        return dealer