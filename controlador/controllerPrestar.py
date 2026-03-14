from vista import limpiar_pantalla
from modelo.repositorio.repositorioLibro import RepositorioLibro

class controllerPrestar:
    def prestarLibro(self, usuario, nombreLibro):
        self.servicio.prestarLibro(usuario, nombreLibro)
        print("Libro prestado correctamente.")