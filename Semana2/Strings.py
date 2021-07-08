frase = 'milainy Karen Benjamim Souza'

#a função len diz o teamanho de caractere de uma sting
contador = len(frase)
print(contador)

# o replace substitui os caracteres desejados (o primeiro) pelo segundo 
frase = frase.replace('milainy', 'Milainy')

# conta quantos caracteres desse tem na string
print(frase.count('a'))

# procura na string esse caractere ou conjunto de caracteres
print(frase.find('Karen'))

# separa tudo que esta com espaço por virgula
print(frase.split())

# quando eu coloco a variavel = variavel.algo ele altera

# todas as letras em mausculo
print(frase.upper())

# tudo em minusculos
print(frase.lower())

# a primeira letra em mausculo
print(frase.capitalize())

#  todas as primeiras letras depois do espaço em mausculo
print(frase.title())

# troca, o que é maiusculo fica minusculo e o contrario
print(frase.swapcase())

# centraliliza o texto com o tamanho em numero string
print(frase.center(80))

# acha onde esta quela string
print(frase.find(ai))

# imprime um intervalo 
print(frase[:3]) # tudo ate a 3º posição 
print(frase[3:]) # da posição 3 ate o final
print(frase[3:5]) # da posicao 3 ate 5

# diz o codigo unicode da letra 
ord("a")