from src.juego.cacho import Cacho

class GestorPartida: 
    
    __jugadores: list

    def __init__(self, jugadores: int) -> None:
        self.__jugadores = [Cacho() for _ in range(jugadores)]

    def iniciar_partida(self) -> None:
        pass

    def get_usuarios(self) -> int:
        return len(self.__jugadores)

    