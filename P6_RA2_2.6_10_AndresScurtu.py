# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 05/05/2025  
# Versió: 1  
# Descripció:
# Operació amb fitxers on pot haver-hi un error durant la lectura
try:
    fitxer = open('fitxer_dades.txt', 'r')
    contingut = fitxer.read()
    print(f"Contingut del fitxer: {contingut}")
except FileNotFoundError:
    print("Error: El fitxer no existeix.")
except Exception as e:
    print(f"Error inesperat: {e}")
finally:
    # Assegura't de tancar el fitxer, independentment de si ha hagut error o no
    if 'fitxer' in locals():
        fitxer.close()
        print("Fitxer tancat correctament.")
