# Administració d'Aplicacions Informàtiques  
# Autor: Andres 
# Data: 03/05/2025  
# Versió: 1  

# Descripció:
# Demana una cadena a l'usuari
cadena = input("Introdueix una cadena: ")

# Comprova que la cadena no estigui buida
if len(cadena) > 0:
    print("Primera lletra:", cadena[0])
    print("Última lletra:", cadena[-1])
else:
    print("Has d'introduir almenys una lletra.")
