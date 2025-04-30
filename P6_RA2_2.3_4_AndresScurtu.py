# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 30/04/2025  
# Versió: 1  
# Descripció:
# Mostrar nombres parells fins a n
try:
    n = int(input("Introdueix un nombre enter: "))
    print("Nombres parells fins a", n, ":")
    for i in range(0, n + 1, 2):
        print(i, end=" ")
except ValueError:
    print("Error: Has d'introduir un nombre enter.")
