from src.juego.contador_pintas import Contador_Pintas

class Arbitro_Ronda:
    def __init__(self):
        self.contador_pintas = Contador_Pintas()
        self.indices = {
            "as": 0,
            "tonto": 1,
            "trenes": 2,
            "cuadra": 3,
            "quina": 4,
            "sexta": 5
        }

    def calzar(self, jugador_calza, jugadores, apuesta_actual, ronda_especial):
        if self.contador_pintas.contar_pintas(jugadores, ronda_especial)[self.indices[apuesta_actual[1]]] == apuesta_actual[0]:
            jugador_calza.add_dado()
        else:
            jugador_calza.remove_dado()

    def dudar(self, jugador_duda, jugador_apuesta, jugadores, apuesta_actual,ronda_especial):
        if self.contador_pintas.contar_pintas(jugadores, ronda_especial)[self.indices[apuesta_actual[1]]] >= apuesta_actual[0]:
            jugador_duda.remove_dado()