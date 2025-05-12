# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 12/05/2025  
# Versió: 1  
# Descripció: Solució del codig
class Factura:
    def __init__(self, client, import_total, impressora):
        self.client = client
        self.import_total = import_total
        self.impressora = impressora  # Impressora injectada des de fora

    def imprimir_factura(self):
        contingut = f"Factura per a {self.client}, total: {self.import_total}"
        self.impressora.imprimir(contingut)

# Exemple d'ús:
class ImpressoraPDF:
    def imprimir(self, contingut):
        print(f"Imprimint PDF: {contingut}")

impressora = ImpressoraPDF()
factura = Factura("Andres", 250.0, impressora)
factura.imprimir_factura()

