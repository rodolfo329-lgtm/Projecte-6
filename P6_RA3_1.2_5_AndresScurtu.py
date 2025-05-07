# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
class Estudiant:
    # Constructor amb nom i nota
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota

    # Mètode per dir si ha aprovat
    def ha_aprovat(self):
        if self.nota >= 5:
            print(f"{self.nom} ha aprovat amb un {self.nota}.")
        else:
            print(f"{self.nom} no ha aprovat. Té un {self.nota}.")

# Exemple d'ús
estudiant1 = Estudiant("Maria", 7.5)
estudiant2 = Estudiant("Joan", 4.2)

estudiant1.ha_aprovat()
estudiant2.ha_aprovat()
