import datetime
from .libro import Libro
from .usuario import Usuario

class Prestamo:
    def __init__(self, libro: Libro, usuario: Usuario):
        self.__libro = libro
        self.__usuario = usuario
        self.__fecha = datetime.datetime.now()
    
    @property
    def libro(self):
        return self.__libro
    
    @property
    def usuario(self):
        return self.__usuario
    
    @property
    def fecha(self):
        return self.__fecha.strftime("%x")