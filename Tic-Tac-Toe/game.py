from board import Board

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current = 0
        self.over = False
        self.winner_name = None


    def start(self):
        current = 0
        while True:
            self.board.print_board()
            player = self.players[current]
            print(f"{player.get_name()}'s turn ({player.get_symbol()})")

            row, col = player.get_move(self.board)

            if self.board.place_mark(row, col, player.get_symbol()):
                if self.board.check_win(player.get_symbol()):
                    self.board.print_board()
                    print(f"{player.get_name()} wins!")
                    break
                if self.board.is_full():
                    self.board.print_board()
                    print("It's a draw!")
                    break
                current = 1 - current
            else:
                print("Cell already taken. Try again.")
