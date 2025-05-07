# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
# Definició de la classe Estudiant
class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota

    def ha_aprovat(self):
        return self.nota >= 5

# Creant una llista d'estudiants
estudiants = [
    Estudiant("Maria", 7.5),
    Estudiant("Joan", 4.2),
    Estudiant("Carla", 6.8),
    Estudiant("Pau", 3.9)
]

# Mostrant només els que han aprovat
print("Estudiants que han aprovat:")
for estudiant in estudiants:
    if estudiant.ha_aprovat():
        print(f"{estudiant.nom} ha aprovat amb un {estudiant.nota}")
