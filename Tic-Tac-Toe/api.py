# api.py
class TicTacToeAPI:
    def __init__(self, player1, player2):
        from game import Game
        self.game = Game(player1, player2)

    def make_move(self, row, col):
        player = self.game.players[self.game.current]
        success = self.game.board.place_mark(row, col, player.get_symbol())
        if success:
            self._check_game_state(player)
            self.game.current = 1 - self.game.current
        return success

    def get_board(self):
        return [[cell.get_symbol() for cell in row] for row in self.game.board.board]

    def current_player_symbol(self):
        return self.game.players[self.game.current].get_symbol()

    def game_over(self):
        return self.game.over

    def winner(self):
        return self.game.winner_name

    def _check_game_state(self, player):
        if self.game.board.check_win(player.get_symbol()):
            self.game.winner_name = player.get_name()
            self.game.over = True
        elif self.game.board.is_full():
            self.game.over = True
