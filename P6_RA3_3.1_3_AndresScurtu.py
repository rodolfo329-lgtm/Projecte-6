# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
class Persona:
    # Constructor amb nom i edat
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    # Mètode per presentar-se
    def presentar_se(self):
        print(f"Hola, soc {self.nom} i tinc {self.edat} anys.")

# Exemple d'ús
persona1 = Persona("Andres", 18)
persona1.presentar_se()
