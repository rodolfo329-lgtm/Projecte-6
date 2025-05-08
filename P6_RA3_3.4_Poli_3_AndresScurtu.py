# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 08/05/2025  
# Versió: 1  
# Descripció:
class Empleat:
    def calcular_sou(self):
        return 0

class Fixe(Empleat):
    def __init__(self, sou_mensual):
        self.sou_mensual = sou_mensual

    def calcular_sou(self):
        return self.sou_mensual

class Autonom(Empleat):
    def __init__(self, hores, tarifa_hora):
        self.hores = hores
        self.tarifa_hora = tarifa_hora

    def calcular_sou(self):
        return self.hores * self.tarifa_hora

# Funció per mostrar sous
def mostrar_sous(llista_empleats):
    for idx, empleat in enumerate(llista_empleats, 1):
        print(f"Empleat {idx}: {empleat.calcular_sou()} €")

# Exemple d'ús
e1 = Fixe(1500)
e2 = Autonom(80, 20)
e3 = Fixe(1800)

empleats = [e1, e2, e3]
mostrar_sous(empleats)
