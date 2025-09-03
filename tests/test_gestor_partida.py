from src.juego.gestor_partida import GestorPartida
from unittest.mock import patch


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

def test_eliminar_jugador():
    gestor = GestorPartida(5)
    gestor.iniciar_partida()
    gestor.eliminar_jugador_sin_dados()
    assert gestor.get_usuarios() == 5

@patch("src.juego.dado.randInt", side_effect=[2,2,2,2,2, 2,2,2,2,2])  
def test_de_covertura_duda(mock_rand): 
    gestor = GestorPartida(2)
    gestor.sentido_turnos("H")
    gestor.iniciar_partida()
    gestor.procesar_apuesta("2 tonto")
    gestor.siguiente_turno()
    gestor.procesar_duda_o_calzo("D")
    gestor.eliminar_jugador_sin_dados()
    assert len(gestor._GestorPartida__jugadores[gestor._GestorPartida__turno].get_valor_dados()) == 4


@patch("src.juego.dado.randInt", side_effect=[2,2,2,2,2, 2,2,2,2,2])  
def test_de_covertura_calzar(mock_rand): 
    gestor = GestorPartida(2)
    gestor.sentido_turnos("H")
    gestor.iniciar_partida()
    gestor.procesar_apuesta("2 tonto")
    gestor.siguiente_turno()
    gestor.procesar_duda_o_calzo("C")
    gestor.eliminar_jugador_sin_dados()
    assert len(gestor._GestorPartida__jugadores[gestor._GestorPartida__turno].get_valor_dados()) == 4


@patch("src.juego.dado.randInt", side_effect=[2,2,2,2,2, 2,2,2,2,2])  
def test_de_covertura_apuesta(mock_rand): 
    gestor = GestorPartida(2)
    gestor.sentido_turnos("H")
    gestor.iniciar_partida()
    gestor.procesar_apuesta("2 tonto")
    gestor.siguiente_turno()
    gestor.procesar_apuesta("3 tonto")
    gestor.siguiente_turno()
    gestor.procesar_duda_o_calzo("C")
    gestor.eliminar_jugador_sin_dados()
    assert len(gestor._GestorPartida__jugadores[gestor._GestorPartida__turno].get_valor_dados()) == 4

@patch("src.juego.dado.randInt", side_effect=[2,2,2,5,6, 1,1,3,4,6])  
def test_mock_dados_con_randint(mock_rand):
    gestor = GestorPartida(2)
    gestor.sentido_turnos("H")
    gestor.iniciar_partida()

    # Ahora los jugadores tendrán exactamente los valores que definimos arriba
    dados_j1 = gestor._GestorPartida__jugadores[0].get_valor_dados()
    dados_j2 = gestor._GestorPartida__jugadores[1].get_valor_dados()

    assert dados_j1 == [2,2,2,5,6]
    assert dados_j2 == [1,1,3,4,6]

@patch("src.juego.dado.randInt", side_effect=[2,2,2,2,2, 2,2,2,2,2])
def test_mock_eliminar_jugador(mock_rand):
    gestor = GestorPartida(2)
    gestor.sentido_turnos("H")
    gestor.iniciar_partida()
    
    gestor.procesar_apuesta("2 tonto")
    gestor.siguiente_turno()
    gestor.procesar_duda_o_calzo("D")
    gestor.eliminar_jugador_sin_dados()
    
    while gestor.get_usuarios() != 1:
        gestor.get_dados_jugador_actual()
        gestor.procesar_apuesta("2 quina")
        gestor.siguiente_turno()
        gestor.procesar_apuesta("3 quina")
        gestor.siguiente_turno()
        gestor.procesar_duda_o_calzo("D")
        gestor.eliminar_jugador_sin_dados()
    
    assert gestor.get_usuarios() == 1

def test_jugador_dispone_especial():
    gestor = GestorPartida(2)
    gestor.sentido_turnos("H")
    gestor.iniciar_partida()
    especial1 = gestor.jugador_dispone_especial(gestor.get_jugador_actual())
    gestor.siguiente_turno()
    for i in range(4):
        gestor._GestorPartida__jugadores[gestor.get_jugador_actual()-1].remove_dado()
    especial2 = gestor.jugador_dispone_especial(gestor.get_jugador_actual())
    assert especial1 == False and especial2 == True


def test_procesar_comodin():
    gestor = GestorPartida(2)
    gestor.sentido_turnos("H")
    gestor.iniciar_partida()

    for i in range(4):
        gestor._GestorPartida__jugadores[gestor.get_jugador_actual()-1].remove_dado()
    assert gestor.procesar_comodin() == False

