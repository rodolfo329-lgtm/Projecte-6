# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 05/05/2025  
# Versió: 1  
# Descripció:
# Gestionar errors d'escriptura
try:
    with open('resultats.txt', 'w') as fitxer:
        fitxer.write("Això és un resultat.\n")
except PermissionError:
    print("Error: No tens permís per escriure en aquest fitxer.")
except FileNotFoundError:
    print("Error: El fitxer no existeix.")
