from flask import Flask, render_template, jsonify, request
from blackjack import game

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


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

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)