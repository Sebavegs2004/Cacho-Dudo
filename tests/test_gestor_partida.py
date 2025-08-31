from src.juego.gestor_partida import GestorPartida

def test_gestor_partida_usuarios():
    gestor = GestorPartida(5)
    assert gestor.get_usuarios() == 5

def test_iniciar_partida():
    gestor = GestorPartida(5)
    gestor.iniciar_partida()
    assert gestor.get_usuarios() == 5