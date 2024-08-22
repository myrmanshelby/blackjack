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

class Round:
    def __init__(self, player, dealer):
        self.deck = Deck()
        self.player = player
        self.dealer = dealer

    def deal(self):
        self.player.hand.add_card(self.deck.deal_one())
        self.dealer.hand.add_card(self.deck.deal_one())
        self.player.hand.add_card(self.deck.deal_one())
        self.dealer.hand.add_card(self.deck.deal_one())

    def play(self, bet_value):
        self.player.chip_total-=bet_value
        self.deck.shuffle()
        self.deal()
        print("Player's Cards: ", self.player.hand.cards)
        print("Dealer's Card: ", self.dealer.hand.cards[0])
        self.players_turn()
        self.dealers_turn()
        self.determine_winner(bet_value)

    def players_turn(self):
        move = input("Hit or stand? Type one. ").lower()
        while move=="hit" and self.player.hand.score<21:
            self.player.hand.add_card(self.deck.deal_one())
            print("Player's Cards: ", self.player.hand.cards)
            if self.player.hand.score<21:
                move = input("Hit or stand? Type one. ").lower()
            else:
                move = "stand"
    
    def dealers_turn(self):
        print("Dealer's Cards: ", self.dealer.hand.cards)
        while self.dealer.hand.score<=16:
            self.dealer.hand.add_card(self.deck.deal_one())
            print("Dealer's Cards: ", self.dealer.hand.cards)

    def determine_winner(self, bet_value):
        print("Player Score: ", self.player.hand.score)
        print("Dealer Score: ", self.dealer.hand.score)

        if self.player.hand.score>self.dealer.hand.score:
            print("You win!")
            self.player.chip_total+=bet_value*2
        elif self.dealer.hand.score>self.player.hand.score:
            print("Dealer wins!")
        else:
            print("It's a tie!")
            self.player.chip_total+=bet_value




    


        

# testing round

shelby = Player()
dealer = Dealer()

print("Player Chips: ", shelby.chip_total)
r = Round(shelby, dealer)
r.play(100)

print("Player Chips: ", shelby.chip_total)


