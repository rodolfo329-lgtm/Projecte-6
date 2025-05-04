# Administració d'Aplicacions Informàtiques  
# Autor: Andres 
# Data: 03/05/2025  
# Versió: 1  

# Descripció:
# Demana una paraula a l'usuari
paraula = input("Introdueix una paraula: ")

# Converteix a minúscules per comparar millor
paraula_normalitzada = paraula.lower()

# Comprova si la paraula és igual al seu revers
if paraula_normalitzada == paraula_normalitzada[::-1]:
    print("És un palíndrom!")
else:
    print("No és un palíndrom.")
