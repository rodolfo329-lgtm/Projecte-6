# temps.py

def segons_a_hores(segons):
    """
    Converteix segons a hores.
    :param segons: Temps en segons
    :return: Temps en hores
    """
    return segons / 3600

def segons_a_minuts(segons):
    """
    Converteix segons a minuts.
    :param segons: Temps en segons
    :return: Temps en minuts
    """
    return segons / 60

def hores_a_segons(hores):
    """
    Converteix hores a segons.
    :param hores: Temps en hores
    :return: Temps en segons
    """
    return hores * 3600
