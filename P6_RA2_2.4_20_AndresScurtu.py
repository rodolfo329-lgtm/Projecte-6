# Administració d'Aplicacions Informàtiques  
# Autor: Andres 
# Data: 03/05/2025  
# Versió: 1  

# Descripció:
# Demanar una llista de paraules a l'usuari
paraules = input("Introdueix una llista de paraules separades per espais: ").split()

# Definir les vocals
vocales = "aeiouAEIOU"

# Crear una nova llista amb les paraules que comencen per vocal
paraules_per_vocal = [paraula for paraula in paraules if paraula[0] in vocales]

# Mostrar la nova llista
print("Paraules que comencen per vocal:", paraules_per_vocal)
