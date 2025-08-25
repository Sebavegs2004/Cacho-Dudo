from src.juego.cacho import Cacho

def test_get_dice_values():
    cacho = Cacho(1)
    dice_values = cacho.get_valor_dados()
    assert 0 <= len(dice_values) <= 5

def test_get_denominaciones():
    cacho = Cacho(1)
    denominacion = ['As', 'Tonto', 'Tren', 'Cuadra', 'Quina', 'Sexto']
    assert all(x in denominacion for x in cacho.get_denominacion_dados())

def test_agitar_cacho():
    cacho = Cacho(1)
    cacho.agitar_cacho()
    assert all(1 <= x <= 6 for x in cacho.get_valor_dados())

def test_get_identificador_cacho():
    cacho = Cacho(5)
    assert cacho.get_indentificador() == 5

def test_get_cantidad_dados():
    cacho = Cacho(1)
    assert cacho.get_cantidad_dados() == 5