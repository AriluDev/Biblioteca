class Prestamo:
    def __init__(self, libro, usuario, fecha):
        self.__libro = libro
        self.__usuario = usuario
        self.__fecha = fecha
    
    @property
    def libro(self):
        return self.__libro
    
    @property
    def usuario(self):
        return self.__usuario
    
    @property
    def fecha(self):
        return self.__fecha