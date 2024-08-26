from flask import Flask, render_template, jsonify
from blackjack.game import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/chip_total', methods=['GET'])
def chip_total():
    total = display_player_chips()
    print(total)
    return jsonify({"chip_total": total})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)