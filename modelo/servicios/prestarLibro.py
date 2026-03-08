from modelo.repositorio.repositorioUsuario import RepositorioUsuario
from modelo.repositorio.repositorioLibro import RepositorioLibro

class ServicioPrestarLibro:
    def __init__(self, usuarios: RepositorioUsuario, libros: RepositorioLibro):
        self.__usuarios = usuarios
        self.__libros = libros

    def prestarLibro(self, nombreUsuario, tituloLibro):
        usuario = self.__usuarios.buscarPorNombre(nombreUsuario)
        libro = self.__libros.buscarPorTitulo(tituloLibro)

        libro.reducirStock()
