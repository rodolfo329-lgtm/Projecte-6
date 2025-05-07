# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
# Definició de la classe Rectangle
class Rectangle:
    def __init__(self, amplada, alcada):
        self.amplada = amplada
        self.alcada = alcada

    def area(self):
        return self.amplada * self.alcada

# Instanciant tres rectangles amb mides diferents
rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(8, 6)
rectangle3 = Rectangle(7, 4)

# Mostrant l'àrea de cadascun
print(f"Àrea del rectangle 1: {rectangle1.area()} m²")
print(f"Àrea del rectangle 2: {rectangle2.area()} m²")
print(f"Àrea del rectangle 3: {rectangle3.area()} m²")
