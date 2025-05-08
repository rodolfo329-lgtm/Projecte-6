# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 08/05/2025  
# Versió: 1  
# Descripció:
class Animal:
    def fer_soroll(self):
        return "So desconegut"

class Gat(Animal):
    def fer_soroll(self):
        return "Miau"

class Vaca(Animal):
    def fer_soroll(self):
        return "Muuu"

# Funció polimòrfica
def reproduir_soroll(animal):
    print(animal.fer_soroll())

# Exemple d'ús
g = Gat()
v = Vaca()

reproduir_soroll(g)  # Miau
reproduir_soroll(v)  # Muuu
