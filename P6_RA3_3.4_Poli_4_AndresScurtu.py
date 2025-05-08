# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 08/05/2025  
# Versió: 1  
# Descripció:
class Missatger:
    def enviar(self, missatge):
        pass  # Mètode base sense implementació

class Email(Missatger):
    def enviar(self, missatge):
        print(f"Enviant email: {missatge}")

class SMS(Missatger):
    def enviar(self, missatge):
        print(f"Enviant SMS: {missatge}")

class WhatsApp(Missatger):
    def enviar(self, missatge):
        print(f"Enviant WhatsApp: {missatge}")

# Funció que envia un missatge a través de diferents missatgers
def enviar_missatges(missatgers, missatge):
    for m in missatgers:
        m.enviar(missatge)

# Exemple d'ús
missatgers = [Email(), SMS(), WhatsApp()]
enviar_missatges(missatgers, "Hola, aquest és un missatge!")
