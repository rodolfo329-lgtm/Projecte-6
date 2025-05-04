# Administració d'Aplicacions Informàtiques  
# Autor: Andres 
# Data: 03/05/2025  
# Versió: 1  

# Descripció:
# Crear una llista buida
paraules = []

# Demanar 5 paraules a l'usuari
for i in range(5):
    paraula = input(f"Introdueix la paraula {i+1}: ")
    paraules.append(paraula)

# Mostrar la llista amb les paraules
print("Les paraules introduïdes són:", paraules)
