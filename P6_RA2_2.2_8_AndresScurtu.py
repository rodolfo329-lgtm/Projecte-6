# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 30/04/2025  
# Versió: 1  
# Descripció:
# Comptar vocals
frase = input("Introdueix una frase: ").lower()
vowels = "aeiou"
comptador = sum(1 for lletra in frase if lletra in vowels)
print(f"La frase conté {comptador} vocals.")
