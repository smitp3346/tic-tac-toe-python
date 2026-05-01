from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

board = [""] * 9

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
    global board
    board = [""] * 9
    return render_template("game.html")

@app.route("/move", methods=["POST"])
def move():
    global board
    data = request.get_json()
    
    index = data["index"]
    player = data["player"]

    if board[index] == "":
        board[index] = player

    winner = check_winner(player)
    draw = "" not in board and not winner

    return jsonify({
        "board": board,
        "winner": player if winner else None,
        "draw": draw
    })

if __name__ == "__main__":
    app.run(debug=True)