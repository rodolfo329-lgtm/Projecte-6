# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 30/04/2025  
# Versió: 1  
# Descripció:
# Generar una seqüència de 0 fins al número introduït
try:
    n = int(input("Introdueix un nombre enter: "))
    for i in range(n + 1):
        print(i, end=" ")
except ValueError:
    print("Error: Has d'introduir un nombre enter.")
