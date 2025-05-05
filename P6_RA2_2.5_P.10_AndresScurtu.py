# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 05/05/2025  
# Versió: 1  
# Descripció:
# Definir la funció que filtra només els nombres parells
def filtra_parells(llista):
    return [num for num in llista if num % 2 == 0]

# Llistes d’exemple
llista1 = [1, 2, 3, 4, 5, 6]
llista2 = [10, 15, 20, 25, 30]

# Aplicar la funció i imprimir els resultats
print(filtra_parells(llista1))  # Sortida: [2, 4, 6]
print(filtra_parells(llista2))  # Sortida: [10, 20, 30]
