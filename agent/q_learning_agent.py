# agent/q_learning_agent.py

import numpy as np
import random

class RLAgent:
    def __init__(self, epsilon=1.0, alpha=0.1, gamma=0.9):
        self.q_table = {}
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma

    def _get_state_key(self, state):
        return str(state)

    def choose_action(self, state, available_actions):
        key = self._get_state_key(state)
        if key not in self.q_table:
            self.q_table[key] = np.zeros(9)

        if random.random() < self.epsilon:
            return random.choice(available_actions)
        q_values = self.q_table[key]
        return max(available_actions, key=lambda a: q_values[a])

    def update(self, state, action, reward, next_state, done, available_actions_next):
        s, s_ = str(state), str(next_state)
        self.q_table.setdefault(s, np.zeros(9))
        self.q_table.setdefault(s_, np.zeros(9))
        target = reward if done else reward + self.gamma * max(self.q_table[s_][a] for a in available_actions_next)
        self.q_table[s][action] += self.alpha * (target - self.q_table[s][action])
