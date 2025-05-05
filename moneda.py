# moneda.py

def euros_a_dollars(euros, taxa_canvi=1.1):
    """
    Converteix euros a dòlars.
    :param euros: Quantitat d'euros
    :param taxa_canvi: Taxa de canvi de l'euro al dòlar (per defecte és 1.1)
    :return: Quantitat en dòlars
    """
    return euros * taxa_canvi

def dollars_a_euros(dollars, taxa_canvi=1.1):
    """
    Converteix dòlars a euros.
    :param dollars: Quantitat de dòlars
    :param taxa_canvi: Taxa de canvi de l'euro al dòlar (per defecte és 1.1)
    :return: Quantitat en euros
    """
    return dollars / taxa_canvi
