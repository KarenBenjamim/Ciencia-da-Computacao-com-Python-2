import ordenador
import random
import time

class contaTempo:
    def listaAleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista
    
    def listaQuaseOrdenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara(self, n):
        print("--------------------------------------------")
        print("Comparando com uma lista não ordenada")        
        print("--------------------------------------------")
        lista1 = self.listaAleatoria(n)
        lista2 = lista1[:]
        lista3 = lista1[:]

        o = ordenador.ordenador()

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("A bolha demorou: ", depois - antes)

        antes = time.time()
        o.bolhaCurta(lista2)
        depois = time.time()
        print("A bolha curta demorou: ", depois - antes)

        antes = time.time()
        o.selecao_direta(lista3)
        depois = time.time()
        print("A seleção direta demorou: ", depois - antes)

    def comparaQuaseOrdenada(self, n):
        print("--------------------------------------------")
        print("Comparando com uma lista quase ordenada")        
        print("--------------------------------------------")
        lista1 = self.listaQuaseOrdenada(n)
        lista2 = lista1[:]
        lista3 = lista1[:]

        o = ordenador.ordenador()

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("A bolha demorou: ", depois - antes)

        antes = time.time()
        o.bolhaCurta(lista2)
        depois = time.time()
        print("A bolha curta demorou: ", depois - antes)

        antes = time.time()
        o.selecao_direta(lista3)
        depois = time.time()
        print("A seleção direta demorou: ", depois - antes)

c = contaTempo()
print(c.compara(1000), c.compara(500))
print(c.comparaQuaseOrdenada(1000), c.comparaQuaseOrdenada(500))