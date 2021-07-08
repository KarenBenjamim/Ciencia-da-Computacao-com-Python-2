def soma_matrizes(m1, m2):
    soma = []
    l = len(m1)
    c = len(m1[0])
    if len(m1) == len(m2):
        for i in range(l):
            soma.append([])
            for j in range(c):
                somaMatriz = m1[i][j] + m2[i][j]
                soma[i].append(somaMatriz)
        return soma
    else:
        return False
