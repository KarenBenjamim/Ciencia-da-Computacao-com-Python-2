import math

class Bhaskara:
    def delta(self, a, b, c):
        return b ** 2 - 4 * a * c

    def main(self):
        a = float(input("digite o valor de a: "))
        b = float(input("digite o valor de b: "))
        c = float(input("digite o valor de c: "))
        print(self.calcula_raiz(a, b, c))

    def calcula_raiz(self, a, b, c):
        d = self.delta(a, b, c)
        if d < 0:
            return 0
        else:
            if d == 0:
                raiz1 = (-b + math.sqrt(d)) / (2 * a)
                return 1, raiz1
            else:
                raiz1 = (-b + math.sqrt(d)) / (2 * a)
                raiz2 = (-b - math.sqrt(d)) / (2 * a)
                return 2, raiz1, raiz2