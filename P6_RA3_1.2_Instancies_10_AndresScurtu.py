# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
# Definició de la classe Persona
class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

# Funció per mostrar les persones amb més de 30 anys
def mostrar_majors_de_30(persones):
    print("Persones amb més de 30 anys:")
    for persona in persones:
        if persona.edat > 30:
            print(f"{persona.nom}, {persona.edat} anys")

# Creant una llista de persones
persones = [
    Persona("Joan", 25),
    Persona("Maria", 35),
    Persona("Carla", 40),
    Persona("Pau", 29)
]

# Cridant la funció per mostrar les persones amb més de 30 anys
mostrar_majors_de_30(persones)
