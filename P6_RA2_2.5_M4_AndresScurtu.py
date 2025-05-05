# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 05/05/2025  
# Versió: 1  
# Descripció:
# Simulació de llençament de dau

import random

def llençar_dau():
    """
    Llença un dau i retorna el resultat (un número entre 1 i 6).
    :return: Número aleatori entre 1 i 6
    """
    return random.randint(1, 6)

def llençar_dau_n_vegades(n):
    """
    Llença un dau n vegades i calcula la mitjana dels resultats.
    :param n: Nombre de vegades que es llençarà el dau
    :return: Mitjana dels resultats dels llençaments
    """
    resultats = [llençar_dau() for _ in range(n)]
    mitjana = sum(resultats) / len(resultats)
    return resultats, mitjana

# Programa principal
if __name__ == "__main__":
    n = int(input("Quantes vegades vols llençar el dau? "))
    resultats, mitjana = llençar_dau_n_vegades(n)
    
    print(f"Resultats dels {n} llençaments: {resultats}")
    print(f"La mitjana dels resultats és: {mitjana:.2f}")
