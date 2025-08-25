from src.juego.validador_apuesta import ValidarApuesta

def test_apuesta_as_sin_ronda_especial():
    assert not ValidarApuesta.es_valida(apuesta_nueva=(1, 'As'), ronda=1, ronda_especial=False)

