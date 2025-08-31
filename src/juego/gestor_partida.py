from src.juego.cacho import Cacho
from src.juego.validador_apuesta import ValidarApuesta
from src.juego.arbitro_ronda import Arbitro_Ronda

class GestorPartida: 
    
    __jugadores: list
    __apuesta_actual: tuple
    __turno: int
    __ronda: int
    __ronda_con_comodin: bool
    __ronda_especial: bool

    def __init__(self, jugadores: int) -> None:
        self.__jugadores = [Cacho(identificador + 1) for identificador in range(jugadores)]
        self.__turno = 0
        self.__apuesta_actual = ()
        self.__ronda_con_comodin = True
        self.__ronda = 0
        self.__ronda_especial = False

    def iniciar_partida(self, turno: int = 0) -> None:
        self.__ronda = 1
        for jugador in self.__jugadores:
            jugador.agitar_cacho()
        self.__apuesta_actual = ()
    
    def get_usuarios(self) -> int:
        return len(self.__jugadores)