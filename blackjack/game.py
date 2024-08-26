from blackjack.players import *

player = Player()
dealer = Dealer()

def display_player_chips():
    return player.chip_total

def subtract_bet(value):
    player.chip_total-=value
    
print(display_player_chips())