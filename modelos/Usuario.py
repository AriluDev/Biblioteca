class Usuario:
    def __init__(self, nombre, contrasena):
        self.__nombre = nombre
        self.__contrasena = contrasena
    
    def get_nombre(self):
        return self.__nombre