from src.juego.cacho import Cacho

def test_get_dice_values():
    cacho = Cacho()
    dice_values = cacho.get_valor_dados()
    assert 0 <= len(dice_values) <= 5

