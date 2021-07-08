def cria_matriz(num_linhas, num_colunas, valor):
    # Matriz é uma lista de listas.
    # Nesse arquivo a função retorna uma matriz com um numero de linhas e coluna.
    matriz = []
    for i in range(num_linhas):
        # cria linha
        linha = []
        for j in range(num_colunas):
            linha.append(valor)
        # cria coluna
        matriz.append(linha)

    return matriz