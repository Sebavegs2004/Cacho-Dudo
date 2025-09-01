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
    assert gestor.formatear_apuesta("7 tren") == (7, "tren")
    assert gestor.formatear_apuesta("2 cuadra") == (2, "cuadra")

def test_procesar_apuesta():
    gestor = GestorPartida(5)
    assert gestor.procesar_apuesta("3 as") == True
    assert gestor.procesar_apuesta("0 tonto") == False
    assert gestor.procesar_apuesta("7 tren") == True

def test_procesar_duda_o_calzo():
    gestor = GestorPartida(10)
    gestor.procesar_apuesta("1 tonto")
    assert gestor.procesar_duda_o_calzo(2) == None
    assert gestor.procesar_duda_o_calzo(3) == None

def test_iniciar_partida():
    gestor = GestorPartida(5)
    gestor.iniciar_partida()
    assert gestor.get_usuarios() == 5

def test_identificador_jugador():
    gestor = GestorPartida(1)
    gestor.sentido_turnos("H")
    gestor.iniciar_partida()
    assert gestor.get_jugador_actual() == 1

def test_siguiente_turno():
    gestor = GestorPartida(2)
    gestor.sentido_turnos("H")
    gestor.iniciar_partida()
    gestor.siguiente_turno()
    assert gestor.get_jugador_actual() == 2 or gestor.get_jugador_actual() == 1

def test_formateo_invalido_dos_strings():
    gestor = GestorPartida(5)
    gestor.iniciar_partida()
    assert gestor.formatear_apuesta("as as") == None

def test_apuesta_invalida():
    gestor = GestorPartida(5)
    gestor.sentido_turnos("H")
    gestor.iniciar_partida()
    gestor.procesar_apuesta("3 tonto")
    gestor.siguiente_turno()
    assert gestor.procesar_apuesta("2 tonto") == False