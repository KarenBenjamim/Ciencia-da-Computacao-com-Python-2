import Bhaskara
import pytest

class TestBhaskara:

    @pytest.fixture
    def b(self):
        return Bhaskara.Bhaskara()

    def testaZerRaiz(self):
        assert b.calcula_raiz(10, 10, 10) == (0)

    def testaUmaRaiz(self):
        assert b.calcula_raiz(1, 0, 0) == (1, 0)

    def testaDuasRaiz(self):
        assert b.calcula_raiz(1, -5, 6) == (2, 3, 2)

    def testaRaizNegativa(self):
        assert b.calcula_raiz(10, 20, 10) == (1, -1)