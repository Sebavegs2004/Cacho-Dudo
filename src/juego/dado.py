from src.servicios.generador_aleatorio import randInt

class Dado:
    def __init__(self):
        self.__valor = 1

    def get_valor(self):
        return self.__valor

    def lanzar_dado(self):
        self.__valor = randInt(1,6)