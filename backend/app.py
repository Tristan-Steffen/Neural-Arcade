from flask import Flask, request, jsonify
from flask_cors import CORS
from games.TicTacToe import TicTacToe
from games.ConnectFour import ConnectFour
from games.GameOfLife import GameOfLife
from models.ticTacToe.DQNAgent import DQNAgent
import os
import numpy as np

app = Flask(__name__)
CORS(app)

dqnAgent = DQNAgent()
dqnAgent.model.load_weights(os.path.join("models", "ticTacToe", "DQNtrainedModels", "DQNModell.h5"))
tic_tac_toe = TicTacToe()
connect_four = ConnectFour()
game_of_life = GameOfLife()

#TIcTacToe
@app.route('/tictactoe-reset', methods=['POST'])
def reset_tictactoe():
    print("reset_tictactoe")
    print(tic_tac_toe.reset())
    return jsonify(tic_tac_toe.reset())

@app.route('/tictactoe-movee', methods=['POST'])
def move_tictactoe():
    data = request.get_json()
    position = data.get('position')
    if position is None or not tic_tac_toe.move(position):
        return jsonify({'error': 'Invalid move'}), 400
    winner = tic_tac_toe.check_winner()
    return jsonify({'board': tic_tac_toe.board.tolist(), 'winner': winner, 'currentPlayer': tic_tac_toe.current_player})

@app.route('/tictactoe-move', methods=['POST'])
def agent_move_tictactoe():
    print("start")
    data = request.get_json()
    position = data.get('position')
    if position is None or not tic_tac_toe.move(position):
        print("Missing state")
        return jsonify({'error': 'Missing state'}), 400
    winner = tic_tac_toe.check_winner()
    if winner is not None:
        print("Winner is not None")
        return jsonify({'board': tic_tac_toe.board.tolist(), 'winner': winner, 'currentPlayer': tic_tac_toe.current_player})
    # Agent move
    action = dqnAgent.model.predict(np.array(tic_tac_toe.board.tolist() + [tic_tac_toe.current_player]).reshape(1, 10))[0]
    print("action")
    print(action)
    print("input")
    print(tic_tac_toe.board.tolist() + [tic_tac_toe.current_player])
    if not tic_tac_toe.move(np.argmax(action)):
        print("error")
        return jsonify({'error': 'Invalid move'}), 400
    winner = tic_tac_toe.check_winner()
    print("winner")
    print(winner)
    return jsonify({'board': tic_tac_toe.board.tolist(), 'winner': winner, 'currentPlayer': tic_tac_toe.current_player})

#ConnectFour
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


#GameOfLife
@app.route('/gameoflife-reset', methods=['POST'])
def reset_game_of_life():
    data = request.get_json()
    rows = data.get('rows')
    columns = data.get('columns')
    if rows is None or columns is None:
        return jsonify({'error': 'Missing rows or columns'}), 400
    return jsonify(game_of_life.reset(rows, columns))

@app.route('/gameoflife-set', methods=['POST'])
def set_game_of_life_cell():
    data = request.get_json()
    row = data.get('row')
    column = data.get('column')
    state = data.get('state', 1)
    if row is None or column is None or not game_of_life.set_cell(row, column, state):
        return jsonify({'error': 'Invalid cell position'}), 400
    return jsonify({'board': game_of_life.board.tolist()})

@app.route('/gameoflife-step', methods=['POST'])
def step_game_of_life():
    return jsonify(game_of_life.step())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')