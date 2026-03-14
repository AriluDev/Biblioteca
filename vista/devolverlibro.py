from vista import limpiar_pantalla
from modelo.repositorio.repositorioLibro import RepositorioLibro

class devolverLibro:
    def ventanaDevolverLibro():
        limpiar_pantalla()
        print("\nDevolver un libro")
        nombreLibro = input("Escribe el nombre del libro que deseas devolver: ")
        return nombreLibro