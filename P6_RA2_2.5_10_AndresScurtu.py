# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 05/05/2025  
# Versió: 1  
# Descripció:
def filtra_parells(llista):
    return [n for n in llista if n % 2 == 0]

# Exemple de crida
nombres = [1, 2, 3, 4, 5, 6]
parells = filtra_parells(nombres)
print(parells)  # Mostra: [2, 4, 6]
