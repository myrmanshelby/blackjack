from cards import *
from players import *

'''
TO DO
* Create round class
    * initialize new deck
    * takes in players
    * takes in bet and subtracts from player
    * resets player hands
    * plays game using blackjack rules
    * declares winner
    * adjusts chips based on rules
* Create game class
    * continues gameplay until chips are gone? need to brainstorm more
'''

# testing deck, hand, and player
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
