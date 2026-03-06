class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__stock = 10
        self.__stockMax = 10
    
    def __str__(self):
        TrueStock = f"\"{self.__titulo}\" de {self.__autor}. Stock Disponible: {self.__stock}."
        FalseStock = f"{self.__titulo} de {self.__autor}. No disponible actualmente."
        if self.__stock > 0:
            return TrueStock
        else:
            return FalseStock

    def __repr__(self):
        return f"Título: {self.__titulo} - Autor: {self.__autor} - Stock: {self.__stock}."

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def stock(self):
        return self.__stock
    
    def prestarLibro(self, cantidad = 1):
        if cantidad <= 0:
            raise Exception("No se puede prestar 0 libros")
        if cantidad > self.__stock:
            raise Exception("No hay stock disponible")
        self.__stock -= cantidad

    def devolverLibro(self, cantidad = 1):
        if cantidad <= 0:
            raise Exception("No se puede devolver 0 libros")
        if cantidad + self.__stock > self.__stockMax:
            raise Exception("Se está devolviendo más libro del stock real.")
        self.__stock += cantidad