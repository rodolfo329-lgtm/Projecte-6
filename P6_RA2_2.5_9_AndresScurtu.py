# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 05/05/2025  
# Versió: 1  
# Descripció:
def estat_persona(edat):
    if edat < 18:
        estat = "Menor d'edat"
        descripcio = "Té menys de 18 anys"
    elif edat < 65:
        estat = "Adult"
        descripcio = "Té entre 18 i 64 anys"
    else:
        estat = "Jubilat"
        descripcio = "Té 65 anys o més"
    return estat, descripcio

# Exemple de crida
estat, descripcio = estat_persona(18)
print(estat)        # Mostra: Jubilat
print(descripcio)   # Mostra: Té 65 anys o més
