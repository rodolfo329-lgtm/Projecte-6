# Administració d'Aplicacions Informàtiques  
# Autor: Andres 
# Data: 03/05/2025  
# Versió: 1  

# Descripció:
# Funció per eliminar espais d'una cadena
def elimina_espais(cadena):
    return cadena.replace(" ", "")

# Demana la cadena a l'usuari
text = input("Introdueix una cadena amb espais: ")

# Mostra el resultat
print("Sense espais:", elimina_espais(text))
