# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 12/05/2025  
# Versió: 1  
# Descripció:
class Comanda:
    def __init__(self, client, notificador):
        self.client = client
        self.notificador = notificador  # Injectem el notificador

    def confirmar(self):
        print(f"Confirmant per a {self.client}")
        self.notificador.notificar(self.client, "La teva comanda ha estat confirmada.")

# Exemple d'ús:
class EmailNotificador:
    def notificar(self, client, missatge):
        print(f"Email a {client}: {missatge}")

notificador = EmailNotificador()
comanda = Comanda("Andres", notificador)
comanda.confirmar()
