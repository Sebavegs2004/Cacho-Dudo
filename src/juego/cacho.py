from src.juego.dado import Dado


class Cacho:
    # Clase que representa un "cacho" (conjunto de 5 dados) de un jugador.
    # Permite lanzar dados, agregar o quitar dados, y manejar dados a favor

    def __init__(self, identificador: int = None):
        # Inicializa un cacho con 5 dados.
        self.mostrar_cacho = True
        self.dados = [Dado(), Dado(), Dado(), Dado(), Dado()]
        self.identificador = identificador
        self.dados_a_favor = 0

    def get_valor_dados(self):
        # Devuelve una lista con los valores de los dados actuales.
        return [x.get_valor() for x in self.dados]

    def get_denominacion_dados(self):
        # Devuelve una lista con la denominación de cada dado (ej. "As", "Tonto", etc.).
        return [x.denominacion_valor() for x in self.dados]

    def agitar_cacho(self):
        # Lanza todos los dados del cacho, generando nuevos valores aleatorios.
        for x in self.dados:
            x.lanzar_dado()

    def remove_dado(self) -> None:
        # Elimina un dado del cacho.
        # Si hay dados a favor, primero se disminuye su contador antes de eliminar dados físicos.
        if len(self.dados) > 0:
            if self.dados_a_favor > 0:
                self.dados_a_favor -= 1
            else:
                del self.dados[-1]

    def add_dado(self):
        # Agrega un dado al cacho.
        # Si el cacho ya tiene 5 dados, se suma un dado a favor.
        if len(self.dados) == 5:
            self.dados_a_favor += 1
        else:
            self.dados.append(Dado())

    def get_cantidad_dados(self) -> int:
        # Retorna la cantidad total de dados incluyendo los dados a favor.
        return len(self.dados) + self.dados_a_favor

    def get_identificador(self):
        # Devuelve el identificador del cacho.
        return self.identificador

    def set_mostrar_cacho_true(self):
        # Activa la visualización del cacho al mostrar los dados.
        self.mostrar_cacho = True

    def set_mostrar_cacho_false(self):
        # Desactiva la visualización del cacho al mostrar los dados.
        self.mostrar_cacho = False

    def mostrar_dados(self):
        # Imprime los valores de los dados si mostrar_cacho está activo.
        if self.mostrar_cacho:
            print([x.get_valor() for x in self.dados])

    def __str__(self):
        # Devuelve una representación en string del cacho, mostrando su identificador y valores de dados.
        return f"Cacho {self.identificador}: {self.get_valor_dados()}"
