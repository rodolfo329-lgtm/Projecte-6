# Administració d'Aplicacions Informàtiques  
# Autor: Andres 
# Data: 03/05/2025  
# Versió: 1  

# Descripció:
# Funció que reverteix una cadena
def reverteix_cadena(cadena):
    return cadena[::-1]

# Demana una cadena a l'usuari
text = input("Introdueix una cadena: ")

# Mostra el resultat
print("Cadena invertida:", reverteix_cadena(text))
