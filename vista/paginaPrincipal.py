from modelo.entidad.usuario import Usuario
from modelo.repositorio.repositorioLibro import RepositorioLibro

class PaginaPrincipalVista:
    def mostrar(repLib: RepositorioLibro, usuario:Usuario):
        print(f"Hola {usuario.nombre}, bienvenido a la biblioteca.")
        print("\nLista de Libros:")
        libros = repLib.listarLibros()
        for libro in libros:
            print(f"- {libro}")