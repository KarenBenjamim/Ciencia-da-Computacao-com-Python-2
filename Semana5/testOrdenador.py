import ordenador
import pytest
import contatempo2
import ordenador

class TestOrdendador:
    @pytest.fixture
    def o (self):
        return ordenador.ordenador()

    @pytest.fixture
    def l_quase(self):
        c = contatempo2.contaTempos()
        return c.listaQuaseOrdenada(100)

    @pytest.fixture
    def l_aleatoria(self):
        c = contatempo2.contaTempo()
        return c.listaAleatoria(100)

    def estaOrdenada(self, l):
        for i in rang(len(l)-1):
            if l[i] > l[i+1]:
                return False
        return True

    def testBolhaCurtaAleatoria(self, o, l_aleatoria):
        o.bolhaCurta(l_aleatoria)
        assert self.estaOrdenada(l_aleatoria)

    def testSelecaoDiretaAle(self, o, l_aleatoria):
        o.selecao_direta(l_aleatoria)
        assert self.estaOrdenada(l_aleatoria)

    def testBolhaCurtaQuaseAleatoria(self, o, l_quase):
        o.bolhaCurta(l_quase)
        assert self.estaOrdenada(l_quase)

    def testSelecaoDiretaAle(self, o, l_quase):
        o.selecao_direta(l_quase)
        assert self.estaOrdenada(l_quase)