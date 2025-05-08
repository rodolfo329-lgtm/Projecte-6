# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 08/05/2025  
# Versió: 1  
# Descripció:
class Animal:
    def parlar(self):
        print("L'animal fa un soroll")

class Gos(Animal):
    def parlar(self):
        print("Bup bup!")

class Gat(Animal):
    def parlar(self):
        print("Miau!")

# Exemple d'ús
a = Animal()
g = Gos()
gat = Gat()

a.parlar()     # L'animal fa un soroll
g.parlar()     # Bup bup!
gat.parlar()   # Miau!
