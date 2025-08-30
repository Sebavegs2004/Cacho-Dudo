from src.juego.dado import Dado

class Cacho:
    def __init__(self, identificador: int = None):
        self.dados = [Dado(), Dado(), Dado(), Dado(), Dado()]
        self.identificador = identificador
        self.dados_a_favor = 0

    def get_valor_dados(self):
        return [x.get_valor() for x in self.dados]

    def get_denominacion_dados(self):
        return [x.denominacion_valor() for x in self.dados]

    def agitar_cacho(self):
        for x in self.dados:
            x.lanzar_dado()
    
    def remove_dado(self) -> None:
        if len(self.dados) > 1:
            if self.dados_a_favor > 0:
                self.dados_a_favor -= 1
            else:
                del self.dados[-1]

    def add_dado(self):
        if len(self.dados) == 5:
            self.dados_a_favor += 1
        else:
            self.dados.append(Dado())
    
    def get_cantidad_dados(self) -> int:
        return len(self.dados) + self.dados_a_favor

    def get_indentificador(self): 
        return self.identificador 


