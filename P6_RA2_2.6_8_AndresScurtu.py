# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 05/05/2025  
# Versió: 1  
# Descripció:
# Llegir fitxer amb nombres i evitar que es bloquegi si el format no és correcte
try:
    with open('nombres.txt', 'r') as fitxer:
        for linia in fitxer:
            try:
                # Intentem convertir la línia a enter
                nombre = int(linia.strip())
                print(f"Número llegit: {nombre}")
            except ValueError:
                # Si no és un enter vàlid, captura l'error i mostra un missatge
                print(f"Error: '{linia.strip()}' no és un nombre vàlid.")
except FileNotFoundError:
    print("Error: El fitxer 'nombres.txt' no existeix.")
