from src.servicios.generador_aleatorio import randInt

class Dado:
    denominacion = ['As','Tonto','Tren','Cuadra','Quina','Sexto']
    def __init__(self, valor = None):
        if valor:
            self.__valor = valor
        else:
            self.__valor = 1

    def get_valor(self):
        return self.__valor

    def lanzar_dado(self):
        self.__valor = randInt(1,6)

    def denominacion_valor(self):
        return self.denominacion[self.__valor-1]