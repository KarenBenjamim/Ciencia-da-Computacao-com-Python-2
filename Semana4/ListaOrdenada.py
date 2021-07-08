def ordenada(lista):
    x = 0
    for i in range(len(lista)):
        x = i + 1
        if x < len(lista):
            if lista[i] > lista[x]:
                return False

    return True
