# tres_en_raya_oliver.py
# Esta seria mi API 
from typing import Optional, List
from cell import Cell
from board import Board
from player import Player
from TicTacToe import JuegoTresEnRaya  # Assumes you put your ABC interface here


class TresEnRayaOliver(JuegoTresEnRaya):
    def __init__(self):
        self.reiniciar_juego()

    def reiniciar_juego(self) -> None:
        self.board = Board()
        self.current_symbol = 'X'
        self.winner = None
        self.finished = False

    def realizar_movimiento(self, fila: int, columna: int) -> bool:
        if self.finished or not (0 <= fila < 3 and 0 <= columna < 3):
            return False

        success = self.board.place_mark(fila, columna, self.current_symbol)
        if not success:
            return False

        if self.board.check_win(self.current_symbol):
            self.winner = self.current_symbol
            self.finished = True
        elif self.board.is_full():
            self.winner = "Empate"
            self.finished = True
        else:
            self.current_symbol = 'O' if self.current_symbol == 'X' else 'X'

        return True

    def obtener_tablero(self) -> List[List[str]]:
        return [[cell.get_symbol() if cell.get_symbol() != ' ' else '' for cell in row] for row in self.board.board]

    def verificar_ganador(self) -> Optional[str]:
        return self.winner

    def obtener_jugador_actual(self) -> str:
        return self.current_symbol

    def esta_juego_terminado(self) -> bool:
        return self.finished
