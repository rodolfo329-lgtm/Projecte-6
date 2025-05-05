# validacions.py
import re

def es_email_valid(email):
    """
    Comprova si l'email té un format vàlid.
    :param email: String amb el correu electrònic
    :return: True si l'email és vàlid, False en cas contrari
    """
    # Expressió regular per validar un email
    patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron_email, email) is not None

def es_telefon_valid(telefon):
    """
    Comprova si el número de tel
