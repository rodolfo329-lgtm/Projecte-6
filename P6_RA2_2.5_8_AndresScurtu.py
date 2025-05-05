# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 05/05/2025  
# Versió: 1  
# Descripció:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Exemples de crida
print(factorial(5))  # Mostra: 120
print(factorial(0))  # Mostra: 1
