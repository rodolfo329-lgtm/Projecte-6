# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
class Llibre:
    # Constructor amb títol, autor i any
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any

    # Mètode per mostrar la informació del llibre
    def mostrar_info(self):
        print(f"Títol: {self.titol}")
        print(f"Autor: {self.autor}")
        print(f"Any: {self.any}")

# Exemple d'ús
llibre1 = Llibre("1984", "George Orwell", 1949)
llibre1.mostrar_info()
