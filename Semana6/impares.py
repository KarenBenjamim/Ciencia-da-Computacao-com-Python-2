def encontra_impares(lista):
    impar = []
    
    if len(lista) == 0:
        return []

    i = lista.pop(0)

    if (i % 2) != 0:
            return [i] + encontra_impares(lista)
    return encontra_impares(lista)



lista = [1,2,3,4,5,6,7,8,9]
print(encontra_impares(lista))
     