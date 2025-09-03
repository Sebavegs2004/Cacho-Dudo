from src.juego.cacho import Cacho
from src.juego.validador_apuesta import ValidarApuesta
from src.juego.arbitro_ronda import Arbitro_Ronda
from random import randrange


class GestorPartida:
    # Clase que gestiona toda la lógica de una partida de Cacho/Dudo.
    # Controla jugadores, turnos, apuestas, dudas/calzos y rondas especiales.

    __jugadores: list
    __especial_disponible: list
    __apuesta_actual: tuple
    __turno: int
    __ronda: int
    __ronda_con_comodin: bool
    __sentido: int

    def __init__(self, jugadores: int) -> None:
        # Inicializa la partida con un número de jugadores.
        # Inicializa:
        #   - lista de jugadores con su cacho
        #   - disponibilidad de rondas especiales
        #   - turno inicial
        #   - apuesta actual vacía
        #   - ronda especial activa
        #   - contador de ronda
        self.__jugadores = [Cacho(identificador + 1) for identificador in range(jugadores)]
        self.__especial_disponible = [True] * jugadores
        self.__turno = self.definir_turnos()
        self.__apuesta_actual = ()
        self.__ronda_con_comodin = True
        self.__ronda = 0

    def jugador_dispone_especial(self, jugador):
        # Verifica si un jugador puede usar su ronda especial (solo si tiene 1 dado).
        return self.__especial_disponible[jugador - 1] and self.__jugadores[jugador - 1].get_cantidad_dados() == 1

    def procesar_comodin(self):
        # Determina si la ronda puede usar comodines (ases) según dados de los jugadores.
        self.__ronda_con_comodin = True
        for jugador in self.__jugadores:
            if jugador.get_cantidad_dados() == 1:
                self.__ronda_con_comodin = False
                break
        return self.__ronda_con_comodin

    def iniciar_partida(self, turno: int = 0) -> None:
        # Inicia la partida y lanza los dados de todos los jugadores.
        self.__ronda = 1
        for jugador in self.__jugadores:
            jugador.agitar_cacho()
        self.__apuesta_actual = ()

    def get_usuarios(self) -> int:
        # Retorna la cantidad de jugadores actuales.
        return len(self.__jugadores)

    def formatear_apuesta(self, apuesta_nueva: str) -> tuple:
        # Valida y formatea una apuesta escrita como string a una tupla (cantidad, pinta).
        # Retorna None si la apuesta no es válida.
        partes = apuesta_nueva.lower().split(" ")

        if len(partes) != 2:
            return None

        try:
            valor = int(partes[0])
            if not 0 < valor:
                return None

            tipo = partes[1]
            if tipo not in ["as", "tonto", "tren", "cuadra", "quina", "sexta"]:
                return None

            return (valor, tipo)

        except ValueError:
            return None

    def procesar_apuesta(self, apuesta_nueva: str) -> bool:
        # Procesa una nueva apuesta.
        # Retorna True si la apuesta es válida y se actualiza la apuesta actual.
        apuesta_nueva = self.formatear_apuesta(apuesta_nueva)

        if apuesta_nueva is None:
            return False

        if ValidarApuesta.es_valida(self.__apuesta_actual, apuesta_nueva, self.__ronda, self.__ronda_con_comodin):
            self.__apuesta_actual = apuesta_nueva
            return True
        return False

    def procesar_duda_o_calzo(self, operacion: str):
        # Procesa la acción de "dudar" o "calzar" una apuesta según el turno actual.
        arbitro = Arbitro_Ronda()

        print("\n\n Dados en juego: ")
        for i in self.__jugadores:
            print(i)

        if operacion == "D":
            # Llama al árbitro para procesar la duda
            arbitro.dudar(self.__jugadores[self.__turno], self.__jugadores[self.__turno - 1 % len(self.__jugadores)], self.__jugadores, self.__apuesta_actual, self.__ronda_con_comodin)
        elif operacion == "C":
            # Llama al árbitro para procesar el calzo
            arbitro.calzar(self.__jugadores[self.__turno], self.__jugadores, self.__apuesta_actual, self.__ronda_con_comodin)

        self.__ronda = 1

    def eliminar_jugador_sin_dados(self) -> str:
        # Elimina jugadores que se quedaron sin dados.
        self.__jugadores = [jugador for jugador in self.__jugadores if jugador.get_cantidad_dados() > 0]
        return f"Quedan {len(self.__jugadores)} jugadores en la partida."

    def definir_turnos(self) -> int:
        # Determina aleatoriamente el primer turno de la partida.
        return randrange(len(self.__jugadores)) % len(self.__jugadores)

    def sentido_turnos(self, sentido: str) -> None:
        # Define el sentido del juego: horario (H) o antihorario (A)
        if sentido == "H": self.__sentido = 1
        elif sentido == "A": self.__sentido = -1

    def siguiente_turno(self) -> None:
        # Avanza al siguiente turno según el sentido y aumenta el contador de ronda.
        self.__turno = (self.__turno + self.__sentido) % len(self.__jugadores)
        self.__ronda += 1
        print(f"Turno del jugador {self.__jugadores[self.__turno].get_identificador()}")

    def get_jugador_actual(self) -> int:
        # Retorna el identificador del jugador cuyo turno es actual.
        return self.__jugadores[self.__turno].get_identificador()

    def get_dados_jugador_actual(self):
        # Muestra los dados del jugador actual.
        self.__jugadores[self.__turno].mostrar_dados()

    def get_dados_contrincantes_actual(self):
        # Muestra los dados de los jugadores contrincantes (excepto el jugador actual).
        for jugador in self.__jugadores:
            if jugador != self.__jugadores[self.__turno]:
                jugador.mostrar_dados()

    def activar_especial(self, jugador_actual):
        # Marca que un jugador ha usado su ronda especial y ya no está disponible.
        self.__especial_disponible[jugador_actual - 1] = False
