# conversions.py

def celsius_a_fahrenheit(c):
    """
    Converteix una temperatura de Celsius a Fahrenheit.
    :param c: Temperatura en graus Celsius
    :return: Temperatura en graus Fahrenheit
    """
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    """
    Converteix una temperatura de Fahrenheit a Celsius.
    :param f: Temperatura en graus Fahrenheit
    :return: Temperatura en graus Celsius
    """
    return (f - 32) * 5/9
