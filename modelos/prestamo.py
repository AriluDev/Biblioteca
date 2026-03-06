import datetime
from .libro import Libro
from .usuario import Usuario

class Prestamo:
    def __init__(self, libro: Libro, usuario: Usuario):
        self.__fecha = datetime.datetime.now()
        self.__libro = libro.titulo
        self.__usuario = usuario

    def __str__(self):
        return f"{self.__fechaPrestamo}. El libro \"{self.__libro}\" fue prestado por {self.__usuario}."

    def __repr__(self):
        return self.__str__()

    @property
    def fecha(self):
        return self.__fecha.strftime("%x")
    
    @property
    def libro(self):
        return self.__libro
    
    @property
    def usuario(self):
        return self.__usuario
    
    @property
    def estado(self):
        return self.__estado
    
   