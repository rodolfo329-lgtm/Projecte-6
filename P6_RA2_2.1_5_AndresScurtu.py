# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 25/04/2025  
# Versió: 1  

# Descripció:
from datetime import date

# Demana l'any de naixement i calcula l'edat
any_naixement = int(input("Introdueix el teu any de naixement: "))
any_actual = date.today().year
edat = any_actual - any_naixement

print(f"Tens {edat} anys.")
if edat >= 18:
    print("Ets major d'edat.")
else:
    print("No ets major d'edat.")
