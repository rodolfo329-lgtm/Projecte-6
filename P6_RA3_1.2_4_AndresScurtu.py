# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
class Producte:
    # Constructor amb nom i preu
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu

    # Mètode per aplicar un descompte (percentatge entre 0 i 100)
    def aplicar_descompte(self, percentatge):
        descompte = self.preu * (percentatge / 100)
        self.preu -= descompte

# Exemple d'ús
producte1 = Producte("Portàtil", 1000)
print(f"Preu abans del descompte: {producte1.preu}€")

producte1.aplicar_descompte(20)
print(f"Preu després del 20% de descompte: {producte1.preu}€")
