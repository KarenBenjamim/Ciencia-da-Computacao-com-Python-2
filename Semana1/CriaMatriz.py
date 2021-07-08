def cria_matriz(num_linhas, num_colunas):
    # Matriz é uma lista de listas.
    # Nesse arquivo a função retorna uma matriz com um numero de linhas e coluna digitado pelo usuario.
    matriz = []
    for i in range(num_linhas):
        # cria linha
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite o eletmento [", i, "][", j, "]: "))
            linha.append(valor)
        # cria coluna
        matriz.append(linha)

    return matriz

def le_matriz():
    lin = int(input("Digite o numero de linhas da matriz: "))
    col = int(input("Digite o numero de colunas da matriz: "))
    return cria_matriz(lin, col)

le_matriz()