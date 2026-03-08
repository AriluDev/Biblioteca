class Membresia:
    def __init__(self, nombre, prestamosPermitidos):
        self.__nombre = nombre
        self.__prestamosPermitidos = prestamosPermitidos
    
    def __str__(self):
        return f"{self.__nombre}"

    def __repr__(self):
        return self.__str__()

    @property
    def nombre(self):
        return self.__nombre

    @property
    def prestamosPermitidos(self):
        return self.__prestamosPermitidos