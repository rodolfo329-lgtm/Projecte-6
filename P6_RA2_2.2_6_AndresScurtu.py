# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 30/04/2025  
# Versió: 1  
# Descripció:
# Mostrar els 10 primers termes de Fibonacci
a, b = 0, 1
print("Seqüència de Fibonacci:")
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()
