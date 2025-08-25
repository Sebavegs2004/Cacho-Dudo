from src.juego.validador_apuesta import ValidarApuesta

def test_apuesta_as_sin_ronda_especial():
    assert not ValidarApuesta.es_valida(apuesta_actual=(1, 'As'), apuesta_nueva=(1, 'As'), ronda=1, ronda_especial=False)

def test_apuesta_inferior_al_anterior():
    assert not ValidarApuesta.es_valida(apuesta_actual=(2, "tren"), apuesta_nueva=(2, "tonto"))

# def test_apuesta_numero_a_as_valida():
#     assert ValidarApuesta.es_valida((4, "tonto"), (3, "as"))

# def test_apuesta_as_a_numero_valida():
#     assert ValidarApuesta.es_valida((2, "as"), (5, "tonto"))

# def test_apuesta_numero_a_as_invalida():
#     assert not ValidarApuesta.es_valida((4, "tonto"), (2, "as"))

# def test_apuesta_as_a_numero_invalida():
#     assert ValidarApuesta.es_valida((2, "as"), (4, "tonto"))