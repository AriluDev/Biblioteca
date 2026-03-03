class Usuario:
    def __init__(self, nombre, contrasena):
        self.__nombre = nombre
        self.__contrasena = contrasena
    
    @property
    def nombre(self):
        return self.__nombre