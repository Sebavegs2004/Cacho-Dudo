from src.juego.dado import Dado

class Cacho:
    def __init__(self, identificador: int = None):
        self.dados = [Dado(), Dado(), Dado(), Dado(), Dado()]
        self.identificador = identificador
        self.dados_a_favor = 0
        self.mostrar_cacho = True

    def get_valor_dados(self):
        return [x.get_valor() for x in self.dados]

    def get_denominacion_dados(self):
        return [x.denominacion_valor() for x in self.dados]

    def agitar_cacho(self):
        for x in self.dados:
            x.lanzar_dado()
    
    def remove_dado(self) -> None:
        if len(self.dados) > 0:
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

    def get_identificador(self): 
        return self.identificador

    def set_mostrar_cacho_true(self):
        self.mostrar_cacho = True

    def set_mostrar_cacho_false(self):
        self.mostrar_cacho = False

    def mostrar_dados(self):
        if self.mostrar_cacho:
            print([x.get_valor() for x in self.dados])
    
    def __str__(self):
        return f"Cacho {self.identificador}: {self.get_valor_dados()}"


