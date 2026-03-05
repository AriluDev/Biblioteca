class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__stock = 10
        self.__disponibilidad = True
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def stock(self):
        return self.__stock
    
    @property
    def disponibilidad(self):
        return self.__disponibilidad