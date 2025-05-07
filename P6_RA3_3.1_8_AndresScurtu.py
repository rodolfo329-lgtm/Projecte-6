# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
class Animal:
    # Constructor amb nom i espècie
    def __init__(self, nom, especie):
        self.nom = nom
        self.especie = especie

    # Mètode per fer un soroll genèric
    def fer_soroll(self):
        print(f"{self.nom} fa un soroll.")

# Exemple d'ús
animal1 = Animal("Toby", "gos")
animal1.fer_soroll()
