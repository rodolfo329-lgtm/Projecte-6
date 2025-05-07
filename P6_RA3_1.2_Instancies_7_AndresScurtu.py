# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
# Definició de la classe Animal
class Animal:
    def __init__(self, nom, especie):
        self.nom = nom
        self.especie = especie

    # Mètode general per fer un soroll
    def fer_soroll(self):
        print(f"{self.nom} fa un soroll.")

# Definició de la classe Gos, que hereta de Animal
class Gos(Animal):
    # Sobreescrivint el mètode fer_soroll() per al Gos
    def fer_soroll(self):
        print(f"{self.nom} fa 'Bup bup!'")

# Exemple d'ús
gos1 = Gos("Toby", "gos")
gos1.fer_soroll()  # Ha de mostrar 'Toby fa Bup bup!'
