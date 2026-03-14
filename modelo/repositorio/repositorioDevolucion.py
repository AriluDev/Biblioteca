from modelo.entidad.devolucion import Devolucion

class RepositorioDevolucion:
    def __init__(self):
        self.__devoluciones = []
    
    def __str__(self):
        return self.listarDevoluciones()

    def __repr__(self):
        return 

    def agregarDevoluciones(self, *devoluciones: Devolucion):
        for devolucion in devoluciones:
            self.__devoluciones.append(devolucion)

    def listarDevoluciones(self):
        return self.__devoluciones.copy()
