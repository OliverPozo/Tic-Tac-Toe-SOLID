from cell import Cell

class Board:
    def __init__(self):
        self.board = [[Cell(row, col) for col in range(3)] for row in range(3)]

    def print_board(self):
        cont = 0
        for row in self.board:
            print(" | ".join(cell.get_symbol() for cell in row))
            if(cont < 2): print("-" * 10)
            cont += 1

    def place_mark(self, row, col, symbol):
        return self.board[row][col].set_symbol(symbol)

    def check_win(self, symbol):
        for row in self.board:
            if all(cell.get_symbol() == symbol for cell in row):
                return True

        for col in range(3):
            if all(self.board[row][col].get_symbol() == symbol for row in range(3)):
                return True

        if all(self.board[i][i].get_symbol() == symbol for i in range(3)) or \
           all(self.board[i][2 - i].get_symbol() == symbol for i in range(3)):
            return True

        return False

    def is_full(self):
        return all(cell.get_symbol() != ' ' for row in self.board for cell in row)
