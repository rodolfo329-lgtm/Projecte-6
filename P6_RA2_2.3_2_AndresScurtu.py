# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 30/04/2025  
# Versió: 1  
# Descripció:
# Suma de 1 fins a n
try:
    n = int(input("Introdueix un nombre enter positiu: "))
    if n > 0:
        suma = sum(range(1, n + 1))
        print(f"La suma dels nombres de 1 fins a {n} és {suma}")
    else:
        print("Error: El nombre ha de ser positiu.")
except ValueError:
    print("Error: Has d'introduir un nombre enter positiu.")
