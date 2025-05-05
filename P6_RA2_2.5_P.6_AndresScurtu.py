# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 05/05/2025  
# Versió: 1  
# Descripció:
# Definir la funció que multiplica tots els nombres passats com a paràmetres
def multiplica_tot(*nombres):
    resultat = 1
    for num in nombres:
        resultat *= num
    return resultat

# Crides a la funció
print(multiplica_tot(2, 3, 4))   # Sortida: 24
print(multiplica_tot(5, 10))     # Sortida: 50
