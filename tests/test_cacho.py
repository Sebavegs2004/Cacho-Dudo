from src.juego.cacho import Cacho

def test_get_dice_values():
    cacho = Cacho()
    dice_values = cacho.get_valor_dados()
    assert 0 <= len(dice_values) <= 5

def test_agitar_cacho():
    cacho = Cacho()
    cacho.agitar_cacho()
    dice_values = cacho.get_valor_dados()
    dice_values_in_range = (1 <= x <= 6 for x in dice_values)
    assert all(dice_values_in_range)