# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 08/05/2025  
# Versió: 1  
# Descripció:
import math

class Figura:
    def area(self):
        print("Àrea no definida")

class Quadrat(Figura):
    def __init__(self, costat):
        self.costat = costat

    def area(self):
        return self.costat ** 2

class Cercle(Figura):
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        return math.pi * (self.radi ** 2)

# Exemple d'ús
figura = Figura()
figura.area()  # Àrea no definida

q = Quadrat(4)
print(f"Àrea del quadrat: {q.area()}")  # 16

c = Cercle(3)
print(f"Àrea del cercle: {c.area():.2f}")  # 28.27
