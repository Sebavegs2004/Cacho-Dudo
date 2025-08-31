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
    
    def formatear_apuesta(self, apuesta_nueva: str) -> tuple:
        partes = apuesta_nueva.split(" ")
        
        if len(partes) != 2:
            return None
        
        try:
            valor = int(partes[0])

            if not 0 < valor < 7:
                return None

            tipo = partes[1]

            if tipo not in ["as", "tonto", "tren", "cuadra", "quina", "sexta"]:
                return None
            
            return (valor, tipo)
        
        except ValueError:
            return None

    def procesar_apuesta(self, apuesta_nueva: str) -> bool:
        apuesta_nueva = self.formatear_apuesta(apuesta_nueva)

        if apuesta_nueva is None: 
            return False

        if ValidarApuesta.es_valida(self.__apuesta_actual, apuesta_nueva, self.__ronda, self.__ronda_especial): 
            self.__apuesta_actual = apuesta_nueva
            return True
        return False 
