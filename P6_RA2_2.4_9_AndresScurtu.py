# Administració d'Aplicacions Informàtiques  
# Autor: Andres 
# Data: 03/05/2025  
# Versió: 1  

# Descripció:
# Demana una frase a l'usuari
frase = input("Introdueix una frase: ")

# Divideix la frase en paraules
paraules = frase.split()

# Mostra cada paraula en una línia nova
print("Les paraules són:")
for paraula in paraules:
    print(paraula)
