class Usuario:
    def __init__(self, nombre, contrasena):
        self.__nombre = nombre
        self.__contrasena = contrasena
        self.__membresia = None
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def membresia(self):
        return self.__membresia