import datetime
from modelos.prestamo import Prestamo

class Devolucion:
    def __init__(self):
        self.__fecha = datetime.datetime.now()

    @property
    def fecha(self):
        return self.__fecha.strftime("%x")
    
    def devolver(self):
        pass