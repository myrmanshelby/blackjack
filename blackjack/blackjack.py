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
    def __init__(self, player, dealer, bet):
        self.deck = Deck()
        self.player = player
        self.dealer = dealer
        self.bet = bet

    def deal(self):
        self.player.hand.add_card(self.deck.deal_one())
        self.dealer.hand.add_card(self.deck.deal_one())
        self.player.hand.add_card(self.deck.deal_one())
        self.dealer.hand.add_card(self.deck.deal_one())

    def play(self):
        self.player.chip_total-=self.bet
        self.deck.shuffle()
        self.deal()

        print("Player's Cards: ", self.player.hand.cards)
        print("Dealer's Card: ", self.dealer.hand.cards[0])

        if self.check_naturals():
            return
        if not self.double_down():
            self.players_turn()

        if self.player.hand.score>21:
            self.determine_winner()
        else:
            self.dealers_turn()
            self.determine_winner()

    def check_naturals(self):
        if self.player.hand.score==21 and self.dealer.hand.score==21:
            print("It's a tie!")
            self.player.chip_total+=self.bet
            return True
        elif self.player.hand.score==21:
            print("You're a natural!")
            self.player.chip_total+=int(self.bet*2.5)
            return True
        elif self.dealer.hand.score==21:
            print("Dealer's a natural!")
            print(self.dealer.hand.cards)
            return True
        else:
            return False
        
    def double_down(self):
        if self.player.hand.score in {9, 10, 11}:
            move = input("Double down? Type y/n. ").lower()
            if move=='y':
                self.player.chip_total-=self.bet
                self.bet=self.bet*2
                print("New bet: ", self.bet)
                self.player.hand.add_card(self.deck.deal_one())
                print("Player's Cards: ", self.player.hand.cards)
                return True

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

    def determine_winner(self):
        print("Player Score: ", self.player.hand.score)
        print("Dealer Score: ", self.dealer.hand.score)

        if (self.dealer.hand.score>self.player.hand.score and self.dealer.hand.score<=21) or self.player.hand.score>21:
            print("Dealer wins")
        elif self.player.hand.score==self.dealer.hand.score:
            print("It's a tie!")
            self.player.chip_total+=self.bet
        else:
            print("You win!")
            self.player.chip_total+=self.bet*2




    


        

# testing round

shelby = Player()
dealer = Dealer()

print("Player Chips: ", shelby.chip_total)
r = Round(shelby, dealer, 100)
r.play()

print("Player Chips: ", shelby.chip_total)


