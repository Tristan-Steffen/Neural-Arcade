from flask import Flask, request, jsonify
from flask_cors import CORS
from games.TicTacToe import TicTacToe
from games.ConnectFour import ConnectFour

app = Flask(__name__)
CORS(app)

tic_tac_toe = TicTacToe()
connect_four = ConnectFour()

@app.route('/tictactoe-reset', methods=['POST'])
def reset_tictactoe():
    return jsonify(tic_tac_toe.reset())

@app.route('/tictactoe-move', methods=['POST'])
def move_tictactoe():
    data = request.get_json()
    position = data.get('position')
    if position is None or not tic_tac_toe.move(position):
        return jsonify({'error': 'Invalid move'}), 400
    winner = tic_tac_toe.check_winner()
    return jsonify({'board': tic_tac_toe.board.tolist(), 'winner': winner, 'currentPlayer': tic_tac_toe.current_player})

@app.route('/connectfour-reset', methods=['POST'])
def reset_connect_four():
    return jsonify(connect_four.reset())

@app.route('/connectfour-move', methods=['POST'])
def move_connect_four():
    data = request.get_json()
    column = data.get('column')
    if column is None or not connect_four.move(column):
        return jsonify({'error': 'Invalid move'}), 400
    winner = connect_four.check_winner()
    return jsonify({'board': connect_four.board.tolist(), 'winner': winner, 'currentPlayer': connect_four.current_player})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
