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

@app.route('/subtract_bet', methods=['POST'])
def subtract_bet():
    data = request.json
    value = data.get('value', 0)
    game.subtract_bet(value)
    new_total = game.display_player_chips()
    print(new_total)
    return jsonify({"chip_total": new_total})

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

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)