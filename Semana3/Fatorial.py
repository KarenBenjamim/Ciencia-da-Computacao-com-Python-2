import pytest

def fatorial(n):
    if n < 0:
        return 0
        
    i = 1    
    while (n > 1):
        i *= n
        n -= 1
    return i

@pytest.mark.parametrize("entrada, esperado",[
    (0, 1),
    (1, 1),
    (-10, 0),
    (4, 24),
    (5, 120)
    ])
def teste(entrada, esperado):
    assert fatorial(entrada) == esperado

def numeroBinomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n - k))
