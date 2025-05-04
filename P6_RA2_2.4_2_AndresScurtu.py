# Administració d'Aplicacions Informàtiques  
# Autor: Andres 
# Data: 03/05/2025  
# Versió: 1  

# Descripció:
# Demana una frase a l'usuari
frase = input("Introdueix una frase: ")

# Defineix les vocals
vocals = "aeiouAEIOU"
comptador = 0

# Recorre la frase i compta les vocals
for lletra in frase:
    if lletra in vocals:
        comptador += 1

# Mostra el resultat
print("La frase conté", comptador, "vocals.")
