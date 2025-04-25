# Administració d'Aplicacions Informàtiques  
# Autor: Andres 

# Data: 24/04/2025  
# Versió: 1  

# Descripció: Aquest codi calcula l'àrea d'un cercle.
# Especificacions de l'entrega: Suma dos nombres predefinits i mostra el resultat.
 
import math

PI = 3.1416  # Constant (Resposta a "Quines són les constants?")

def calcular_area(radi):  # Aquesta part és una funció (Resposta a "Quina part és una funció?")
    return PI * radi ** 2

radi = float(input("Introdueix el radi: "))  # Aquesta línia llegeix dades de l'usuari (Resposta a "Quina línia llegeix dades de l'usuari?")
# Variables: radi, area (Resposta a "Quines són les variables?")
area = calcular_area(radi)
print("L'àrea del cercle és:", area)  # Aquesta línia mostra el resultat (Resposta a "Quina línia mostra el resultat?")
