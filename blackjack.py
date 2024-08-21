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
        
class Hand:
    def __init__(self):
        self.cards=[]
        self.score=0
    
    def add_card(self, card):
        self.cards.append(card)
        self.set_score()

    def set_score(self):
        ace_count=0
        self.score=0
        for card in self.cards:
            if card[0] in {'J','Q','K'}:
                self.score+=10
            elif card[0]=='A':
                ace_count+=1
            else:
                self.score+=int(card[0])
        
        for i in range(ace_count):
            if self.score<=10:
                self.score+=11
            else:
                if i>=1 and self.score==21:
                    self.score-=11
                    self.score+=2
                else:
                    self.score+=1
    
    def reset_hand(self):
        self.cards=[]
        self.score=0

class Player:
    def __init__(self):
        self.hand=Hand()
        self.chip_total=2500

    

# testing deck
d = Deck()
d.shuffle()

shelby = Player()
shelby.hand.add_card(d.deal_one())
shelby.hand.add_card(d.deal_one())
print(shelby.hand.cards)
print(shelby.hand.score)

shelby.hand.reset_hand()
shelby.hand.add_card(d.deal_one())
shelby.hand.add_card(d.deal_one())
print(shelby.hand.cards)
print(shelby.hand.score)
