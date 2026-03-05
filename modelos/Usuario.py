class Usuario:
    def __init__(self, nombre, contrasena):
        self.__nombre = nombre
        self.__contrasena = contrasena
        self.__membresia = None
        self.__librosPrestados = []
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def membresia(self):
        return self.__membresia
    
    @property
    def librosPrestados(self):
        return self.__librosPrestados
    
    """ def verificarContrasena(self, contrasena):
        return self.__contrasena == contrasena """