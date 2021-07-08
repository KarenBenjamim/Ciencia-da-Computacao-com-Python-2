def bolha(lista):
    fim = (len(lista))

    for i in range(fim-1, 0, -1):
        for j in range(i):
            
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(lista)
                
    return lista

def bolhaCurta(lista):
    fim = (len(lista))

    for i in range(fim-1, 0, -1):
        trocou = False
        for j in range(i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
                print(j, i)
            if not trocou:
                return
    return lista

lista = [5, 2, 1, 3, 4]
print(bolha([5, 1, 4, 2]))