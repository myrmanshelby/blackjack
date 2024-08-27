from blackjack.players import *
from blackjack.cards import *

player = Player()
dealer = Dealer()
deck = Deck()

def display_player_chips():
    return player.chip_total

def subtract_bet(value):
    player.chip_total-=value

def get_card_file(cards):
    file_lst = []
    for rank, suit in cards:
        file_lst.append(rank+'_of_'+suit)
    return file_lst
    
def first_deal():
    player.hand.add_card(deck.deal_one())
    dealer.hand.add_card(deck.deal_one())
    player.hand.add_card(deck.deal_one())
    dealer.hand.add_card(deck.deal_one())
    return [get_card_file(player.hand.cards), get_card_file(dealer.hand.cards)]