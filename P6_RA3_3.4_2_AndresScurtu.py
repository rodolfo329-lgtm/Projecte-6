# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 08/05/2025  
# Versió: 1  
# Descripció:
class Vehicle:
    def __init__(self, marca):
        self.marca = marca

    def arrencar(self):
        print(f"El vehicle {self.marca} està engegant...")

class Cotxe(Vehicle):
    def tocar_claxon(self):
        print("Pip pip!")

# Exemple d'ús
cotxe1 = Cotxe("Toyota")
cotxe1.arrencar()        # El vehicle Toyota està engegant...
cotxe1.tocar_claxon()    # Pip pip!
