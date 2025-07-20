# 🤖 Tic-Tac-Toe RL Agent

A simple implementation of a Reinforcement Learning agent (Q-learning) that learns to play **Tic-Tac-Toe** through self-play. Built in Python with a modular architecture, this project allows training, evaluation, and human interaction with the AI agent.

---

## 🚀 Features

- ✅ Self-play training using Q-learning
- ✅ ε-greedy exploration strategy
- ✅ Modular architecture
- ✅ Interactive play against the trained agent
- ✅ Easy saving/loading of the Q-table

---

## 🎮 How to Play

### 1. Clone the project

git clone https://github.com/yourusername/tic-tac-toe-rl.git
cd tic-tac-toe-rl


###  2. Install dependencies

pip install -r requirements.txt

### 3. Train the agent

python main.py

-> This trains the agent using Q-learning and saves the learned Q-table to q_table.pkl

### 4. Play against the trained agent

python evaluation/play_against_human.py

-> You'll play as O and the agent plays as X. Enter positions from 0 to 8 like this: 

0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
---------

### 🧠 Learning Algorithm
We use Q-Learning, an off-policy reinforcement learning algorithm. The agent updates its Q-values using the Bellman equation:

Q(s, a) ← Q(s, a) + α * [r + γ * max_a' Q(s', a') - Q(s, a)]

- α = learning rate

- γ = discount factor

- ε = exploration rate

### ⚙️ Hyperparameters:

epsilon=1.0       # exploration rate

alpha=0.1         # learning rate

gamma=0.9         # discount factor

### 📈 Future Improvements

Add GUI for playing

Add training against smarter opponents

Visualize learning curves

Export model to ONNX or similar
