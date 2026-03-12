from modelo.entidad.prestamo import Prestamo

class RepositorioPrestamo:
    def __init__(self):
        self.__prestamos = []
    
    def __str__(self):
        return f"{self.prestamos}"

    @property
    def prestamos(self):
        return self.__prestamos

    def agregarPrestamos(self, *prestamos: Prestamo):
        for prestamo in prestamos:
            self.__prestamos.append(prestamo)
    
    def eliminarPrestamos(self, *prestamos: Prestamo):
        for prestamo in prestamos:
            self.__prestamos.remove(prestamo)