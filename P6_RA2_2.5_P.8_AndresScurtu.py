# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 05/05/2025  
# Versió: 1  
# Descripció:
# Definir la funció que calcula el factorial d'un nombre
def factorial(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat

# Crides a la funció
print(factorial(0))  # Sortida: 1
print(factorial(3))  # Sortida: 6
print(factorial(5))  # Sortida: 120
