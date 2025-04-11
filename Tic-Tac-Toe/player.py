from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def get_move(self, board):
        pass

    @abstractmethod
    def get_symbol(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
