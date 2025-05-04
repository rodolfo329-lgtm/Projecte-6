# Administració d'Aplicacions Informàtiques  
# Autor: Andres 
# Data: 03/05/2025  
# Versió: 1  

# Descripció:
# Definir la funció que retorna la llista al revés
def llista_al_reves(llista):
    llista_invertida = []
    # Recórrer la llista de darrere endavant i afegir els elements a la nova llista
    for i in range(len(llista) - 1, -1, -1):
        llista_invertida.append(llista[i])
    return llista_invertida

# Exemple de llista
llista_original = [1, 2, 3, 4, 5]

# Cridar la funció i mostrar el resultat
llista_reversa = llista_al_reves(llista_original)
print("Llista original:", llista_original)
print("Llista al revés:", llista_reversa)
