from modelo.entidad.usuario import Usuario

class RepositorioUsuario:
    def __init__(self):
        self.__usuarios = []

    def agregarUsuarios(self, *usuarios: Usuario):
        coincidencias = []

        for usuario in usuarios:
            if any(usuario.nombre == existente.nombre for existente in self.__usuarios):
                coincidencias.append(usuario)
            else:
                self.__usuarios.append(usuario)

        if coincidencias:
            print(f"Los siguientes usuarios no han sido agregados porque ya existen: {coincidencias}")
    
    def eliminarUsuarios(self, *usuarios: Usuario):
        coincidencias = []

        for usuario in usuarios:
            if any(usuario.nombre == existente.nombre for existente in self.__usuarios):
                self.__usuarios.remove(usuario)
            else:
                coincidencias.append(usuario)
        
        if coincidencias:
            print(f"Los siguientes usuarios no han sido eliminados porque no existen: {coincidencias}")

    def buscarPorNombre(self, nombreUsuario: Usuario):
        for usuario in self.__usuarios:
            if usuario.nombre == nombreUsuario:
                return usuario
        return None

    def listarUsuarios(self):
        return self.__usuarios.copy()