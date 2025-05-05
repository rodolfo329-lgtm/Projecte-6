# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 05/05/2025  
# Versió: 1  
# Descripció:
# Llegir i escriure en un fitxer
try:
    with open('sortida.txt', 'r+') as fitxer:
        contingut = fitxer.read()
        print("Contingut original del fitxer:")
        print(contingut)

        # Afegir una línia nova al final
        fitxer.write("Aquesta és una línia afegida en mode r+.\n")
except FileNotFoundError:
    print("Error: El fitxer no existeix.")
