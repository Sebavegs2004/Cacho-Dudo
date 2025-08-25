from src.juego.validador_apuesta import ValidarApuesta

def test_apuesta_as_sin_ronda_especial():
    assert not ValidarApuesta.es_valida(apuesta_actual=(1, 'As'), apuesta_nueva=(1, 'As'), ronda=1, ronda_especial=False)

def test_apuesta_inferior_al_anterior():
    assert not ValidarApuesta.es_valida(apuesta_actual=(2, "tren"), apuesta_nueva=(2, "tonto"), ronda=10, ronda_especial=False)

def test_apuesta_numero_a_as_valida():
    assert ValidarApuesta.es_valida(apuesta_actual=(4, "tonto"), apuesta_nueva=(3, "as"), ronda=10, ronda_especial=False)

def test_apuesta_as_a_numero_valida():
    assert ValidarApuesta.es_valida(apuesta_actual=(2, "as"), apuesta_nueva=(5, "tonto"), ronda=10, ronda_especial=False)
