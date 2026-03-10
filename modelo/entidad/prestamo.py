import datetime
from .usuario import Usuario
from .libro import Libro

class Prestamo:
    def __init__(self, usuario: Usuario, libro: Libro):
        self.__fecha = datetime.datetime.now()
        self.__usuario = usuario
        self.__libro = libro

    def __str__(self):
        return f"{self.fecha}. {self.__usuario.nombre} prestó {self.__libro.titulo}."

    def __repr__(self):
        return f"{self.fecha} - {self.libro.titulo}"

    @property
    def fecha(self):
        return self.__fecha.strftime("%x")
       
    @property
    def usuario(self):
        return self.__usuario
   
    @property
    def libro(self):
        return self.__libro