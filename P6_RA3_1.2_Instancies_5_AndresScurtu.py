# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
# Definició de la classe Producte
class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu

    # Mètode per aplicar un descompte al preu
    def aplicar_descompte(self, percentatge):
        descompte = self.preu * (percentatge / 100)
        self.preu -= descompte

    def mostrar_info(self):
        print(f"Producte: {self.nom}, Preu: {self.preu:.2f}€")

# Funció per aplicar descompte a tots els productes
def aplicar_descompte_a_productes(productes, percentatge):
    for producte in productes:
        producte.aplicar_descompte(percentatge)

# Creant una llista de productes
productes = [
    Producte("Portàtil", 1000),
    Producte("Mòbil", 500),
    Producte("Auriculars", 150)
]

# Aplicant un descompte del 10% a tots els productes
aplicar_descompte_a_productes(productes, 10)

# Mostrant la informació dels productes després del descompte
for producte in productes:
    producte.mostrar_info()
