def maiusculas(frase):
    letra = []
    for i in range(len(frase)):
        if frase[i] == frase[i].upper() and (frase[i] != " " and frase[i] != "!" and frase[i] != "?"
        and frase[i] != "." and frase[i] != "," and frase[i] != ")" and frase[i] != "2" and frase[i] != "3"):             
            letra.append(frase[i])
    i += 1 
    letras = "".join(letra)          
    return letras
 
print(maiusculas('PrOgRaMaMoS em python!'))