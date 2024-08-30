from blackjack.players import *
from blackjack.cards import *

player = Player()
dealer = Dealer()
deck = Deck()

def display_player_chips():
    return player.chip_total

def subtract_bet(value):
    player.chip_total-=value

def add_bet(value):
    player.chip_total+=value

def get_card_file_list(cards):
    file_lst = []
    for rank, suit in cards:
        file_lst.append(rank+'_of_'+suit)
    return file_lst

def get_card_file(card):
    return card[0]+'_of_'+card[1]

def get_player_score():
    return player.hand.score

def get_dealer_score():
    return dealer.hand.score

def check_natural():
    natural = ''
    if dealer.hand.score==21 and player.hand.score==21:
        natural = 'both'
    elif dealer.hand.score==21:
        natural = 'dealer'
    elif player.hand.score==21:
        natural = 'player'
    else:
        natural = 'none'
    return natural
    
def first_deal():
    player.hand.add_card(deck.deal_one())
    dealer.hand.add_card(deck.deal_one())
    player.hand.add_card(deck.deal_one())
    dealer.hand.add_card(deck.deal_one())
    return [get_card_file_list(player.hand.cards), get_card_file_list(dealer.hand.cards)]

def flip_dealer_card():
    return get_card_file(dealer.hand.cards[1])

def hit_dealer():
    new_card = deck.deal_one()
    dealer.hand.add_card(new_card)
    return get_card_file(new_card)

def hit():
    new_card = deck.deal_one()
    player.hand.add_card(new_card)
    return get_card_file(new_card)