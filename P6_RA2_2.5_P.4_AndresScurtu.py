# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 05/05/2025  
# Versió: 1  
# Descripció:
# Definir la funció es_parell(numero)
def es_parell(numero):
    return numero % 2 == 0

# Llista de nombres
llista = [1, 2, 3, 4, 5, 6]

# Recórrer la llista i imprimir si cada número és parell
for num in llista:
    print(f"El número {num} és parell: {es_parell(num)}")
