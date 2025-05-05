# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 05/05/2025  
# Versió: 1  
# Descripció:
def multiplica_tot(*nombres):
    resultat = 1
    for n in nombres:
        resultat *= n
    return resultat

# Exemples de crida
print(multiplica_tot(2, 3, 4))     # Mostra: 24
print(multiplica_tot(5))           # Mostra: 5
print(multiplica_tot())            # Mostra: 1 (no hi ha cap número, es retorna 1 per convenció)
