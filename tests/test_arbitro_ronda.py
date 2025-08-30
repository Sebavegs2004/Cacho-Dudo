from src.juego.arbitro_ronda import Arbitro_Ronda
from src.juego.cacho import Cacho

def test_calzar_exitoso():
    jugadores = [Cacho(1), Cacho(2)]
    arbitro_ronda = Arbitro_Ronda()
    arbitro_ronda.calzar(jugadores[0], jugadores, (10, 'as'), False)
    assert jugadores[0].get_cantidad_dados() == 6
