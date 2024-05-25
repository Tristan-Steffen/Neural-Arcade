from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

class ConnectFour:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.board = np.zeros((self.rows, self.columns))
        self.current_player = 1

    def reset(self):
        self.board = np.zeros((self.rows, self.columns))
        self.current_player = 1
        return {'board': self.board.tolist(), 'currentPlayer': self.current_player}

    def move(self, column):
        if not 0 <= column < self.columns:
            return False
        row = next((r for r in range(self.rows - 1, -1, -1) if self.board[r, column] == 0), None)
        if row is None:
            return False
        self.board[row, column] = self.current_player
        self.current_player = 3 - self.current_player  # Switch player
        return True

    def check_winner(self):
        # Check for a win in horizontal, vertical, and both diagonal directions
        for r in range(self.rows):
            for c in range(self.columns - 3):
                if self.board[r, c] == self.board[r, c + 1] == self.board[r, c + 2] == self.board[r, c + 3] != 0:
                    return int(self.board[r, c])

        for r in range(self.rows - 3):
            for c in range(self.columns):
                if self.board[r, c] == self.board[r + 1, c] == self.board[r + 2, c] == self.board[r + 3, c] != 0:
                    return int(self.board[r, c])

        for r in range(self.rows - 3):
            for c in range(self.columns - 3):
                if self.board[r, c] == self.board[r + 1, c + 1] == self.board[r + 2, c + 2] == self.board[r + 3, c + 3] != 0:
                    return int(self.board[r, c])

        for r in range(3, self.rows):
            for c in range(self.columns - 3):
                if self.board[r, c] == self.board[r - 1, c + 1] == self.board[r - 2, c + 2] == self.board[r - 3, c + 3] != 0:
                    return int(self.board[r, c])

        if np.all(self.board != 0):
            return 0  # Draw
        return None  # No winner yet


class TicTacToe:
    def __init__(self):
        self.board = np.zeros(9)
        self.current_player = 1

    def reset(self):
        self.board = np.zeros(9)
        self.current_player = 1
        return self.board.tolist()

    def move(self, position):
        if self.board[position] != 0:
            return False
        self.board[position] = self.current_player
        self.current_player = 3 - self.current_player  # switch player
        return True

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != 0:
                return int(self.board[combo[0]])
        if 0 not in self.board:
            return 0  # Draw
        return None  # No winner yet

tic_tac_toe = TicTacToe()
connect_four = ConnectFour()

@app.route('/reset-tictactoe', methods=['POST'])
def reset_tictactoe():
    return jsonify(tic_tac_toe.reset())

@app.route('/move-tictactoe', methods=['POST'])
def move_tictactoe():
    data = request.get_json()
    position = data.get('position')
    if position is None or not tic_tac_toe.move(position):
        return jsonify({'error': 'Invalid move'}), 400
    winner = tic_tac_toe.check_winner()
    return jsonify({'board': tic_tac_toe.board.tolist(), 'winner': winner, 'currentPlayer': tic_tac_toe.current_player})

@app.route('/reset-connectfour', methods=['POST'])
def reset_connect_four():
    return jsonify(connect_four.reset())

@app.route('/move-connectfour', methods=['POST'])
def move_connect_four():
    data = request.get_json()
    column = data.get('column')
    if column is None or not connect_four.move(column):
        return jsonify({'error': 'Invalid move'}), 400
    winner = connect_four.check_winner()
    return jsonify({'board': connect_four.board.tolist(), 'winner': winner, 'currentPlayer': connect_four.current_player})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

