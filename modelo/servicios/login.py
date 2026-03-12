from modelo.repositorio.repositorioUsuario import RepositorioUsuario

class Login:
    def __init__(self, usuarios: RepositorioUsuario):
        self.__usuarios = usuarios
    
    def accesoSistema(self, nombre, contrasena):
        usuario = self.__usuarios.buscarPorNombre(nombre)
        
        if usuario is None:
            raise Exception("El usuario no existe.")

        if usuario.contrasena != contrasena:
            raise Exception("Contraseña incorrecta.")

        return usuario