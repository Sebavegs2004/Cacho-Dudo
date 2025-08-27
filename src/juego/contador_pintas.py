from src.juego.dado import Dado
from src.juego.cacho import Cacho

class Contador_Pintas:

    def __init__(self):
        self.pintas = [0, 0, 0, 0, 0, 0]

    def clean_count(self):
        self.pintas = [0, 0, 0, 0, 0, 0]

    def contar_pintas(self, cachos, con_comodin):
        self.clean_count()
        for cacho in cachos:
            for valor in cacho.get_valor_dados():
                if valor == 1 and con_comodin:
                    self.pintas = [veces + 1 for veces in self.pintas]
                else:
                    self.pintas[valor - 1] += 1
        return self.pintas