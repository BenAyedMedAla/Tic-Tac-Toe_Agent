# environment/tic_tac_toe.py

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def reset(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        return self.board.copy()

    def available_actions(self):
        return [i for i, x in enumerate(self.board) if x == ' ']

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            if self.check_winner(player):
                self.current_winner = player
            return True
        return False

    def check_winner(self, player):
        combos = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        return any(all(self.board[i] == player for i in combo) for combo in combos)

    def is_done(self):
        return self.current_winner is not None or ' ' not in self.board

    def get_winner(self):
        return self.current_winner

    def render(self):
        print("\nBoard:")
        for i in range(3):
            print('|'.join(self.board[i*3:(i+1)*3]))
