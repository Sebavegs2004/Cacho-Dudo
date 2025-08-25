from src.juego.dado import Dado

class Cacho:
    def __init__(self, identificador: int = None):
        self.dados = [Dado(), Dado(), Dado(), Dado(), Dado()]
        self.identificador = identificador

    def get_valor_dados(self):
        return [x.get_valor() for x in self.dados]

    def get_denominacion_dados(self):
        return [x.denominacion_valor() for x in self.dados]

    def agitar_cacho(self):
        for x in self.dados:
            x.lanzar_dado()
    
    

    def get_indentificador(self): 
        return self.identificador 


