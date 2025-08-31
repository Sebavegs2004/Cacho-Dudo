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

    def procesar_duda_o_calzo(self, operacion: int):
        arbitro = Arbitro_Ronda()

        print("\n\n Dados en juego: ")
        for i in self.__jugadores:
            print(i)


        if operacion == 2:
            arbitro.dudar(self.__jugadores[self.__turno], self.__jugadores[self.__turno - 1 % len(self.__jugadores)], self.__jugadores, self.__apuesta_actual, self.__ronda_con_comodin)
        elif operacion == 3:
            arbitro.calzar(self.__jugadores[self.__turno], self.__jugadores, self.__apuesta_actual, self.__ronda_con_comodin)

        self.__ronda = 1

    def eliminar_jugador_sin_dados(self) -> str:
        self.__jugadores = [jugador for jugador in self.__jugadores if jugador.get_cantidad_dados() > 0]
        return f"Quedan {len(self.__jugadores)} jugadores en la partida."

    def definir_turnos(self) -> None: 
        # Crear función
        self.__turno = 0

    def siguiente_turno(self) -> None:
        self.__turno = (self.__turno + 1) % len(self.__jugadores)
        self.__ronda += 1
        print(f"Turno del jugador {self.__jugadores[self.__turno].get_identificador()}")

    def get_jugador_actual(self) -> int:
        return self.__jugadores[self.__turno].get_identificador()

    def get_dados_jugador_actual(self): 
        print(self.__jugadores[self.__turno].get_valor_dados())