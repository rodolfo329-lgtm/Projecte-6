# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 05/05/2025  
# Versió: 1  
# Descripció:
# Definir la funció amb un paràmetre per defecte
def saluda_nom(nom="amic"):
    print(f"Bon dia, {nom}!")

# Crides a la funció
saluda_nom("Joan")   # Sortida: Bon dia, Joan!
saluda_nom()         # Sortida: Bon dia, amic!
saluda_nom("Laia")   # Sortida: Bon dia, Laia!
