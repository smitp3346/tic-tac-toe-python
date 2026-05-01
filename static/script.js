let currentPlayer = "X";
let board = ["", "", "", "", "", "", "", "", ""];
let gameOver = false;

function makeMove(index) {
    if (board[index] !== "" || gameOver) return;

    fetch("/move", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            index: index,
            player: currentPlayer
        })
    })
    .then(res => res.json())
    .then(data => {
        board = data.board;
        updateBoard();

        if (data.winner) {
            gameOver = true;
            document.getElementById("status").innerText =
                data.winner + " Wins 🎉";
        }
        else if (data.draw) {
            gameOver = true;
            document.getElementById("status").innerText =
                "Draw 🤝";
        }
        else {
            currentPlayer = currentPlayer === "X" ? "O" : "X";
        }
    });
}

function updateBoard() {
    let cells = document.getElementsByClassName("cell");

    for (let i = 0; i < 9; i++) {
        cells[i].innerText = board[i];
    }
}