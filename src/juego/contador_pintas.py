from src.juego.dado import Dado
from src.juego.cacho import Cacho

class Contador_Pintas:
    # Clase que se encarga de contar las pintas (valores) de los dados
    # de uno o varios cachos. Puede considerar o no los comodines (ases).

    def __init__(self):
        # Inicializa el contador de pintas.
        self.pintas = [0, 0, 0, 0, 0, 0]

    def clean_count(self):
        # Reinicia el conteo de pintas a cero.
        self.pintas = [0, 0, 0, 0, 0, 0]

    def contar_pintas(self, cachos, con_comodin):
        # Cuenta las pintas de todos los dados en los cachos proporcionados.
        self.clean_count()
        for cacho in cachos:
            for valor in cacho.get_valor_dados():
                if valor == 1 and con_comodin:
                    # Si es un comodín, sumar uno a cada pinta.
                    self.pintas = [veces + 1 for veces in self.pintas]
                else:
                    # Si no es comodín, sumar uno a la posición correspondiente.
                    self.pintas[valor - 1] += 1
        return self.pintas
