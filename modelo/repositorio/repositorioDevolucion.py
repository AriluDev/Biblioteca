from modelo.entidad.devolucion import Devolucion

class RepositorioDevolucion:
    def __init__(self):
        self.__devoluciones = []
    
    def __str__(self):
        return self.listarDevoluciones()

    def __repr__(self):
        return 

    def listarDevoluciones(self):
        return self.__devoluciones.copy()
