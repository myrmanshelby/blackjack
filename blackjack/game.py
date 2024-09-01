from blackjack.players import *
from blackjack.cards import *
from flask import session

def init_game():
    session['player'] = Player().to_dict()
    session['dealer'] = Dealer().to_dict()
    session['deck'] = Deck().to_dict()
    session.modified = True


def display_player_chips():
    player = Player.from_dict(session['player'])
    return player.chip_total

def reset_player_chips():
    player = Player.from_dict(session['player'])
    player.chip_total = 2500
    session['player'] = player.to_dict()
    session.modified = True
    return player.chip_total

def subtract_bet(value):
    player = Player.from_dict(session['player'])
    player.chip_total -= value
    session['player'] = player.to_dict()
    session.modified = True

def add_bet(value):
    player = Player.from_dict(session['player'])
    player.chip_total += value
    session['player'] = player.to_dict()
    session.modified = True

def reset():
    player = Player.from_dict(session['player'])
    dealer = Dealer.from_dict(session['dealer'])
    deck = Deck.from_dict(session['deck'])
    
    player.hand.reset_hand()
    dealer.hand.reset_hand()
    deck.build()

    session['player'] = player.to_dict()
    session['dealer'] = dealer.to_dict()
    session['deck'] = deck.to_dict()
    session.modified = True

def get_card_file_list(cards):
    file_lst = []
    for rank, suit in cards:
        file_lst.append(rank + '_of_' + suit)
    return file_lst

def get_card_file(card):
    return card[0] + '_of_' + card[1]

def get_player_score():
    player = Player.from_dict(session['player'])
    return player.hand.score

def get_dealer_score():
    dealer = Dealer.from_dict(session['dealer'])
    return dealer.hand.score

def check_natural():
    player = Player.from_dict(session['player'])
    dealer = Dealer.from_dict(session['dealer'])

    if dealer.hand.score == 21 and player.hand.score == 21:
        return 'both'
    elif dealer.hand.score == 21:
        return 'dealer'
    elif player.hand.score == 21:
        return 'player'
    else:
        return 'none'

def first_deal():
    player = Player.from_dict(session['player'])
    dealer = Dealer.from_dict(session['dealer'])
    deck = Deck.from_dict(session['deck'])

    player.hand.add_card(deck.deal_one())
    dealer.hand.add_card(deck.deal_one())
    player.hand.add_card(deck.deal_one())
    dealer.hand.add_card(deck.deal_one())

    session['player'] = player.to_dict()
    session['dealer'] = dealer.to_dict()
    session['deck'] = deck.to_dict()
    session.modified = True

    return [get_card_file_list(player.hand.cards), get_card_file_list(dealer.hand.cards)]

def flip_dealer_card():
    dealer = Dealer.from_dict(session['dealer'])
    return get_card_file(dealer.hand.cards[1])

def hit_dealer():
    dealer = Dealer.from_dict(session['dealer'])
    deck = Deck.from_dict(session['deck'])

    new_card = deck.deal_one()
    dealer.hand.add_card(new_card)

    session['dealer'] = dealer.to_dict()
    session['deck'] = deck.to_dict()
    session.modified = True

    return get_card_file(new_card)

def hit():
    player = Player.from_dict(session['player'])
    deck = Deck.from_dict(session['deck'])

    new_card = deck.deal_one()
    player.hand.add_card(new_card)

    session['player'] = player.to_dict()
    session['deck'] = deck.to_dict()
    session.modified = True

    return get_card_file(new_card)