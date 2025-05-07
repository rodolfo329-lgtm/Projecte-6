# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
# Definició de la classe Cotxe
class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

    def mostrar_informacio(self):
        print(f"Marca: {self.marca}")
        print(f"Model: {self.model}")
        print(f"Any: {self.any}")

# Instanciant dos cotxes
cotxe1 = Cotxe("Tesla", "Model S", 2022)
cotxe2 = Cotxe("Ford", "Mustang", 2020)

# Imprimint la informació dels cotxes
print("Informació Cotxe 1:")
cotxe1.mostrar_informacio()

print("\nInformació Cotxe 2:")
cotxe2.mostrar_informacio()
