import datetime
from .devolucionDetalle import DevolucionDetalle
from .usuario import Usuario


class Devolucion:
    def __init__(self, usuario: Usuario):
        self.__fecha = datetime.datetime.now()
        self.__usuario = usuario
        self.__librosDevueltos = []

    @property
    def fecha(self):
        return self.__fecha.strftime("%x")
    
    def agregarDetalle(self, *devolucionDetalle: DevolucionDetalle):
        for libro in devolucionDetalle:
            self.__librosDevueltos.append(libro)