from modelo.entidad.libro import Libro

class PrestamoDetalle:
    def __init__(self, libro: Libro, cantidad):
        self.__libro = libro.titulo
        self.__cantidad = cantidad
    
    def __repr__(self):
        return f"{self.__libro} - {self.__cantidad}"

    @property
    def libro(self):
        return self.__libro
    @property
    def cantidad(self):
        return self.__cantidad