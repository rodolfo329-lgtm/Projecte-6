# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 08/05/2025  
# Versió: 1  
# Descripció:
class Vehicle:
    def moure(self):
        pass  # Mètode base

class Cotxe(Vehicle):
    def moure(self):
        print("El cotxe condueix per la carretera.")

class Bicicleta(Vehicle):
    def moure(self):
        print("La bicicleta pedala pel carril bici.")

class Barca(Vehicle):
    def moure(self):
        print("La barca navega pel riu.")

# Funció per simular moviment
def simular_moviment(vehicles):
    for v in vehicles:
        v.moure()

# Exemple d'ús
vehicles = [Cotxe(), Bicicleta(), Barca()]
simular_moviment(vehicles)
