# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
# Definició de la classe CompteBancari
class CompteBancari:
    def __init__(self, saldo=0):
        self.saldo = saldo

    # Mètode per ingressar diners
    def ingressar(self, quantitat):
        if quantitat > 0:
            self.saldo += quantitat
            print(f"Ingrés de {quantitat}€. Nou saldo: {self.saldo}€")
        else:
            print("La quantitat ha de ser positiva.")

    # Mètode per retirar diners
    def retirar(self, quantitat):
        if 0 < quantitat <= self.saldo:
            self.saldo -= quantitat
            print(f"Retirada de {quantitat}€. Nou saldo: {self.saldo}€")
        else:
            print("No es pot retirar aquesta quantitat, saldo insuficient o quantitat invàlida.")

    # Mètode per veure el saldo
    def veure_saldo(self):
        print(f"Saldo actual: {self.saldo}€")

# Exemple d'ús
compte = CompteBancari()

# Simulant les operacions
compte.ingressar(500)  # Ingrés de 500€
compte.retirar(200)    # Retirada vàlida de 200€
compte.retirar(400)    # Retirada superior al saldo (no es pot fer)
compte.veure_saldo()   # Mostrar saldo final
