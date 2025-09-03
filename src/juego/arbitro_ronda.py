from src.juego.contador_pintas import Contador_Pintas

class Arbitro_Ronda:
    # Clase encargada de arbitrar las rondas del juego Dudo/Cacho.
    # Se encarga de validar apuestas, administrar aciertos o fallos
    # y modificar la cantidad de dados de los jugadores según corresponda.

    def __init__(self):
        # Inicializa el árbitro de la ronda.
        # Crea un contador de pintas y un índice que mapea los nombres de pintas a posiciones.
        self.contador_pintas = Contador_Pintas()
        self.indices = {
            "as": 0,
            "tonto": 1,
            "tren": 2,
            "cuadra": 3,
            "quina": 4,
            "sexta": 5
        }

    def calzar(self, jugador_calza, jugadores, apuesta_actual, ronda_especial):
        # Verifica si un jugador logra "calzar" (adivinar exactamente) la apuesta actual.
        # Si el número exacto de dados coincide con la apuesta, el jugador gana un dado.
        # Si no coincide, el jugador pierde un dado.
        if self.contador_pintas.contar_pintas(jugadores, ronda_especial)[self.indices[apuesta_actual[1]]] == apuesta_actual[0]:
            print("Acertaste")
            jugador_calza.add_dado()
        else:
            print("Fallaste")
            jugador_calza.remove_dado()

    def dudar(self, jugador_duda, jugador_apuesta, jugadores, apuesta_actual, ronda_especial):
        # Permite que un jugador dude de la apuesta realizada por otro.
        # Si la apuesta era válida (hay al menos esa cantidad de dados), el jugador que dudó pierde un dado.
        # Si la apuesta era inválida (hay menos de lo apostado), el jugador que apostó pierde un dado.
        if self.contador_pintas.contar_pintas(jugadores, ronda_especial)[self.indices[apuesta_actual[1]]] >= apuesta_actual[0]:
            print("Fallaste")
            jugador_duda.remove_dado()
        else:
            print("Acertaste")
            jugador_apuesta.remove_dado()
