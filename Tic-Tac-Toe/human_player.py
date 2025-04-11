from player import Player

class HumanPlayer(Player):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self, board):
        while True:
            try:
                move = input(f"{self.name} ({self.symbol}) - Enter row and column (1-3): ").split()
                row, col = int(move[0]) - 1, int(move[1]) - 1
                if 0 <= row < 3 and 0 <= col < 3:
                    return row, col
                print("Coordinates out of range.")
            except Exception:
                print("Invalid input. Enter two numbers separated by space.")

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name
