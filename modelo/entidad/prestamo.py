import datetime
from .prestamoDetalle import PrestamoDetalle
from .usuario import Usuario

class Prestamo:
    def __init__(self, usuario: Usuario):
        self.__fecha = datetime.datetime.now()
        self.__usuario = usuario
        self.__librosPrestados = []

    def __str__(self):
        return f"{self.fecha}. {self.__usuario.nombre} {self.__librosPrestados}."

    def agregarDetalle(self, *prestamoDetalle: PrestamoDetalle):
        for libro in prestamoDetalle:
            self.__librosPrestados.append(libro)

    @property
    def fecha(self):
        return self.__fecha.strftime("%x")
       
    @property
    def usuario(self):
        return self.__usuario
   
    @property
    def librosPrestados(self):
        return self.__librosPrestados