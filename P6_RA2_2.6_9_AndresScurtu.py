# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 05/05/2025  
# Versió: 1  
# Descripció:
# Intentar obrir un fitxer en mode lectura, si no existeix, creem un nou fitxer
try:
    with open('fitxer.txt', 'r') as fitxer:
        contingut = fitxer.read()
        print(f"Contingut del fitxer: {contingut}")
except FileNotFoundError:
    # Si el fitxer no existeix, el creem i escrivim una línia
    with open('fitxer.txt', 'w') as fitxer:
        fitxer.write("Fitxer creat automàticament\n")
    print("El fitxer no existia, s'ha creat automàticament.")
