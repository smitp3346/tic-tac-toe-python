from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

board = [""] * 9
game_over = False


def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]] == player:
            return True
    return False


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/game")
def game():
    global board, game_over
    board = [""] * 9
    game_over = False
    return render_template("game.html")


@app.route("/move", methods=["POST"])
def move():
    global board, game_over

    if game_over:
        return jsonify({
            "board": board,
            "winner": None,
            "draw": False
        })

    data = request.get_json()
    index = data["index"]
    player = data["player"]

    if board[index] == "":
        board[index] = player

    winner = check_winner(player)
    draw = "" not in board and not winner

    if winner:
        game_over = True

    return jsonify({
        "board": board,
        "winner": player if winner else None,
        "draw": draw
    })


if __name__ == "__main__":
    app.run(debug=True)