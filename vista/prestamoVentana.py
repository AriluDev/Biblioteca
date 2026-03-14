from vista import limpiar_pantalla
from modelo.repositorio.repositorioLibro import RepositorioLibro

class PrestamoVentana:
    def mostrar(self, repLib: RepositorioLibro):
        limpiar_pantalla()
        print("\nLista de Libros:")
        libros = repLib.listarLibros()
        for libro in libros:
            print(f"- {libro}")
        print("\n")
        nombreLibro = input("Nombre del libro: ")