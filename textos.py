# textos.py

def posar_majuscules(text):
    """
    Converteix el text a majúscules.
    :param text: El text a convertir
    :return: El text en majúscules
    """
    return text.upper()

def posar_minuscules(text):
    """
    Converteix el text a minúscules.
    :param text: El text a convertir
    :return: El text en minúscules
    """
    return text.lower()

def capitalitzar(text):
    """
    Capitalitza la primera lletra de cada paraula del text.
    :param text: El text a capitalitzar
    :return: El text amb la primera lletra de cada paraula en majúscules
    """
    return text.title()
