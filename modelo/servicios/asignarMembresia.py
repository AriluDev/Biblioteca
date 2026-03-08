from modelo.repositorio.repositorioUsuario import RepositorioUsuario
from modelo.repositorio.repositorioMembresia import RepositorioMembresia

class AsignarMembresia:
    def __init__(self, usuarios: RepositorioUsuario, membresias: RepositorioMembresia):
        self.__usuarios = usuarios
        self.__membresias = membresias

    def asignarMembresia(self, nombreUsuario, nombreMembresia):
        usuario = self.__usuarios.buscarPorNombre(nombreUsuario)
        membresia = self.__membresias.buscarPorNombre(nombreMembresia)

        usuario.membresia = membresia