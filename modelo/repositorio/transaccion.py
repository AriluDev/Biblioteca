from modelos.prestamo import Prestamo
from modelos.usuario import Usuario

class Transaccion:
    def __init__(self):
        self.__transacciones = []
        self.__prestamos = []
        self.__devoluciones = []

    def agregarPrestamo(self, prestamo: Prestamo):
        self.__prestamos.append(prestamo)
        self.__transacciones.append(Prestamo)

    def eliminarPrestamo(self, prestamo: Prestamo):
        self.__prestamos.remove(prestamo)

    def listarPrestamos(self):
        return self.__prestamos.copy()