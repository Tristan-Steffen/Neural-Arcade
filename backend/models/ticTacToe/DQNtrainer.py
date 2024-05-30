from games import TicTacToe
from backend.models.ticTacToe.DQNAgent import DQNAgent
import keras
import os

EPISODES = 300
game = TicTacToe.TicTacToe()
agent = DQNAgent()

for e in range(EPISODES):
    game.reset()
    state = game.board.tolist() + [game.current_player]
    done = False
    while not done:
        action = agent.act(state)
        next_state = game.board.tolist() + [game.current_player]
        winner = game.check_winner()
        reward = 0
        if game.move(action):
            if winner is not None:
                if winner == 0:
                    reward = 0.5  # Draw
                else:
                    reward = 1 if winner == 1 else -1
                done = True
            agent.remember(state, action, reward, next_state, done)
            state = next_state
        else:
            reward = -10
            done = True
            agent.remember(state, action, reward, next_state, done)
            state = next_state
    agent.replay(100)
    agent.update_target_model()
    if e % 25 == 0:
        print(f"Episode {e}/{EPISODES}, Epsilon: {agent.epsilon}")
        
# Modell speichern
keras.saving.save_model(agent.model, os.path.join("DQNtrainedModels", "DQNModell.h5"))