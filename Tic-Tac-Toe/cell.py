class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.symbol = ' '

    def is_empty(self):
        return self.symbol == ' '

    def set_symbol(self, symbol):
        if self.is_empty():
            self.symbol = symbol
            return True
        return False

    def get_symbol(self):
        return self.symbol
