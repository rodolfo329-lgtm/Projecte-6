# geometria.py
import math

def area_quadrat(costat):
    """
    Calcula l'àrea d'un quadrat.
    :param costat: Longitud del costat del quadrat
    :return: Àrea del quadrat
    """
    return costat ** 2

def area_cercle(radi):
    """
    Calcula l'àrea d'un cercle.
    :param radi: Radi del cercle
    :return: Àrea del cercle
    """
    return math.pi * (radi ** 2)

def area_rectangle(base, altura):
    """
    Calcula l'àrea d'un rectangle.
    :param base: Longitud de la base del rectangle
    :param altura: Alçada del rectangle
    :return: Àrea del rectangle
    """
    return base * altura
