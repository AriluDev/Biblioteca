from modelo.repositorio.repositorioLibro import RepositorioLibro

class PrestamoVentana:
    def mostrar(self, repLib: RepositorioLibro):
        print("\nLista de Libros:")
        libros = repLib.listarLibros()
        for libro in libros:
            print(f"- {libro}")
        print("\n")
        nombreLibro = input("Nombre del libro: ")