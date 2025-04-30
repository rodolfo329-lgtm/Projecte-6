# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 25/04/2025  
# Versió: 1  

# Descripció:
# Demana una lletra i indica si és vocal o consonant
lletra = input("Introdueix una lletra: ").lower()
if len(lletra) == 1 and lletra.isalpha():
    if lletra in "aeiou":
        print("És una vocal.")
    else:
        print("És una consonant.")
else:
    print("Has d'introduir una sola lletra.")
