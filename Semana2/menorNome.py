
def menor_nome(nomes):
    for i in range(len(nomes)):
        nomes[i] = nomes[i].strip()
                
    tamanhoLista= len(nomes)
    tamanhoNome = [len(n) for n in nomes]
    menorNome = min(tamanhoNome)
    menor = []

    for i in range(tamanhoLista):
        n = nomes[i]
        if len(n) == menorNome:
            menor.append(nomes[i].capitalize())
    menor = "".join(menor)
    return menor
