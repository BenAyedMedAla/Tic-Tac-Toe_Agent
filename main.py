# main.py
import pickle
from training.train import train_agent

if __name__ == "__main__":
    agent = train_agent(episodes=10000)

    # Save Q-table
    with open("q_table.pkl", "wb") as f:
        pickle.dump(agent.q_table, f)
    print("✅ Q-table saved.")