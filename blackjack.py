from random import shuffle

RANKS = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
SUITS = ['clubs','hearts','spades','diamonds']

class Deck:
    def __init__(self):
        self.cards=[]
        self.build()

    def build(self):
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append((rank, suit))

    def shuffle(self):
        shuffle(self.cards)

    def deal_one(self):
        if len(self.cards)>1:
            return self.cards.pop()
        
class Player:
    def __init__(self):
        self.cards=[]
        self.score=0
        self.chip_total=2500
    

d = Deck()
d.shuffle()
print(d.deal_one())
print(len(d.cards))