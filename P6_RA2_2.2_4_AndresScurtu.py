# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 30/04/2025  
# Versió: 1  
# Descripció:
import random

# Joc d'endevinar número entre 1 i 100
secret = random.randint(1, 100)
intents = 0

while True:
    intents += 1
    guess = int(input("Endevina el número (1-100): "))
    if guess < secret:
        print("Massa baix.")
    elif guess > secret:
        print("Massa alt.")
    else:
        print(f"Correcte! Ho has encertat en {intents} intents.")
        break
