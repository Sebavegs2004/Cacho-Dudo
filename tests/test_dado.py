from src.juego.dado import Dado
def test_lanzar_dado(mocker):
    mock_randint = mocker.patch("src.juego.dado.random.randint", return_value = 6)
    dado = Dado()
    dado.lanzar_dado()
    assert dado.__valor() == 6

def test_get_valor():
    dado = Dado()
    dado.valor = 6
    assert dado.get_valor() == 6