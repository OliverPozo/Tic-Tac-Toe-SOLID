# api_server.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from TicTacToeOliver import TresEnRayaOliver

app = FastAPI()
juego = TresEnRayaOliver()

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir si quieres
    allow_methods=["*"],
    allow_headers=["*"],
)

class Movimiento(BaseModel):
    fila: int
    columna: int

@app.post("/reiniciar")
def reiniciar():
    juego.reiniciar_juego()
    return {"mensaje": "Juego reiniciado"}

@app.get("/tablero")
def obtener_tablero():
    return juego.obtener_tablero()

@app.post("/mover")
def mover(mov: Movimiento):
    exito = juego.realizar_movimiento(mov.fila, mov.columna)
    return {"exito": exito}

@app.get("/jugador")
def jugador_actual():
    return {"jugador": juego.obtener_jugador_actual()}

@app.get("/ganador")
def ganador():
    return {"ganador": juego.verificar_ganador()}

@app.get("/terminado")
def terminado():
    return {"terminado": juego.esta_juego_terminado()}
