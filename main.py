from flask import Flask, render_template, jsonify, request, url_for
from blackjack import game
from blackjack import cards

app = Flask(__name__)

@app.route("/")
def index():
    d = cards.Deck()
    card_list = []
    for rank, suit in d.cards:
        card_list.append(rank+"_of_"+suit)
    
    card_list.append('card_back')

    card_urls = {card: url_for('static', filename=f'img/{card}.png') for card in card_list}
    return render_template("index.html", card_urls=card_urls)


@app.route('/chip_total', methods=['GET'])
def chip_total():
    total = game.display_player_chips()
    print(total)
    return jsonify({"chip_total": total})

@app.route('/reset_player_chips', methods=['GET'])
def reset_player_chips():
    total = game.reset_player_chips()
    print(total)
    return jsonify({"chip_total": total})

@app.route('/subtract_bet', methods=['POST'])
def subtract_bet():
    data = request.json
    value = data.get('value', 0)
    game.subtract_bet(value)
    new_total = game.display_player_chips()
    return jsonify({"chip_total": new_total})

@app.route('/add_bet', methods=['POST'])
def add_bet():
    data = request.json
    value = data.get('value', 0)
    game.add_bet(value)
    new_total = game.display_player_chips()
    print(new_total)
    return jsonify({"chip_total": new_total})

@app.route('/reset')
def reset():
    game.reset()
    return '', 204

@app.route('/first_deal', methods=['GET'])
def first_deal():
    cards = game.first_deal()
    p_card_one = cards[0][0]
    p_card_two = cards[0][1]
    d_card_one = cards[1][0]
    d_card_two = 'card_back'
    return jsonify({"p_card_one": p_card_one, 
                    "p_card_two": p_card_two,
                    "d_card_one": d_card_one,
                    "d_card_two": d_card_two})

@app.route('/hit', methods=['GET'])
def hit():
    new_card = game.hit()
    return jsonify({"new_card": new_card})

@app.route('/hit_dealer', methods=['GET'])
def hit_dealer():
    new_card = game.hit_dealer()
    return jsonify({"new_card": new_card})

@app.route('/player_score', methods=['GET'])
def player_score():
    player_score = game.get_player_score()
    return jsonify({'player_score': player_score})

@app.route('/dealer_score', methods=['GET'])
def dealer_score():
    dealer_score = game.get_dealer_score()
    return jsonify({'dealer_score': dealer_score})

@app.route('/check_natural', methods=['GET'])
def check_natural():
    natural = game.check_natural()
    return jsonify({'natural': natural})

@app.route('/flip_card_dealer', methods=['GET'])
def flip_card_dealer():
    card = game.flip_dealer_card()
    return jsonify({"card": card})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)