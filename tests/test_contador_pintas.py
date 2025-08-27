import pytest

from src.juego.contador_pintas import Contador_Pintas
from src.juego.cacho import Cacho
from src.juego.dado import Dado

@pytest.mark.parametrize('con_comodin,expected',[[True,[2,3,3,3,3,2]],[False,[2,1,1,1,1,0]]])
def test_contar_pintas(con_comodin,expected):
    contador = Contador_Pintas()
    cacho1 = Cacho()
    cacho2 = Cacho()
    cacho1.dados = [Dado(), Dado(), Dado(), Dado(), Dado()]
    cacho2.dados = [Dado()]
    cachos = [cacho1, cacho2]
    for cacho in cachos:
        for i,dado in enumerate(cacho.dados):
            dado._Dado__valor = i%6+1
    assert contador.contar_pintas(cachos, con_comodin) == expected
