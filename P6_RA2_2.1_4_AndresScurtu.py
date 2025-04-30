# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 25/04/2025  
# Versió: 1  

# Descripció:
# Demana una nota i indica si és aprovat o suspès
nota = int(input("Introdueix una nota (1-10): "))
if nota >= 5 and nota <= 10:
    print("Aprovat")
elif nota < 5 and nota >= 0:
    print("Suspès")
else:
    print("Nota no vàlida")
