# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 30/04/2025  
# Versió: 1  
# Descripció:
# Comprova si un número és primer
num = int(input("Introdueix un número positiu: "))
if num < 2:
    print("No és primer.")
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("No és primer.")
            break
    else:
        print("És un nombre primer.")
