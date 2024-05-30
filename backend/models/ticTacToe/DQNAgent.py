import numpy as np
import keras
from keras import Sequential
from keras.src.layers import Flatten, Dense
from collections import deque
import random

class DQNAgent:
    def __init__(self):
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.model = self.build_model()
        self.target_model = self.build_model()
        self.target_model.set_weights(self.model.get_weights())
        self.memory = deque(maxlen=2000)

    def build_model(self):
        model = Sequential([
            Flatten(input_shape=(10,)),  # Flattening input shape (9,)
            Dense(512, activation='relu'),
            Dense(9, activation='linear')
        ])
        model.compile(optimizer=keras.optimizers.Adam(self.learning_rate), 
                      loss='mse')
        return model

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.choice(np.where(np.array(state) == 0)[0])
        act_values = self.model.predict(np.array(state).reshape(1, 10), verbose=0)
        return np.argmax(act_values[0])

    def interact(self, state):
        act_values = self.model.predict(np.array(state).reshape(1, 10), verbose=0)
        return np.argmax(act_values[0])
    
    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def replay(self, batch_size):
        if len(self.memory) < batch_size:
            return

        minibatch = random.sample(self.memory, batch_size)
        states = np.array([transition[0] for transition in minibatch])
        actions = np.array([transition[1] for transition in minibatch])
        rewards = np.array([transition[2] for transition in minibatch])
        next_states = np.array([transition[3] for transition in minibatch])
        dones = np.array([transition[4] for transition in minibatch])
        next_q_values = self.target_model.predict(next_states, verbose=0)
        targets = rewards + self.gamma * np.amax(next_q_values, axis=1) * (1 - dones)
        target_f = self.model.predict(states, verbose=0)

        for i, action in enumerate(actions):
            target_f[i][action] = targets[i]

        self.model.fit(states, target_f, epochs=1, verbose=1)

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def update_target_model(self):
        self.target_model.set_weights(self.model.get_weights())