from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, symbol):
        self._name = name
        self._symbol = symbol

    def get_symbol(self):
        return self._symbol

    def get_name(self):
        return self._name

    @abstractmethod
    def get_move(self, board):
        pass
