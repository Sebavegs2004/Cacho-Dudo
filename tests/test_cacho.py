from src.juego.cacho import Cacho
from src.juego.dado import Dado

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
    assert cacho.get_identificador() == 5

def test_get_cantidad_dados():
    cacho = Cacho(1)
    assert cacho.get_cantidad_dados() == 5

def test_eliminar_dados():
    cacho = Cacho(1)
    cacho.remove_dado()
    assert cacho.get_cantidad_dados() == 4

def test_eliminar_dados_a_favor(mocker):
    cacho = Cacho()
    mocker.patch.object(cacho, "dados_a_favor", 2)
    cacho.remove_dado()
    assert cacho.get_cantidad_dados() == 6

def test_añadir_dado(mocker):
    cacho = Cacho()
    mocker.patch.object(cacho, "dados", [Dado(), Dado(), Dado()])
    cacho.add_dado()
    assert cacho.get_cantidad_dados() == 4

def test_añadir_dados_a_favor():
    cacho = Cacho(1)
    cacho.add_dado()
    assert cacho.get_cantidad_dados() == 6

def test_mostrar_cacho(capsys):
    cacho = Cacho(1)
    cacho.mostrar_dados()
    resultado_print = capsys.readouterr()
    assert resultado_print.out == "[1, 1, 1, 1, 1]\n"

