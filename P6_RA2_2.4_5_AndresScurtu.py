# Administració d'Aplicacions Informàtiques  
# Autor: Andres 
# Data: 03/05/2025  
# Versió: 1  

# Descripció:
# Demana una frase a l'usuari
frase = input("Introdueix una frase: ")

# Substitueix totes les "a" i "A" per "@"
frase_modificada = frase.replace("a", "@").replace("A", "@")

# Mostra el resultat
print("Frase modificada:", frase_modificada)

