# Administració d'Aplicacions Informàtiques  
# Autor: Andres 
# Data: 03/05/2025  
# Versió: 1  

# Descripció:
# Crear les dues llistes buides
parells = []
senars = []

# Demanar 10 números a l'usuari
for i in range(10):
    numero = int(input(f"Introdueix el número {i+1}: "))
    
    # Comprovar si el número és parell o senar
    if numero % 2 == 0:
        parells.append(numero)
    else:
        senars.append(numero)

# Mostrar les dues llistes
print("Llista de números parells:", parells)
print("Llista de números senars:", senars)
