from modelo.repositorio.repositorioUsuario import RepositorioUsuario
from modelo.repositorio.repositorioLibro import RepositorioLibro
from modelo.repositorio.repositorioPrestamo import RepositorioPrestamo
from modelo.entidad.prestamo import Prestamo

class ServicioPrestarLibro:
    def __init__(self, usuarios: RepositorioUsuario, libros: RepositorioLibro):
        self.__usuarios = usuarios
        self.__libros = libros

    def prestarLibro(self, nombreUsuario, tituloLibro):
        usuario = self.__usuarios.buscarPorNombre(nombreUsuario)
        libro = self.__libros.buscarPorTitulo(tituloLibro)

        if usuario.membresia.prestamosPermitidos > len(usuario.librosPrestados):
            libro.reducirStock()
            prestamo = Prestamo(usuario, libro)
            usuario.librosPrestados.append(prestamo)

        print("Préstamo exitoso.")
