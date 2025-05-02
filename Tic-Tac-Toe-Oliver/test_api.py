import pytest
from typing import Type
from TicTacToe import JuegoTresEnRaya
from TicTacToeOliver import TresEnRayaOliver

@pytest.fixture
def juego() -> JuegoTresEnRaya:
    # Inyección de dependencia: usamos la interfaz, instanciando la implementación
    return TresEnRayaOliver()

def test_movimiento_valido(juego: JuegoTresEnRaya):
    resultado = juego.realizar_movimiento(0, 0)
    assert resultado is True
    assert juego.obtener_tablero()[0][0] == 'X'

def test_movimiento_en_celda_ocupada(juego: JuegoTresEnRaya):
    juego.realizar_movimiento(1, 1)
    resultado = juego.realizar_movimiento(1, 1)
    assert resultado is False

def test_cambio_de_turno(juego: JuegoTresEnRaya):
    juego.realizar_movimiento(0, 0)
    assert juego.obtener_jugador_actual() == 'O'
    juego.realizar_movimiento(0, 1)
    assert juego.obtener_jugador_actual() == 'X'

def test_movimiento_fuera_de_rango(juego: JuegoTresEnRaya):
    resultado = juego.realizar_movimiento(3, 3)
    assert resultado is False
    resultado = juego.realizar_movimiento(-1, 0)
    assert resultado is False

def test_movimiento_despues_de_ganar(juego: JuegoTresEnRaya):
    # X gana
    juego.realizar_movimiento(0, 0)  # X
    juego.realizar_movimiento(1, 0)  # O
    juego.realizar_movimiento(0, 1)  # X
    juego.realizar_movimiento(1, 1)  # O
    juego.realizar_movimiento(0, 2)  # X gana

    assert juego.verificar_ganador() == 'X'
    resultado = juego.realizar_movimiento(2, 2)  # Ya no se puede mover
    assert resultado is False

# 6. Empate
def test_empate(juego):
    movimientos = [
        (0, 0), (0, 1), (0, 2),
        (1, 1), (1, 0), (1, 2),
        (2, 1), (2, 0), (2, 2)
    ]
    for fila, col in movimientos:
        juego.realizar_movimiento(fila, col)
    assert juego.verificar_ganador() is "Empate"

# 7. Victoria en fila
def test_victoria_en_fila(juego):
    juego.realizar_movimiento(2, 0)
    juego.realizar_movimiento(0, 0)
    juego.realizar_movimiento(2, 1)
    juego.realizar_movimiento(0, 1)
    juego.realizar_movimiento(2, 2)  # X gana
    assert juego.verificar_ganador() == 'X'

# 8. Victoria en columna
def test_victoria_en_columna(juego):
    juego.realizar_movimiento(0, 0)
    juego.realizar_movimiento(0, 1)
    juego.realizar_movimiento(1, 0)
    juego.realizar_movimiento(1, 1)
    juego.realizar_movimiento(2, 0)  # X gana
    assert juego.verificar_ganador() == 'X'

# 9. Victoria en diagonal principal
def test_victoria_diagonal_principal(juego):
    juego.realizar_movimiento(0, 0)
    juego.realizar_movimiento(0, 1)
    juego.realizar_movimiento(1, 1)
    juego.realizar_movimiento(0, 2)
    juego.realizar_movimiento(2, 2)
    assert juego.verificar_ganador() == 'X'

# 10. Victoria en diagonal secundaria
def test_victoria_diagonal_secundaria(juego):
    juego.realizar_movimiento(0, 2)
    juego.realizar_movimiento(0, 0)
    juego.realizar_movimiento(1, 1)
    juego.realizar_movimiento(1, 0)
    juego.realizar_movimiento(2, 0)  # gana
    assert juego.verificar_ganador() is "X"

# 11. Jugador inicial es X
def test_jugador_inicial(juego):
    assert juego.obtener_jugador_actual() == 'X'

# 12. Tablero vacío al inicio
def test_tablero_vacio(juego):
    for fila in juego.obtener_tablero():
        for celda in fila:
            assert celda == ''

# 13. No se puede jugar luego de empate
def test_movimiento_tras_empate(juego):
    movimientos = [
        (0, 0), (0, 1), (0, 2),
        (1, 1), (1, 0), (1, 2),
        (2, 1), (2, 0), (2, 2)
    ]
    for f, c in movimientos:
        juego.realizar_movimiento(f, c)
    assert juego.realizar_movimiento(0, 0) is False

# 14. No se cambia turno en movimiento inválido
def test_turno_no_cambia_si_movimiento_invalido(juego):
    juego.realizar_movimiento(1, 1)
    jugador = juego.obtener_jugador_actual()
    juego.realizar_movimiento(1, 1)  # Movimiento inválido
    assert juego.obtener_jugador_actual() == jugador

# 15. No se puede jugar en tablero lleno
def test_tablero_lleno(juego):
    movimientos = [
        (0, 0), (0, 1), (0, 2),
        (1, 1), (1, 0), (1, 2),
        (2, 1), (2, 0), (2, 2)
    ]
    for f, c in movimientos:
        juego.realizar_movimiento(f, c)
    for i in range(3):
        for j in range(3):
            assert juego.realizar_movimiento(i, j) is False

# 16. Movimiento en todas las esquinas
def test_movimiento_en_esquinas(juego):
    juego.realizar_movimiento(1, 1)
    juego.realizar_movimiento(1, 0)
    juego.realizar_movimiento(1, 2)
    assert juego.realizar_movimiento(2, 2) is True

# 17. El tablero refleja todos los movimientos
def test_tablero_refleja_movimientos(juego):
    juego.realizar_movimiento(0, 0)
    juego.realizar_movimiento(1, 1)
    juego.realizar_movimiento(2, 2)
    tablero = juego.obtener_tablero()
    assert tablero[0][0] == 'X'

# 18. Movimiento en el centro
def test_movimiento_centro(juego):
    assert juego.realizar_movimiento(1, 1) is True

# 19. Movimiento con fila inválida
def test_fila_invalida(juego):
    assert juego.realizar_movimiento(5, 1) is False

# 20. Movimiento con columna inválida
def test_columna_invalida(juego):
    assert juego.realizar_movimiento(1, -2) is False

# 21. Movimiento en la última casilla
def test_movimiento_ultima_casilla(juego):
    # Completa el tablero con movimientos
    juego.realizar_movimiento(0, 0)
    juego.realizar_movimiento(0, 1)
    juego.realizar_movimiento(1, 1)
    juego.realizar_movimiento(1, 0)
    juego.realizar_movimiento(2, 0)
    juego.realizar_movimiento(2, 1)
    juego.realizar_movimiento(1, 2)
    juego.realizar_movimiento(2, 2)
    # El único espacio vacío es (0, 2)
    assert juego.realizar_movimiento(0, 2) is True

# 22. Comprobación de la jugabilidad alternada de jugadores
def test_jugabilidad_alternada(juego):
    juego.realizar_movimiento(0, 0)  # X
    juego.realizar_movimiento(1, 1)  # O
    assert juego.obtener_jugador_actual() == 'X'

# 23. Comprobar si se retorna ganador después de una victoria
def test_retorno_ganador(juego):
    juego.realizar_movimiento(0, 0)  # X
    juego.realizar_movimiento(1, 0)  # O
    juego.realizar_movimiento(0, 1)  # X
    juego.realizar_movimiento(1, 1)  # O
    juego.realizar_movimiento(0, 2)  # X gana
    assert juego.verificar_ganador() == 'X'

# 24. Comprobación de tablero vacío después de reiniciar el juego
def test_reiniciar_juego(juego):
    juego.realizar_movimiento(0, 0)  # X
    juego.realizar_movimiento(1, 1)  # O
    juego.realizar_movimiento(0, 1)  # X
    juego.reiniciar_juego()  # Reiniciar juego
    tablero = juego.obtener_tablero()
    assert all(celda == '' for fila in tablero for celda in fila)

# 25. Verificar que no haya ganador si el tablero está lleno sin victoria
def test_no_ganador_si_tablero_lleno(juego):
    movimientos = [
        (1, 1), (0, 0), (0, 1),
        (2, 1), (1, 0), (1, 2),
        (2, 0), (0, 2), (2, 2)
    ]
    for f, c in movimientos:
        juego.realizar_movimiento(f, c)
    assert juego.verificar_ganador() is "Empate"

