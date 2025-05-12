# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 12/05/2025  
# Versió: 1  
# Descripció:
class CarretCompra:
    def __init__(self, total, estrategia_descompte):
        self.total = total
        self.estrategia_descompte = estrategia_descompte  # Estratègia externa

    def aplicar_descompte(self):
        self.total = self.estrategia_descompte.aplicar(self.total)

# Exemple de classe d’estratègia de descompte
class Descompte20:
    def aplicar(self, total):
        return total * 0.8

# Ús:
descompte = Descompte20()
carret = CarretCompra(100, descompte)
carret.aplicar_descompte()
print(f"Total amb descompte: {carret.total}")
