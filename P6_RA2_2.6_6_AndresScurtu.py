# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 05/05/2025  
# Versió: 1  
# Descripció:
# Comprovar si el fitxer existeix abans de llegir-lo
import os

if os.path.exists('dades.txt'):
    with open('dades.txt', 'r') as fitxer:
        contingut = fitxer.read()
        print(contingut)
else:
    print("Error: El fitxer dades.txt no existeix.")
