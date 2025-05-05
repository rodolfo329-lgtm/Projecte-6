# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 05/05/2025  
# Versió: 1  
# Descripció:
# Comptar el nombre de línies d'un fitxer
try:
    with open('sortida.txt', 'r') as fitxer:
        linies = fitxer.readlines()
        print(f"El fitxer té {len(linies)} línies.")
except FileNotFoundError:
    print("Error: El fitxer no existeix.")
