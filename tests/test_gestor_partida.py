from src.juego.gestor_partida import GestorPartida

def test_gestor_partida_usuarios():
    gestor = GestorPartida(5)
    assert gestor.get_usuarios() == 5

def test_iniciar_partida():
    gestor = GestorPartida(5)
    gestor.iniciar_partida()
    assert gestor.get_usuarios() == 5

def test_formatear_apuesta():
    gestor = GestorPartida(5)
    assert gestor.formatear_apuesta("3 as") == (3, "as")
    assert gestor.formatear_apuesta("0 tonto") == None
    assert gestor.formatear_apuesta("7 tren") == None
    assert gestor.formatear_apuesta("2 cuadra") == (2, "cuadra")

def test_procesar_apuesta():
    gestor = GestorPartida(5)
    assert gestor.procesar_apuesta("3 as") == True
    assert gestor.procesar_apuesta("0 tonto") == False
    assert gestor.procesar_apuesta("7 tren") == False