import pytest

from src.juego.dado import Dado
def test_lanzar_dado(mocker):
    mock_randint = mocker.patch("src.juego.dado.random.randint", return_value = 6)
    dado = Dado()
    dado.lanzar_dado()
    assert dado._Dado__valor == 6

def test_get_valor():
    dado = Dado()
    dado._Dado__valor = 6
    assert dado.get_valor() == 6

@pytest.mark.parametrize("test_input,expected",list(enumerate(['As','Tonto','Tren','Cuadra','Quina','Sexto'], start=1)))
def test_denominacion_valor(test_input,expected):
    dado = Dado()
    dado._Dado__valor = test_input
    assert dado.denominacion_valor() == expected
