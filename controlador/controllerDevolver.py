from vista import limpiar_pantalla
from modelo.repositorio.repositorioLibro import RepositorioLibro

class controllerDevolver:
    def devolverLibro(self, usuario, nombreLibro):
        self.servicio.devolverLibro(usuario, nombreLibro)
        print("Libro devuelto correctamente.")