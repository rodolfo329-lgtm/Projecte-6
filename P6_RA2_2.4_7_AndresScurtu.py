# Administració d'Aplicacions Informàtiques  
# Autor: Andres 
# Data: 03/05/2025  
# Versió: 1  

# Descripció:
# Demana una cadena i una lletra
cadena = input("Introdueix una cadena: ")
lletra = input("Introdueix la lletra que vols comptar: ")

# Comprova que l'usuari ha introduït una sola lletra
if len(lletra) != 1:
    print("Has d'introduir només una lletra.")
else:
    # Comptar quantes vegades apareix la lletra (sense diferenciar majúscules i minúscules)
    comptador = cadena.lower().count(lletra.lower())
    print(f"La lletra '{lletra}' apareix {comptador} vegades a la cadena.")
