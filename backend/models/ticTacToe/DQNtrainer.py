from games import TicTacToe
from models.ticTacToe.DQNAgent import DQNAgent
import keras
import os

EPISODES = 2000
game = TicTacToe.TicTacToe()
agent = DQNAgent()

for e in range(EPISODES):
    game.reset()
    state = game.board.tolist() + [game.current_player]
    done = False
    while not done:
        action = agent.act(state)
        valid_move = game.move(action)
        next_state = game.board.tolist() + [game.current_player]
        reward = 0
        if valid_move:
            winner = game.check_winner()
            if winner is not None:
                if winner == 0:
                    reward = 0.5  # Draw
                else:
                    reward = 1 if winner == game.current_player else -1
                done = True
            agent.remember(state, action, reward, next_state, done)
            state = next_state
        else:
            reward = -5
            done = True
            agent.remember(state, action, reward, next_state, done)
    agent.replay(500)
    agent.update_target_model()
    if e % 25 == 0:
        print(f"Episode {e}/{EPISODES}, Epsilon: {agent.epsilon}")

# Save the model
keras.saving.save_model(agent.model, os.path.join("DQNtrainedModels", "DQNModell.h5"))