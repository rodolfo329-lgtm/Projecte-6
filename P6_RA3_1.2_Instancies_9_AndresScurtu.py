# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
import math

# Definició de la classe Cercle
class Cercle:
    def __init__(self, radi):
        self.radi = radi

    # Mètode per calcular l'àrea del cercle
    def area(self):
        return math.pi * (self.radi ** 2)

# Creant una llista de cercles
cercles = [
    Cercle(3),   # Àrea = π * 3² ≈ 28.27
    Cercle(5),   # Àrea = π * 5² ≈ 78.54
    Cercle(7),   # Àrea = π * 7² ≈ 153.94
    Cercle(4)    # Àrea = π * 4² ≈ 50.27
]

# Mostrant els cercles amb àrea superior a 50
print("Cercles amb àrea superior a 50:")
for cercle in cercles:
    if cercle.area() > 50:
        print(f"Radi: {cercle.radi}, Àrea: {cercle.area():.2f}")
