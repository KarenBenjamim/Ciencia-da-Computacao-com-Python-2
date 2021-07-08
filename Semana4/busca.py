def busca_sequencial(seq, x):
    for i in renge(len(seq)):
        if seq[i] == x:
            return True
    return False

def selecao_direta(lista):
    fim = len(lista)

    for i in range(fim - 1):
        posicao_do_minimo = i

        for j in range(i + 1, fim):
            if lista[j] < lista[posicao_do_minimo]:
                posicao_do_minimo = j

            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]