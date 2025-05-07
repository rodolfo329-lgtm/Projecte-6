# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
class Rectangle:
    # Constructor amb amplada i alçada
    def __init__(self, amplada, alcada):
        self.amplada = amplada
        self.alcada = alcada

    # Mètode per calcular l'àrea
    def area(self):
        return self.amplada * self.alcada

    # Mètode per calcular el perímetre
    def perimetre(self):
        return 2 * (self.amplada + self.alcada)

# Exemple d'ús
rectangle1 = Rectangle(5, 3)
print("Àrea:", rectangle1.area())
print("Perímetre:", rectangle1.perimetre())
