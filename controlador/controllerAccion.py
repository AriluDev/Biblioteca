from vista.prestarlibro import prestarLibro
from vista.devolverlibro import devolverLibro

class AccionController:

    def __init__(self, servicioPrestar, servicioDevolver, repPre):
        self.servicioPrestar = servicioPrestar
        self.servicioDevolver = servicioDevolver
        self.repPre = repPre

    def ejecutarAccion(self, accion, usuario):

        if accion == "1":
            libro = prestarLibro.ventanaPrestarLibro()
            print("Elegiste prestar el libro:", libro)

            self.servicioPrestar.prestarLibro(usuario.nombre, libro, self.repPre)

        elif accion == "2":
            libro = devolverLibro.ventanaDevolverLibro()
            print("Elegiste devolver el libro:", libro)

            self.servicioDevolver.devolverLibro(usuario.nombre, libro)

        elif accion == "3":
            print("Gracias por usar la biblioteca")
            exit()

        else:
            print("Opción no válida")