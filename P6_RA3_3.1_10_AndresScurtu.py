# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
import math

class Punt:
    # Constructor amb les coordenades x i y
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Mètode per calcular la distància a un altre punt
    def calcular_distancia(self, altre_punt):
        distancia = math.sqrt((self.x - altre_punt.x) ** 2 + (self.y - altre_punt.y) ** 2)
        return distancia

# Exemple d'ús
punt1 = Punt(3, 4)
punt2 = Punt(7, 1)

distancia = punt1.calcular_distancia(punt2)
print(f"La distància entre els punts és: {distancia:.2f}")

