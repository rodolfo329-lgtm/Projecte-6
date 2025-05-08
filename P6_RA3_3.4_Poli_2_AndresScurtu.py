# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 08/05/2025  
# Versió: 1  
# Descripció:
class Figura:
    def dibuixar(self):
        print("Dibuixant una figura...")

class Cercle(Figura):
    def dibuixar(self):
        print("Dibuixant un cercle")

class Quadrat(Figura):
    def dibuixar(self):
        print("Dibuixant un quadrat")

class Triangle(Figura):
    def dibuixar(self):
        print("Dibuixant un triangle")

# Crear llista de figures
figures = [Cercle(), Quadrat(), Triangle()]

# Recórrer la llista i cridar dibuixar()
for figura in figures:
    figura.dibuixar()
