# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 30/04/2025  
# Versió: 1  
# Descripció:
# Taula de multiplicar
try:
    n = int(input("Introdueix un nombre enter per veure la seva taula de multiplicar: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
except ValueError:
    print("Error: Has d'introduir un nombre enter.")
