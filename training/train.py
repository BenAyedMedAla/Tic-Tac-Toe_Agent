# training/train.py

from agent.q_learning_agent import RLAgent
from environment.tic_tac_toe import TicTacToe
import random

def train_agent(episodes=5000):
    env = TicTacToe()
    agent = RLAgent()

    for ep in range(episodes):
        state = env.reset()
        done = False
        player = 'X'
        while not done:
            available = env.available_actions()
            action = agent.choose_action(state, available)
            env.make_move(action, player)
            next_state = env.board.copy()
            reward, done = 0, env.is_done()

            if done:
                winner = env.get_winner()
                if winner == 'X':
                    reward = 1
                elif winner == 'O':
                    reward = -1
                else:
                    reward = 0.5
                agent.update(state, action, reward, next_state, done, [])
                break

            opponent_action = random.choice(env.available_actions())
            env.make_move(opponent_action, 'O')
            state_ = env.board.copy()
            done = env.is_done()
            reward = -1 if env.get_winner() == 'O' else 0

            agent.update(state, action, reward, state_, done, env.available_actions())
            state = state_

        # Decay epsilon
        agent.epsilon = max(agent.epsilon * 0.995, 0.01)

        if ep % 500 == 0:
            print(f"Episode {ep} complete. ε = {agent.epsilon:.4f}")

    return agent
