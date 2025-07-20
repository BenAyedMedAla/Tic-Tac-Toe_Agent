import sys
import os
import pickle

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agent.q_learning_agent import RLAgent
from environment.tic_tac_toe import TicTacToe

def play_vs_agent(trained_agent):
    env = TicTacToe()
    state = env.reset()

    print("🎮 Tic-Tac-Toe: You (O) vs Agent (X)")
    print("Enter positions as numbers (0-8):")
    print("0 | 1 | 2")
    print("---------")
    print("3 | 4 | 5")
    print("---------")
    print("6 | 7 | 8\n")

    env.render()

    while not env.is_done():
        # Agent move
        available = env.available_actions()
        action = trained_agent.choose_action(state, available)
        env.make_move(action, 'X')
        print("\n🤖 Agent played:")
        env.render()

        if env.is_done():
            break

        # Human move
        valid = False
        while not valid:
            try:
                move = int(input("🧍 Your move (0-8): "))
                if move in env.available_actions():
                    env.make_move(move, 'O')
                    valid = True
                else:
                    print("⛔ Invalid move. Try again.")
            except ValueError:
                print("❌ Not a number. Try again.")

        state = env.board.copy()

    # Game over
    print("\n🏁 Game Over")
    winner = env.get_winner()
    if winner == 'X':
        print("🤖 Agent wins!")
    elif winner == 'O':
        print("🎉 You win!")
    else:
        print("🤝 It's a draw!")

if __name__ == "__main__":
    agent = RLAgent(epsilon=0)  # Use trained Q-table only

    # Try loading Q-table
    try:
        with open("q_table.pkl", "rb") as f:
            agent.q_table = pickle.load(f)
            print("✅ Loaded trained Q-table.")
    except FileNotFoundError:
        print("⚠️ No trained Q-table found. Run training first.")
        sys.exit()

    play_vs_agent(agent)
