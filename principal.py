# principal.py
import constants

def calcular_força_gravitatoria(massa):
    """
    Calcula la força gravitatòria sobre un objecte.
    :param massa: Massa de l'objecte en kg
    :return: La força gravitatòria en Newtons
    """
    return massa * constants.GRAVETAT

# Exemple d'ús
massa = float(input("Introdueix la massa de l'objecte (en kg): "))
força = calcular_força_gravitatoria(massa)

print(f"La força gravitatòria sobre un objecte de {massa} kg és {força:.2f} N.")
