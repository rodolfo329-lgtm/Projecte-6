# Curs: ASIX (Administració de Sistemes en Xarxa)   
# Autor: Andres  
# Data: 07/05/2025  
# Versió: 1  
# Descripció:
# Definició de la classe Llibre
class Llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any

    def mostrar_info(self):
        return f"Títol: {self.titol}, Autor: {self.autor}, Any: {self.any}"

# Definició de la classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.llibres = []  # Llista per emmagatzemar els llibres

    # Mètode per afegir un llibre a la biblioteca
    def afegir_llibre(self, llibre):
        self.llibres.append(llibre)

    # Mètode per mostrar tots els llibres
    def mostrar_llibres(self):
        if self.llibres:
            print("Llibres a la biblioteca:")
            for llibre in self.llibres:
                print(llibre.mostrar_info())
        else:
            print("No hi ha llibres a la biblioteca.")

# Exemple d'ús
# Creant una biblioteca
biblioteca = Biblioteca()

# Creant alguns llibres
llibre1 = Llibre("1984", "George Orwell", 1949)
llibre2 = Llibre("El senyor dels anells", "J.R.R. Tolkien", 1954)
llibre3 = Llibre("Cien años de soledad", "Gabriel García Márquez", 1967)

# Afegint els llibres a la biblioteca
biblioteca.afegir_llibre(llibre1)
biblioteca.afegir_llibre(llibre2)
biblioteca.afegir_llibre(llibre3)

# Mostrant tots els llibres de la biblioteca
biblioteca.mostrar_llibres()
