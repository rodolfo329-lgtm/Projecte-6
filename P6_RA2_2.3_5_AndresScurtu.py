# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 30/04/2025  
# Versió: 1  
# Descripció:
# Funció per comprovar si un nombre és primer
def es_primer(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Demana un nombre i mostra tots els primers fins a aquest
try:
    n = int(input("Introdueix un nombre enter positiu: "))
    if n < 2:
        print("Has d'introduir un nombre igual o més gran que 2.")
    else:
        print(f"Nombres primers de 2 fins a {n}:")
        for i in range(2, n + 1):
            if es_primer(i):
                print(i, end=" ")
except ValueError:
    print("Error: Has d'introduir un nombre enter positiu.")
