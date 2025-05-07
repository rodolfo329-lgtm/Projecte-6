# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
class CompteBancari:
    # Constructor amb saldo inicial (per defecte 0)
    def __init__(self, saldo=0):
        self.saldo = saldo

    # Mètode per ingressar diners
    def ingressar(self, quantitat):
        if quantitat > 0:
            self.saldo += quantitat
        else:
            print("La quantitat ha de ser positiva.")

    # Mètode per retirar diners
    def retirar(self, quantitat):
        if 0 < quantitat <= self.saldo:
            self.saldo -= quantitat
        else:
            print("No es pot retirar aquesta quantitat.")

    # Mètode per veure el saldo
    def veure_saldo(self):
        print(f"Saldo actual: {self.saldo}€")

# Exemple d'ús
compte = CompteBancari()
compte.ingressar(500)
compte.retirar(150)
compte.veure_saldo()
