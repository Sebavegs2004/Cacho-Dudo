from src.servicios.generador_aleatorio import randInt

class Dado:
    # Clase que representa un dado de 6 caras.
    # Permite obtener su valor, lanzarlo aleatoriamente
    # y obtener la denominación correspondiente a su valor.

    # Denominaciones de los valores del dado
    denominacion = ['As', 'Tonto', 'Tren', 'Cuadra', 'Quina', 'Sexto']

    def __init__(self, valor=None):
        # Inicializa un dado.
        if valor:
            self.__valor = valor
        else:
            self.__valor = 1

    def get_valor(self):
        # Devuelve el valor actual del dado (1 a 6).
        return self.__valor

    def lanzar_dado(self):
        # Asigna un valor aleatorio al dado entre 1 y 6.
        self.__valor = randInt(1,6)

    def denominacion_valor(self):
        # Devuelve la denominación asociada al valor actual del dado.
        return self.denominacion[self.__valor-1]
