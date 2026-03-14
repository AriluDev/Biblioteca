from modelo.entidad.libro import Libro
from modelo.repositorio.repositorioLibro import RepositorioLibro
from modelo.repositorio.repositorioUsuario import RepositorioUsuario
from modelo.repositorio.repositorioDevolucion import RepositorioDevolucion

class DevolverLibro:
    def __init__(self, usuarios: RepositorioUsuario, libros: RepositorioLibro):
        self.__usuarios = usuarios
        self.__libros = libros
    
    def devolverLibro(self, nombreUsuario, nombreLibro):
        usuario = self.__usuarios.buscarPorNombre(nombreUsuario)
        libro = self.__libros.buscarPorTitulo(nombreLibro)

        libro.aunmentarStock()
        usuario.quitarPrestamo(libro)
        print("Devolución exitosa")