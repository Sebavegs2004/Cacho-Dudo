from src.juego.dado import Dado

class Cacho:
    def __init__(self):
        self.dados = [Dado(), Dado(), Dado(), Dado(), Dado()]

    def get_valor_dados(self):
        return [x.get_valor() for x in self.dados]

    def agitar_cacho(self):
        for x in self.dados:
            x.lanzar_dado()


