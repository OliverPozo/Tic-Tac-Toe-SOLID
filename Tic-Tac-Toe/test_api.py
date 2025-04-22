#make_move 
import pytest
from api import TicTacToeAPI
from player import Player

class MockPlayer(Player):
    def __init__(self, name, symbol, moves=None):
        super().__init__(name, symbol)
        self.moves = moves or []

    def get_move(self, board):
        return self.moves.pop(0)

@pytest.fixture
def api():
    p1 = MockPlayer("P1", "X")
    p2 = MockPlayer("P2", "O")
    return TicTacToeAPI(p1, p2)

def test_make_move_success(api):
    assert api.make_move(0, 0) is True
    assert api.get_board()[0][0] == "X"

def test_make_move_occupied_cell(api):
    api.make_move(0, 0)
    assert api.make_move(0, 0) is False

def test_make_move_changes_turn(api):
    api.make_move(0, 0)
    assert api.current_player_symbol() == "O"

def test_make_move_winning(api):
    # Simula jugadas para que gane X
    api.make_move(0, 0)  # X
    api.make_move(1, 0)  # O
    api.make_move(0, 1)  # X
    api.make_move(1, 1)  # O
    api.make_move(0, 2)  # X gana

    assert api.game_over() is True
    assert api.winner() == "P1"
