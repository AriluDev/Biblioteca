class Usuario:
    def __init__(self, nombre, contrasena):
        self.__nombre = nombre
        self.__contrasena = contrasena
        self.__membresia = None
        self.__librosPrestados = []
    
    def __str__(self):
        return f"{self.__nombre} - {self.__membresia}"

    def __repr__(self):
        return self.__str__()
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def membresia(self):
        return self.__membresia
    
    @property
    def librosPrestados(self):
        return self.__librosPrestados
    
    @membresia.setter
    def membresia(self, membresia):
        self.__membresia = membresia
