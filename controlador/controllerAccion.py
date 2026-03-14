from vista.prestarlibro import prestarLibro
from vista.devolverlibro import devolverLibro

class AccionController:

    def ejecutarAccion(self, accion):

        if accion == "1":
            libro = prestarLibro.ventanaPrestarLibro()
            print("Elegiste prestar el libro:", libro)

        elif accion == "2":
            libro = devolverLibro.ventanaDevolverLibro()
            print("Elegiste devolver el libro:", libro)

        else:
            print("Opción no válida")