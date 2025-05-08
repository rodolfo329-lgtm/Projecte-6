# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 08/05/2025  
# Versió: 1  
# Descripció:
class Llibre:
    def __init__(self, titol, autor):
        self.titol = titol
        self.autor = autor

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}")

class LlibrePaper(Llibre):
    def __init__(self, titol, autor, n_pagines):
        super().__init__(titol, autor)
        self.n_pagines = n_pagines

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}, Pàgines: {self.n_pagines}")

class LlibreDigital(Llibre):
    def __init__(self, titol, autor, format):
        super().__init__(titol, autor)
        self.format = format

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}, Format: {self.format}")

# Exemple d'ús
paper = LlibrePaper("1984", "George Orwell", 328)
digital = LlibreDigital("El Petit Príncep", "Antoine de Saint-Exupéry", "PDF")

paper.mostrar_info()
digital.mostrar_info()
