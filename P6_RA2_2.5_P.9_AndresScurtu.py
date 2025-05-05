# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 05/05/2025  
# Versió: 1  
# Descripció:
# Definir la funció que classifica l'estat segons l'edat
def estat_persona(edat):
    if edat < 18:
        return "menor d'edat"
    elif edat < 65:
        return "adult"
    else:
        return "jubilat"

# Llista d’edats
edats = [12, 25, 70]

# Cridar la funció per cada edat i imprimir el resultat
for edat in edats:
    print(f"Edat {edat}: {estat_persona(edat)}")
