# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
class Cotxe:
    # Constructor per inicialitzar els atributs
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

    # Mètode per mostrar la informació del cotxe
    def mostrar_informacio(self):
        print(f"Marca: {self.marca}")
        print(f"Model: {self.model}")
        print(f"Any: {self.any}")

# Exemple d'ús
cotxe1 = Cotxe("Seat", "Ibiza", 2018)
cotxe1.mostrar_informacio()
