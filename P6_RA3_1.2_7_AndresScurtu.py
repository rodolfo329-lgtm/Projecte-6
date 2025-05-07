# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
import math

class Cercle:
    # Constructor amb el radi
    def __init__(self, radi):
        self.radi = radi

    # Mètode per calcular l'àrea
    def area(self):
        return math.pi * self.radi ** 2

    # Mètode per calcular el perímetre
    def perimetre(self):
        return 2 * math.pi * self.radi

# Exemple d'ús
cercle1 = Cercle(3)
print(f"Àrea: {cercle1.area():.2f}")
print(f"Perímetre: {cercle1.perimetre():.2f}")
